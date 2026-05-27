import json
import logging
import requests

DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1508740002996162723/COExBbC_blfUauuXeE6y6_M7RouTW_niT5pgViyReYIUIUuT-dHRRZ6xVnmK-8yhc1I2"

def send_to_discord(content):
    if not content.strip():
        logging.error("❌ Discord Engine: Content is empty!")
        return False

    # 阻斷 400 錯誤：實施 2000 字元鋼鐵律法安全截斷
    if len(content) > 1900:
        logging.warning(f"⚠️ 報告長度 ({len(content)}) 超過 Discord 上限。正在實施安全防護截斷...")
        content = content[:1900] + "\n\n⚠️ *(由於 Discord 訊息長度限制，其餘深度資安情資已由 NemoClaw 安全加密封存)*"

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
