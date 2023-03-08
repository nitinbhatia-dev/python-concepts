import jwt
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

private_key = None#b'-----BEGIN OPENSSH PRIVATE KEY----- \n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 \nCHt5JHJuBRsX78cpua2QlF5gQSw= \n-----END OPENSSH PRIVATE KEY-----'
#with open("C:\\Users\\nitin\\jwtRS256.key",mode='r',encoding='UTF-8') as f:
with open("C:\\Users\\nitin\\private.pem",mode='r',encoding='UTF-8') as f:
    private_key = f.read()
    #print(t)
print(private_key)
print(type(private_key))

public_key = None
#with open("C:\\Users\\nitin\\jwtRS256.key.pub",mode='r',encoding='UTF-8') as f:
with open("C:\\Users\\nitin\\public.pem",mode='r',encoding='UTF-8') as f:
    public_key = f.read()
#private_key_bytes:bytes = bytes(private_key,encoding="UTF-8")
#passphrase = b"dummy"
encoded = jwt.encode(payload={"Message":"Hello"}, key=private_key, algorithm="RS256",)
#private_key_passphrase = serialization.load_pem_private_key(private_key,password=passphrase,backend=default_backend())

#encoded = jwt.encode(payload={"Message":"Hello"}, key=private_key_passphrase, algorithm="RS256")
print(encoded)

decoded = jwt.decode(encoded,key=public_key,algorithms="RS256")

print(decoded)