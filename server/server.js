const express = require('express')
const bodyparser = require('body-parser');
const cors = require('cors')

const app = express()

app.use(bodyparser.urlencoded({extended: false}));
app.use(bodyparser.json());
app.use(cors());

const port = process.env.PORT || 5000;

app.get('/', (req, res) => {
  res.send('Welcome to the server!')
})

app.post("/upload_data", (req,res) => {
    let data =req.body.array;
    console.log("Uploaded Data\n\n:" + data);

    res.json({response: data});
})

app.listen(port, () => {
  console.log(`App listening on port ${port}`)
})