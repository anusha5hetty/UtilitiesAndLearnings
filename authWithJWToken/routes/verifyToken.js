const jwt = require('jsonwebtoken')

module.exports = function (req, res, next) {
    const jwtToken = req.header('token')
    if (!jwtToken) return res.status(401).send('Access Denied')

    try {
        const userVerified = jwt.verify(jwtToken, process.env.SECRET_TOKEN)
        req.user = userVerified
        next()
    }
    catch (ex) {
        res.status(400).send(`Invalid Token ${ex}`)
    }
}