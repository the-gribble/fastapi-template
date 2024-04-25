import jwt

# used to test the result of token decoding

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzYW0iLCJleHAiOjE3MTM5NzI1Mjl9.pDyGGoWNO4MzhxUGI8BqNfAA9UOztrQquB8fXcv4EBs"
decoded_token = jwt.decode(token, options={"verify_signature": False})  # Decode without verification
print(decoded_token)  # Check the claims
