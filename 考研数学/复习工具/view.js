// Dataview custom view. Progress is stored in the vault, never in browser memory alone.
const statePath = "考研数学/复习工具/复习进度.json";
const file = dv.app.vault.getAbstractFileByPath(statePath);
if (!file) throw new Error("找不到错题复习进度文件，请检查复习工具目录。");
let data = JSON.parse(await dv.app.vault.read(file));
if (data.version !== 1 || !Array.isArray(data.items)) throw new Error("复习进度格式不正确。");
const root = dv.container.createDiv({ cls: "exam-review" });
const error = root.createDiv({ cls: "exam-review-error" });
const hosts = new Map();
const busy = new Set();

function roundName(index) {
    return ["二刷", "三刷", "四刷", "五刷", "六刷"][index] ?? `第 ${index + 2} 刷`;
}

async function save(id, index, outcome) {
    if (busy.has(id)) return;
    busy.add(id);
    renderItem(data.items.find(item => item.id === id));
    try {
        const written = await dv.app.vault.process(file, raw => {
            const latest = JSON.parse(raw);
            const item = latest.items.find(value => value.id === id);
            if (!item || index >= item.rounds.length) throw new Error("题目状态已变，请重新打开清单。");
            // A stale view must not change a hidden round after an earlier round was passed.
            if (item.rounds.slice(0, index).some(value => value !== "failed")) {
                throw new Error("前一轮状态已变，请重新操作。");
            }
            item.rounds[index] = outcome;
            if (outcome === "failed" && index === item.rounds.length - 1) item.rounds.push("pending");
            latest.updatedAt = new Date().toISOString();
            return JSON.stringify(latest, null, 2) + "\n";
        });
        data = JSON.parse(written);
        error.textContent = "";
    } catch (cause) {
        error.textContent = `未能保存，操作没有确认成功：${cause.message ?? cause}`;
    } finally {
        busy.delete(id);
        renderItem(data.items.find(item => item.id === id));
    }
}

function renderItem(item) {
    const host = hosts.get(item.id);
    if (!host) return;
    host.empty();
    for (let index = 0; index < item.rounds.length; index++) {
        const outcome = item.rounds[index];
        const row = host.createDiv({ cls: "exam-review-row" });
        row.dataset.round = String(index);
        if (index > 0) row.addClass("exam-review-retry");
        const label = row.createEl("label", { cls: "exam-review-label" });
        const checkbox = label.createEl("input", { type: "checkbox", cls: "task-list-item-checkbox" });
        checkbox.checked = outcome === "passed";
        checkbox.disabled = busy.has(item.id);
        checkbox.setAttribute("aria-label", `${item.book} ${item.question} ${roundName(index)}独立做对`);
        const title = label.createEl("span", { text: index === 0 ? item.question : roundName(index) });
        if (outcome === "passed") title.addClass("exam-review-passed");
        checkbox.addEventListener("change", () => save(item.id, index, checkbox.checked ? "passed" : "pending"));
        if (outcome !== "passed") {
            const failed = row.createEl("button", { text: outcome === "failed" ? "没做对 · 待重刷" : "没做对", cls: "exam-review-fail" });
            failed.type = "button";
            failed.disabled = busy.has(item.id) || outcome === "failed";
            failed.addEventListener("click", () => save(item.id, index, "failed"));
        }
        if (index === 0) {
            const details = row.createEl("details", { cls: "exam-review-details" });
            details.createEl("summary", { text: `记录 ${item.dates.length} 次` });
            const sources = details.createDiv();
            for (const date of item.dates) {
                const link = sources.createEl("a", { text: date, cls: "internal-link" });
                link.href = `考研数学/错题/${date}`;
                link.addEventListener("click", event => {
                    event.preventDefault();
                    dv.app.workspace.openLinkText(`考研数学/错题/${date}`, dv.currentFilePath, event.ctrlKey || event.metaKey);
                });
                sources.appendText(" ");
            }
            if (item.hint) sources.createDiv({ text: item.hint });
        }
        // Further rounds appear only after explicitly recording an incorrect attempt.
        if (outcome !== "failed") break;
    }
}

let chapter = "";
for (const item of data.items.filter(item => item.book === input.book)) {
    if (item.chapter !== chapter) {
        chapter = item.chapter;
        root.createEl("h3", { text: chapter });
    }
    const host = root.createDiv({ cls: "exam-review-item" });
    host.dataset.questionId = item.id;
    hosts.set(item.id, host);
    renderItem(item);
}

dv.component.registerEvent(dv.app.vault.on("modify", async changed => {
    if (changed.path !== statePath) return;
    try {
        data = JSON.parse(await dv.app.vault.read(file));
        for (const item of data.items) renderItem(item);
    } catch (cause) {
        error.textContent = `读取进度失败：${cause.message ?? cause}`;
    }
}));
