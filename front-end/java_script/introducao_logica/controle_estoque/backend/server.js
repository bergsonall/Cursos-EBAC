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

// READ
app.get("/produtos", (req, res) => {
  db.all("SELECT * FROM produtos", [], (err, rows) => {
    if (err) return res.status(500).json(err);
    res.json(rows);
  });
});

// UPDATE
app.put("/produtos/:id", (req, res) => {
  const { nome, quantidade, preco } = req.body;
  const { id } = req.params;

  db.run(
    "UPDATE produtos SET nome=?, quantidade=?, preco=? WHERE id=?",
    [nome, quantidade, preco, id],
    function (err) {
      if (err) return res.status(500).json(err);
      res.json({ updated: this.changes });
    }
  );
});

// DELETE
app.delete("/produtos/:id", (req, res) => {
  db.run(
    "DELETE FROM produtos WHERE id=?",
    [req.params.id],
    function (err) {
      if (err) return res.status(500).json(err);
      res.json({ deleted: this.changes });
    }
  );
});

app.listen(3000, () => {
  console.log("Servidor rodando em http://localhost:3000");
});