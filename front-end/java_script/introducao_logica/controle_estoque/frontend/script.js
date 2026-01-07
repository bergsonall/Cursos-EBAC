document.getElementById('produto-form').addEventListener('submit', (e) => {
    e.preventDefault();

    const produto = {
        nome: document.getElementById('nome').value,
        quantidade: parseInt(document.getElementById('quantidade').value),
        preco: parseFloat(document.getElementById('preco').value)
    }

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
