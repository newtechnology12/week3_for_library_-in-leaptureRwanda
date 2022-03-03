import jwt
encoded = jwt.encode({"some": "payload"}, "secret", algorithm="HS256")
print(encoded)

jwt.decode(encoded, "secret", algorithms=["HS256"])
{'some': 'payload'}