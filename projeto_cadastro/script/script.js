document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("cadastroForm");
    const mensagem = document.getElementById("mensagem");

    form.addEventListener("submit", function(event) {
        event.preventDefault();

        const email = document.getElementById("email").value;
        const senha = document.getElementById("senha").value;
        const confirmarSenha = document.getElementById("confirmarSenha").value;

        // Regex para validar e-mail
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

        // Regex para validar senha forte
        const senhaRegex = /^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;

        if (!emailRegex.test(email)) {
            mensagem.textContent = "Por favor, insira um e-mail válido.";
            return;
        }

        if (!senhaRegex.test(senha)) {
            mensagem.textContent = "A senha deve ter pelo menos 8 caracteres, 1 letra maiúscula, 1 número e 1 caractere especial.";
            return;
        }

        if (senha !== confirmarSenha) {
            mensagem.textContent = "As senhas não coincidem.";
            return;
        }

        // Se passou de todas as validações
        mensagem.style.color = "green";
        mensagem.textContent = "Cadastro realizado com sucesso!";
        form.reset();
    });
});
