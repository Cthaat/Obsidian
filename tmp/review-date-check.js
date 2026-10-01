(async () => {
    const file = app.vault.getAbstractFileByPath("考研数学/复习工具/复习进度.json");
    const id = document.querySelector(".exam-review-item")?.dataset.questionId;
    const original = JSON.parse(await app.vault.read(file)).items.find(item => item.id === id);
    const snapshot = JSON.parse(JSON.stringify(original));
    const host = () => document.querySelector(`.exam-review-item[data-question-id="${id}"]`);
    const current = async () => JSON.parse(await app.vault.read(file)).items.find(item => item.id === id);
    const expectedDate = new Intl.DateTimeFormat("sv-SE", { timeZone: "Asia/Shanghai", year: "numeric", month: "2-digit", day: "2-digit" }).format(new Date());
    const assert = (value, message) => { if (!value) throw new Error(message); };
    const wait = async predicate => {
        const deadline = Date.now() + 6000;
        while (!(await predicate())) {
            if (Date.now() > deadline) throw new Error("Date test timed out");
            await new Promise(resolve => setTimeout(resolve, 30));
        }
    };
    const toggle = index => {
        const box = host().querySelectorAll("input")[index];
        box.checked = !box.checked;
        box.dispatchEvent(new Event("change", { bubbles: true }));
    };
    try {
        await app.vault.process(file, raw => {
            const data = JSON.parse(raw);
            const item = data.items.find(item => item.id === id);
            item.rounds = ["pending"];
            delete item.completionDates;
            return JSON.stringify(data, null, 2);
        });
        await wait(() => host()?.querySelectorAll("input").length === 1 && !host().querySelector("input").checked);
        toggle(0);
        await wait(async () => (await current()).rounds[0] === "passed" && !host().querySelector("input").disabled);
        assert((await current()).completionDates?.[0] === expectedDate, "Checking must persist the Shanghai completion date");
        assert(host().querySelector(".exam-review-date")?.textContent === expectedDate, "Completion date must be visible next to the check");
        const view = app.workspace.activeLeaf.view;
        const state = view.getState();
        await view.setState({ ...state, mode: "source" }, {});
        await view.setState({ ...state, mode: "preview" }, {});
        await wait(() => host()?.querySelector(".exam-review-date")?.textContent === expectedDate);
        toggle(0);
        await wait(async () => (await current()).rounds[0] === "pending" && !host().querySelector("input").disabled);
        assert((await current()).completionDates[0] === null, "Unchecking must clear this round's date");
        assert(!host().querySelector(".exam-review-date"), "Unchecked item must hide completion date");
        host().querySelector("button").click();
        await wait(() => host().querySelectorAll("input").length === 2 && !host().querySelectorAll("input")[1].disabled);
        toggle(1);
        await wait(async () => (await current()).rounds[1] === "passed" && !host().querySelectorAll("input")[1].disabled);
        assert((await current()).completionDates[1] === expectedDate && (await current()).completionDates[0] === null, "Third attempt must save its own date");
        assert(host().querySelector('[data-round="1"] .exam-review-date')?.textContent === expectedDate, "Third-attempt date must render");
        return "PASS: check saves and displays completion date; reload preserves date; uncheck clears date; third-attempt dates are separate.";
    } finally {
        await app.vault.process(file, raw => {
            const data = JSON.parse(raw);
            const item = data.items.find(item => item.id === id);
            item.rounds = snapshot.rounds;
            if (snapshot.completionDates) item.completionDates = snapshot.completionDates;
            else delete item.completionDates;
            return JSON.stringify(data, null, 2) + "\n";
        });
    }
})()
