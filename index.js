const express = require('express');
const { post } = require('request-promise');
const app = express();

app.get('/', async(req,res)=>{
    res.send("Uploaded!");
});

app.post('/create', async (req,res) => {
    re
})

const port = (port) => {
    const fport = process.env.PORT || port;
    console.log(`app listening at port ${fport}`);

    app.listen(fport, console.log(`Test app listening at https://localhost:${fport}`));
}

port(3000);