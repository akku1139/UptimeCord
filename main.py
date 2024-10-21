import json
import urllib.request
import os

WEBHOOK_URL = os.environ["WEBHOOK_URL"]

msg = {
  "content": "test"
}

headers = {
  "Content-Type": "application/json",
  "User-Agent": "DiscordBot (https://github.com/akku1139/UptimeCord, 0.0.1)",
}

req = urllib.request.Request(
  WEBHOOK_URL,
  json.dumps(msg).encode(),
  headers,
  method="POST",
)

with urllib.request.urlopen(req) as res:
  body = res.read()
  print(body)
