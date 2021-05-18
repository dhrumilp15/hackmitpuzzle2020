import jwt
import time
import base64
import json
import string

possible = string.ascii_letters + string.digits

def bash_jwt(cookie):
    payload = cookie.split(".")[2]
    payload = base64.b64decode(payload)
    payload = json.loads(payload)

    def recurse(public_key):
        public_key.append(possible[itera])
        
        encoded = jwt.encode(payload, ''.join(public_key),algorithm='HS256')
        if encoded.decode() == cookie:
            return PUBLIC_KEY
        
    

cookie = input("The cookie monster wants cookies! >:( :")

print(f"THE KEY IS: {bash_jwt(cookie)}")
