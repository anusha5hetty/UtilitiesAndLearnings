const jwt = require('jsonwebtoken')

const auth = (req, res, next) => {
    const jwtToken = req.header('token')
    if (!jwtToken) return res.status(401).send('Access Denied')

    try {
        const userVerified = jwt.verify(jwtToken, process.env.SECRET_TOKEN)

        req.user = userVerified
    }
    catch (ex) {
        res.status(400).send(`Something went wrong - ${ex}`)
    }
}