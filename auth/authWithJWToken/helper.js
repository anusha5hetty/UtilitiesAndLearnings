const User = require('./model/User');
const bcrypt = require('bcrypt')

const createUser = async (name, password, email, role) => {
    const userDetails = await User.findOne({ email: email })
    if (!userDetails) {
        const salt = await bcrypt.genSalt(10)
        const hashedPassword = await bcrypt.hash(password, salt)
        // const hashedPassword = await bcrypt.hash(process.env.SUPERADMIN_PWD, salt)

        // Create new user
        const reqPayload = {
            name: name,
            password: hashedPassword,
            email: email,
            role: role
        }

        const user = new User(reqPayload);

        try {
            const savedUser = await user.save()
            console.log("SAVED USER", JSON.stringify(savedUser))
        }
        catch (ex) {
            console.log("ERROR OCCURED", ex)
        }
    }
    else {
        console.log(`${name} already exists.`)
    }

}

module.exports = { createUser }