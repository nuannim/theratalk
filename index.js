const express = require("express");
const path = require("path");
const port = 3000;

// Creating the Express server
const app = express();


app.use(express.static('public'));
app.set('view engine', 'ejs');


app.get('/', function (req, res) {
    res.render('home_p');
});

app.get('/lesson', function (req, res) {
    res.render('lesson_p');
});

app.get('/progress', function (req, res) {
    res.render('progress_p');
});

app.get('/profile', function (req, res) {
    res.render('profile_p');
});

app.get('/home', function (req, res) {
    res.render('home_patient');
});


app.listen(port, () => {
    console.log(`listening to port ${port}`);
});