const sqlite3 = require("sqlite3").verbose();
const path = require("path");
const fs = require("fs");

// garante que a pasta db existe
const dbDir = path.join(__dirname, "db");
if (!fs.existsSync(dbDir)) {
  fs.mkdirSync(dbDir);
}

// caminho absoluto do banco
const dbPath = path.join(dbDir, "app.db");

const db = new sqlite3.Database(dbPath, (err) => {
  if (err) {
    console.error("Erro ao conectar no banco:", err.message);
  } else {
    console.log("Banco SQLite conectado com sucesso!");
  }
});

db.exec(require("fs").readFileSync("schema.sql", "utf8"));

module.exports = db;