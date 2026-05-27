import time
import logging
from agent_core import run_dual_brain_intel
from discord_notifier import send_to_discord

if __name__ == "__main__":
    INTERVAL = 30  # 演示期間設定 30 秒自動通報一次
    logging.info(f"⚡ OpenShell Autonomous Cron Job instantiated. Frequency: every {INTERVAL}s.")
    
    while True:
        try:
            report_content = run_dual_brain_intel()
            send_to_discord(report_content)
        except Exception as e:
            logging.error(f"Main Scheduler Loop interrupted: {e}")
        time.sleep(INTERVAL)
