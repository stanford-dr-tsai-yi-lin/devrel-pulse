import os
import json
import logging
import requests

# SECURITY GUARDRAIL: Fetch from environment matrix to prevent credential leakage
DISCORD_WEBHOOK_URL = os.environ.get("DISCORD_WEBHOOK_URL")

def send_to_discord(content):
    if not DISCORD_WEBHOOK_URL:
        logging.error("❌ Discord Engine: DISCORD_WEBHOOK_URL environment variable is missing!")
        return False

    if not content.strip():
        logging.error("❌ Discord Engine: Content is empty!")
        return False

    # Prevent HTTP 400 Bad Request: Enforce Discord's 2000 character strict limit
    if len(content) > 1900:
        logging.warning(f"⚠️ Payload length ({len(content)}) exceeds Discord limits. Enforcing safety truncation...")
        content = content[:1900] + "\n\n⚠️ *(Due to Discord's payload limits, further telemetry data has been securely vaulted by NemoClaw)*"

    payload = {"content": content}
    headers = {"Content-Type": "application/json"}
    try:
        response = requests.post(DISCORD_WEBHOOK_URL, data=json.dumps(payload), headers=headers)
        if response.status_code in [200, 204]:
            logging.info("🎯 Discord Engine: Report successfully tunneled to Command Center.")
            return True
        else:
            logging.error(f"❌ Discord Engine: Delivery failed with Status Code {response.status_code}")
            return False
    except Exception as e:
        logging.error(f"💥 Discord Engine: Connection exception: {e}")
        return False
