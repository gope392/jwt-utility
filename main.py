import os
import jwt
import datetime
import uuid
import sys

def generate_jwt(input_data, secret):
    try:
        # Fill required claims
        iat = datetime.datetime.utcnow()
        jti = uuid.uuid4()
        payload = {'data': input_data, 'date': datetime.date.today().strftime('%Y-%m-%d')}
        # Generate JWT Token
        jwt_payload = {'iat': iat, 'jti': str(jti), 'payload': payload}
        jwt_token = jwt.encode(jwt_payload, secret, algorithm='HS512')
        print('JWT Token has been successfully generated: ', jwt_token)
        return jwt_token
    except Exception as e:
        print(e)

def validate_jwt(jwt_token, secret):
    try:
        # Validate JWT Token
        jwt_json = jwt.decode(jwt_token, secret, algorithms='HS512')
        print('JWT Token has been correctly decrypted', jwt_json)
        return jwt_json
    except Exception as e:
        print(e)

def read_secret(filepath):
    try:
        with open(filepath, 'r') as file:
            secret = file.read()
            return secret
    except Exception as e:
        print(e)

# Validate input data
input_data = os.environ.get('input_data')
if not input_data:
    print('Empty input data. Exiting')
    exit()
else:
    secret = read_secret('secret.txt')
    jwt_token = generate_jwt(input_data, secret)
    validate_jwt(jwt_token, secret)

