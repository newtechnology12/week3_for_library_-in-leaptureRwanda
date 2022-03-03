from flask import *
from flask_bcrypt import Bcrypt
# import json as _json


app = Flask(__name__)
bcrypt = Bcrypt(app)

print("welcome this the flask-Bcrypt: ")
hash_generate_password = bcrypt.generate_password_hash('albert20986')
 # returns marching password
pw_hashs = bcrypt.generate_password_hash('albert20986', 20)
check = bcrypt.check_password_hash(hash_generate_password, 'albert20986')
print(pw_hashs)

if check:
    print("yes: your password is marching")
else:
    print("No: your password is incorrect, please correct your password")