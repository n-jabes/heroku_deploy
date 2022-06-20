const express = require('express');
const app = express();

app.get('/', async(req,res)=>{
    res.send("Uploaded!");
});

const port = () => {
    const PORT = process.env.PORT || 3000;
    console.log(`app listening at port ${PORT}`);

    app.listen(PORT, console.log(`Example app listening at https://localhost:${PORT}`));
}