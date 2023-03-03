#!/usr/bin/python3
import fire
import jwt
import json
import sys

def jwt_encode(secret):
  data = sys.stdin.read()
  j = jwt.encode(json.loads(data),secret,algorithm="HS256")
  return j

if __name__ == '__main__':
  fire.Fire(jwt_encode)