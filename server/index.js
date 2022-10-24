const express = require("express");
const app = express();
const mysql = require("mysql");
const cors = require("cors");

app.use(cors());
app.use(express.json());

const db = mysql.createConnection({
  user: "root",
  host: "localhost",
  password: "password",
  database: "test_schema",
});

app.get("/", (req, res) => {
  db.query("SELECT * FROM mapping_table", (err, result) => {
    dict = {}
    if (err) {
      console.log(err);
    } else {
      for(i=0; i<result.length; i++) {
        dict[result[i].address] = result[i].isVerified
      }
      res.send(dict);
    }
  });
});

PORT = process.env.PORT || 5000;

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});