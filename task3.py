import hmac, hashlib

key = b'secretkey123'
with open("data.txt", "rb") as f:
    msg = f.read()

hmac_digest = hmac.new(key, msg, hashlib.sha256).hexdigest()
print(hmac_digest)
