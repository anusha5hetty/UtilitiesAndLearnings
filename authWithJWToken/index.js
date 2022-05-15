const mongoose = require('mongoose');
const dotenv = require('dotenv')

// Connect to DB
dotenv.config();
mongoose.connect(process.env.DB_CONNECT, { useNewUrlParser: true }, () => {
    console.log("[Anusha] Connected to DB", process.env.DB_CONNECT)
})

const express = require('express');
const authRoute = require('./routes/auth')
const app = express();


// Middleware
//To read the request body. Without this req.body will not have any value
// TODO: Find Why not ?
app.use(express.json())

// Import Routes
app.use('/api/user', authRoute);



// Listner
app.listen(3000, () => console.log('[Anusha] Connected to the app server'))