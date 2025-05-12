document.addEventListener("DOMContentLoaded", () => {
  const form = document.querySelector("form");

  form.addEventListener("submit", (e) => {
    const username = form.querySelector("input[name='username']").value.trim();
    const password = form.querySelector("input[name='password']").value;
    const confirm = form.querySelector("input[name='confirm']").value;

    if (!username || !password || !confirm) {
      alert("Preencha todos os campos.");
      e.preventDefault();
      return;
    }

    if (password !== confirm) {
      alert("As senhas não coincidem.");
      e.preventDefault();
    }
  });
});
