import json
import urllib.request
import os
from datetime import datetime

WEBHOOK_URL = os.environ["WEBHOOK_URL"]

msg = {
  "embeds": [{
    "description": "test",
    "timestamp": datetime.now(datetime.UTC).isoformat(),
  }]
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
