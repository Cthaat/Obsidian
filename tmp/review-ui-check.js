(async () => {
    const path = "考研数学/复习工具/复习进度.json";
    const file = app.vault.getAbstractFileByPath(path);
    const original = JSON.parse(await app.vault.read(file)).items.find(item => item.id === "q-001").rounds;
    const assert = (condition, message) => { if (!condition) throw new Error(message); };
    const host = () => document.querySelector('.exam-review-item[data-question-id="q-001"]');
    const state = async () => JSON.parse(await app.vault.read(file)).items.find(item => item.id === "q-001").rounds;
    const wait = async predicate => {
        const deadline = Date.now() + 6000;
        while (!(await predicate())) {
            if (Date.now() > deadline) throw new Error("Timed out waiting for saved UI state");
            await new Promise(resolve => setTimeout(resolve, 30));
        }
    };
    const clickCheckbox = index => {
        const checkbox = host().querySelectorAll('input[type="checkbox"]')[index];
        checkbox.checked = !checkbox.checked;
        checkbox.dispatchEvent(new Event("change", { bubbles: true }));
    };
    try {
        // Isolate this item and restore it afterward; no other progress is touched.
        await app.vault.process(file, raw => {
            const data = JSON.parse(raw);
            data.items.find(item => item.id === "q-001").rounds = ["pending"];
            return JSON.stringify(data, null, 2);
        });
        await wait(() => host()?.querySelectorAll('input[type="checkbox"]').length === 1);
        assert(document.querySelectorAll('.exam-review-item').length === 363, "All 363 items must render");
        assert(document.querySelectorAll('.exam-review-item input[type="checkbox"]').length === 363, "Initial state must show exactly one checkbox per item");
        host().querySelector('button').click();
        await wait(async () => (await state())[0] === "failed" && host().querySelectorAll('input').length === 2);
        assert(host().textContent.includes("三刷"), "Wrong second attempt must show third attempt");
        // Re-render the note to prove the third attempt is restored from disk.
        const view = app.workspace.activeLeaf.view;
        const current = view.getState();
        await view.setState({ ...current, mode: "source" }, {});
        await view.setState({ ...current, mode: "preview" }, {});
        await wait(() => host()?.querySelectorAll('input').length === 2);
        host().querySelector('[data-round="1"] button').click();
        await wait(async () => (await state())[1] === "failed" && host().querySelectorAll('input').length === 3);
        assert(host().textContent.includes("四刷"), "Wrong third attempt must show fourth attempt");
        clickCheckbox(1);
        await wait(async () => (await state())[1] === "passed" && host().querySelectorAll('input').length === 2);
        assert(host().querySelectorAll('input')[1].checked, "Correct third attempt must be checked");
        clickCheckbox(0);
        await wait(async () => (await state())[0] === "passed" && host().querySelectorAll('input').length === 1);
        assert(host().querySelector('input').checked, "Correct second attempt must leave just one checked box");
        clickCheckbox(0);
        await wait(async () => (await state())[0] === "pending" && !host().querySelector('input').checked);
        return "PASS: 363 items, one initial checkbox each; incorrect expands third/fourth attempts; correct collapses retries; reload preserves state; uncheck works.";
    } finally {
        await app.vault.process(file, raw => {
            const data = JSON.parse(raw);
            data.items.find(item => item.id === "q-001").rounds = original;
            return JSON.stringify(data, null, 2) + "\n";
        });
    }
})()
