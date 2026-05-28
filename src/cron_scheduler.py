import os
import sys
import time
import logging
from src.agent_core import run_dual_brain_intel

# Flexible Integration: Prioritize modular Discord engine with a graceful fallback
try:
    from src.discord_notifier import send_to_discord
except ImportError:
    import requests
    def send_to_discord(content):
        url = os.getenv("DISCORD_WEBHOOK_URL")
        if url:
            requests.post(url, json={"content": content})
        return True

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s]: %(message)s')
logger = logging.getLogger("DevRelPulseScheduler")

# Polling Telemetry: Dynamic audit interval via environment variable (defaulting to 15s)
INTERVAL = int(os.getenv("AUDIT_INTERVAL", 15))

def main():
    logger.info("⏰ [Scheduler] DevRel Pulse Autonomous Daemon Activated.")
    logger.info(f"⏱️ Telemetry audit interval configuration: Enforcing {INTERVAL}s loop boundary.")
    
    try:
        while True:
            # 1. Trigger core multi-agent federation telemetry (Scout & Director orchestrations)
            report = run_dual_brain_intel()
            
            # 2. If the cognitive layer captures a repository delta, dispatch via notifier network
            if report:
                logger.info("🔥 [Scheduler] Dynamic repository delta captured! Dispatched to notifier network.")
                send_to_discord(report)
            
            # 3. Enter quiet standby cooldown period to mitigate alert fatigue
            logger.info(f"⏳ Standby: {INTERVAL} seconds until the next telemetry audit...\n")
            time.sleep(INTERVAL)
            
    except KeyboardInterrupt:
        # 🛑 Gracefully catch KeyboardInterrupt (SIGINT) to ensure a clean daemon shutdown
        logger.info("🛑 [Scheduler] Autonomous daemon gracefully terminated by maintainer signal.")
        sys.exit(0)
    except Exception as e:
        logger.error(f"💥 [Scheduler] Unhandled infrastructure failure in daemon loop: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
