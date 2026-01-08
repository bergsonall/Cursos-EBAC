// Código para a página index.html
document.addEventListener("DOMContentLoaded", () => {

    const form = document.getElementById("produto-form");
    if (!form) return;

    form.addEventListener("submit", (e) => {
        e.preventDefault();

        const produto = {
            nome: document.getElementById("nome").value,
            quantidade: parseInt(document.getElementById("quantidade").value),
            preco: parseFloat(document.getElementById("preco").value)
        };

        fetch("http://localhost:3000/produtos", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(produto)
        })
            .then(res => res.json())
            .then(data => {
                console.log("Produto adicionado:", data);
            })
            .catch(err => console.error("Erro ao adicionar produto:", err));
    })
});

// Código para a página alterar.html
document.addEventListener("DOMContentLoaded", () => {

    const form = document.getElementById("altera-form");
    if (!form) return;

    form.addEventListener("submit", (e) => {
        e.preventDefault();

        const produto = {
            nome: document.getElementById('nome').value,
            quantidade: parseInt(document.getElementById('quantidade').value),
            preco: parseFloat(document.getElementById('preco').value)
        }

        fetch("http://localhost:3000/produtos", {
            method: "PUT",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(produto)
        })
            .then(res => res.json())
            .then(data => {
                console.log("Produto alterado:", data);
            })
            .catch(err => console.error("Erro ao alterar produto:", err));
    })
});

// Código para a página excluir.html
document.addEventListener("DOMContentLoaded", () => {

    const form = document.getElementById("exclui-form");
    if (!form) return;

    form.addEventListener('submit', (e) =>{
        e.preventDefault();

        const produto = {
            nome: document.getElementById('nome').value
        }
        fetch("http://localhost:3000/produtos", {
            method: "DELETE",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(produto)
        })
            .then(res => res.json())
            .then(data => {
                console.log("Produto excluído:", data);
            })
            .catch(err => console.error("Erro ao excluir produto:", err));
    })
});

// Código para a página relatorio.html
document.addEventListener("DOMContentLoaded", () => {
    const tabela = document.getElementById("tabela-produtos");
    if (!tabela) return;
    fetch("http://localhost:3000/produtos")
        .then(res => res.json())
        .then(data => {
            data.forEach(produto => {
                const row = tabela.insertRow();
                row.insertCell(0).innerText = produto.nome;
                row.insertCell(1).innerText = produto.quantidade;
                row.insertCell(2).innerText = produto.preco.toFixed(2);
            });
        })
        .catch(err => console.error("Erro ao carregar produtos:", err));
})