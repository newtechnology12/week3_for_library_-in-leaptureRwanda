from cerberus import Validator

v = Validator()
v.schema = {"contact_details": {
    "type": "dict",
    "schema": {
        "phone": {
            "type": "string",
            "minlength": 10,
            "maxlength": 10,
            "regex": "^0[0-9]{9}$"
        },
        "email": {
            "type": "string",
            "minlength": 8,
            "maxlength": 255,
            "required": True,
            "regex": "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$"
        }
    }
}}

if v.validate({'contact_details': {'phone': '078503077223',
                                   'email': 'twayigizealbert12@gmail.com'}}):
    print('your email and number is valid data')
else:
    print('invalid data')
    print(v.errors)
