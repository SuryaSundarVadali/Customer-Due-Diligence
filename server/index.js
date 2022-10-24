const express = require("express");
const app = express();
const mysql = require("mysql");
const cors = require("cors");

app.use(cors());
app.use(express.json());

const db = mysql.createConnection({
  user: "root",
  host: "localhost",
  password: "yathin017",
  database: "test_schema",
});

app.get("/", (req, res) =>{
  res.send('[{"address":"0xB245B4DBEe83064CDd975D31Af9edA5f6a4508A4","isVerified":0},{"address":"0xE6707721ad79f4519f80D95ef4D961b60893CD76","isVerified":1}]');
})

app.get("/mappings", (req, res) => {
  db.query("SELECT * FROM mapping_table", (err, result) => {
    if (err) {
      console.log(err);
    } else {
      res.send(result);
    }
  });
});

app.listen(3001, () => {
  console.log("Server is running on port 3001");
});