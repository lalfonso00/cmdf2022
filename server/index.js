// server/index.js

const express = require("express");
const fs = require('fs')

const PORT = process.env.PORT || 3001;

const app = express();





app.get("/api", (req, res) => {
    res.json({ message: "Hello from server!" });
});

app.get("/jpi", (req, res) => {
    res.json({ message: "Hello from server!" });
});

app.listen(PORT, () => {
    console.log(`Server listening on ${PORT}`);
});

const mongoose = require('mongoose');

main().catch(err => console.log(err));

async function main() {
    const kittySchema = new mongoose.Schema({
        name: String
    });
    // const dbconnect = await fs.readFile('uri.txt', 'utf8', (err, data) => {
    //     if (err) {
    //         console.error(err)
    //         return
    //     }
    //     console.log(typeof data)
    //     return data
    // })

    console.log(dbconnect)
    await mongoose.connect(dbconnect).then(console.log("connected to db!"));
    const Kitten = mongoose.model('Kitten', kittySchema);
    const silence = new Kitten({ name: 'Silence' });
    console.log(silence.name)
    await silence.save()


    const kittens = await Kitten.find();
    console.log(kittens);

}