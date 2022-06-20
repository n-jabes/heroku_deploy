const express = require('express');
const app = express();

app.get('/', async(req,res)=>{
    res.send("Uploaded!");
});

const port = (port) => {
    const PORT = process.env.PORT || port;
    console.log(`app listening at port ${PORT}`);

    app.listen(PORT, console.log(`Test app listening at https://localhost:${PORT}`));
}

port(3000);