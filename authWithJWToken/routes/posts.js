const router = require('express').Router();
const verifyToken = require('./verifyToken')


router.get('/', verifyToken, (req, res) => {
    res.json({ posts: { 'title': 'Title of the post', 'description': 'Well this is the description' } })
})

module.exports = router
