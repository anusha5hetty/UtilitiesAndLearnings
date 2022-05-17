const router = require('express').Router();
const User = require('./../model/User');
const bcrypt = require('bcrypt')
const jwt = require('jsonwebtoken')
const { registerUserReqValidation, loginReqValidation } = require('./../validations/validation.js');


router.post('/register',
    async (req, res) => {
        const validateRes = registerUserReqValidation(req.body)

        if (validateRes.error) {

            res.status(400).send(validateRes.error)
        }
        else {
            console.log("Inisde Else part 1")
            const userDetails = await User.findOne({ email: req.body.email })

            // Check if user exists
            if (userDetails) return res.status(400).send('User already exists')
            console.log("Inisde Else part 2")
            // Hash password
            const salt = await bcrypt.genSalt(10)
            const hashedPassword = await bcrypt.hash(req.body.password, salt)
            console.log("Inisde Else part 3")
            // Create new user
            const reqPayload = {
                name: req.body.name,
                password: hashedPassword,
                email: req.body.email,
                role: req.body.role
            }

            const user = new User(reqPayload);

            try {
                const savedUser = await user.save()
                console.log("SAVED USER", JSON.stringify(savedUser))
                res.status(201).send()
            }
            catch (ex) {
                console.log("EXCEPTION OCCURED", ex)
                res.status(400).send(ex)
            }
        }
    }
);


router.post('/login',
    async (req, res) => {
        const validateRes = loginReqValidation(req.body)

        if (validateRes.error) {

            res.status(400).send(validateRes.error)
        }
        else {
            // const reqPayload = {
            //     name: req.body.name,
            //     password: req.body.password,
            //     email: req.body.email
            // }

            const userDetails = await User.findOne({ email: req.body.email })
            if (!userDetails) return res.status(400).send('User email or password not correct')

            const validPwd = await bcrypt.compare(req.body.password, userDetails.password)
            if (!validPwd) return res.status(401).send('Authentication Failed')


            const jwtToken = jwt.sign({ email: userDetails.email, name: userDetails.name, _id: userDetails._id }, process.env.SECRET_TOKEN)
            res.header('tokne', jwtToken)

            res.status(200).send('Hurrah!! Logged In')

        }
    }
);

module.exports = router;