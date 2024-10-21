import json
import urllib.request
import os
import datetime
import psutil

WEBHOOK_URL = os.environ["WEBHOOK_URL"]

i = 0
cpus = []
for cpu in psutil.cpu_percent(interval=0.3, percpu=True):
  cpus.append({
    "name": f"CPU{i}",
    "value": f"{cpu}%",
    "inline": True,
  })
  i += 1

vm = psutil.virtual_memory()

msg = {
  "embeds": [{
    "fields": [
      *cpus,
      {
        "name": "Memory",
        "value": f"{vm.percent}%",
      }
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
