const Joi = require('@hapi/joi')


const registerUserReq = (data) => {
    const userSchema = Joi.object({
        name: Joi.string().required().min(6),
        password: Joi.string().required().max(1024),
        email: Joi.string().required().email().min(10).max(255),
        role: Joi.string().required().valid('Admin', 'BasicUser')
    });

    const error = userSchema.validate(data)
    return error
}

const loginReq = (data) => {
    const userSchema = Joi.object({
        name: Joi.string().required().min(6),
        password: Joi.string().required().max(1024),
        email: Joi.string().required().email().min(10).max(255),
    });

    const error = userSchema.validate(data)
    return error
}


module.exports = { registerUserReqValidation: registerUserReq, loginReqValidation: loginReq }