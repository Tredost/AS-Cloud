document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector("form");

    form.addEventListener("submit", (e) => {
        const username = form.querySelector("input[name='username']").value;
        const password = form.querySelector("input[name='password']").value;

        if (!username || !password) {
            alert("Preencha todos os campos.");
            e.preventDefault();
        }
    });
});