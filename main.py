import json
import urllib.request
import os
import datetime

WEBHOOK_URL = os.environ["WEBHOOK_URL"]

msg = {
  "embeds": [{
    "fields": [
      {
        "name": "CPU",
        "value": "xx.x %"
      },
    ],
    "timestamp": datetime.datetime.now(datetime.UTC).isoformat(),
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
