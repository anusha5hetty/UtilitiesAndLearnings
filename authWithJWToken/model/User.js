const mongoose = require('mongoose');

const userSchema = mongoose.Schema({
    name: {
        type: String,
        required: true,
        min: 6
    },
    password: {
        type: String,
        required: true,
        max: 1024
    },
    email: {
        type: String,
        required: true,
        min: 10,
        max: 255
    },
    date: {
        type: Date,
        default: Date.now(),
        required: false
    }
})

module.exports = mongoose.model('User', userSchema)