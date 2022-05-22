const mongoose = require('mongoose');
const dotenv = require('dotenv')
const express = require('express');
const authRoute = require('./routes/auth')
const postsRoute = require('./routes/posts')
const { createUser } = require('./helper.js')

// Connect to DB
dotenv.config();

mongoose.connect(process.env.DB_CONNECT, { useNewUrlParser: true }, () => {
    console.log("[Anusha] Connected to DB", process.env.DB_CONNECT)
})

const app = express();

// Middleware
//To read the request body. Without this req.body will not have any value
// TODO: Find Why not ?
app.use(express.json())


createUser(process.env.SUPERADMIN_USR, process.env.SUPERADMIN_PWD, process.env.SUPERADMIN_EMAIL, process.env.SUPERADMIN_ROLE)


// Import Routes
app.use('/api/user', authRoute);
app.use('/api/posts', postsRoute);


// Listner
app.listen(3000, () => console.log('[Anusha] Connected to the app server'))