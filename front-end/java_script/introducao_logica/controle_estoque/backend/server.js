const express = require("express");
const db = require("./database");
const cors = require("cors");

const app = express();
app.use(express.json());
app.use(cors());

// CREATE
app.post("/produtos", (req, res) => {
  const { nome, quantidade, preco } = req.body;

  db.run(
    "INSERT INTO produtos (nome, quantidade, preco) VALUES (?, ?, ?)",
    [nome, quantidade, preco],
    function (err) {
      if (err) return res.status(500).json(err);
      res.json({ id: this.lastID });
    }
  );
});

// UPDATE
app.put('/produtos', (req, res) => {
  const { nome, quantidade, preco } = req.body;


  if (!nome) {
    return res.status(400).json({ erro: 'Nome do produto é obrigatório' });
  }


  db.run(
    `UPDATE produtos SET quantidade = ?, preco = ? WHERE nome = ?`,
    [quantidade, preco, nome],
    function (err) {
      if (err) return res.status(500).json(err);


      if (this.changes === 0) {
        return res.status(404).json({ erro: 'Produto não encontrado' });
      }


      res.json({ mensagem: 'Produto alterado com sucesso' });
    }
  );
});

// DELETE
app.delete("/produtos", (req, res) => {
  const { nome } = req.body;

  db.run(
    "DELETE FROM produtos WHERE nome=?",
    [nome],
    function (err) {
      if (err) return res.status(500).json(err);
      res.json({ mensagem: 'Produto excluído com sucesso' });
    }
  );
});

app.listen(3000, () => {
  console.log("Servidor rodando em http://localhost:3000");
});