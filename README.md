# 📡 DevRel Pulse 📡

> An Autonomous Multi-Agent Open-Source Telemetry & Throttling Guardrail Confined within NVIDIA NemoClaw.

---

## 💡 Overview

Maintaining large-scale open-source ecosystems (like NemoClaw) poses two major operational hurdles for Developer Relations (DevRel) teams: **Alert Fatigue** from endless community telemetry noise, and **Token Bill Explosion** from naive LLM-based reactive polling.

**DevRel Pulse** solves this by implementing a **Compound AI System** designed to run 24/7 autonomously with **Zero Human in the Loop**. Instead of burning endless API tokens on static repository checks, the system orchestrates a low-cost, high-fidelity deterministic agent alongside a heavy-duty cognitive model to capture, analyze, and triage critical repository issues in under 30 seconds.

---

## 🏗️ Architecture & Multi-Agent Collaboration

DevRel Pulse bifurcates concerns into two highly specialized logic agents to maximize performance while optimizing execution costs:

```text
[GitHub Web API] ──> (Agent A: Scout) ──[State Fingerprint Hash Change?]
                     │
              [No: Silent Halt] 
                     │
              [Yes: Fetch External Intel via Tavily]
                     │
                     ▼
            (Agent B: Director) ──> [Inference via Nemotron-3 120B]
                     │
                     ▼
            [Discord Control Panel Triage Alert Card]
```

### 1. Agent A: Scout (Deterministic Orchestration)
- **Role:** Active 24/7 telemetry monitor and data sanitizer.
- **Mechanism:** Automatically intercepts raw repository events, filters out non-issue noise (such as active Pull Request floods), and computes a **Dynamic State Fingerprint (MD5 Hash)** of the active issues list.
- **Throttling:** If no state mutation is detected, the pipeline **instantly halts (fuses)**. This prevents unneeded API calls to downstream heavy LLMs, saving 100% of invalid inference costs.

### 2. Agent B: Director (Cognitive Strategy)
- **Role:** High-context executive summary and public relations draft generation.
- **Mechanism:** Triggered only when Agent A signals a legitimate repository mutation. It triggers a search radar via Tavily API for background context, aggregates the payload, and streams it into the **local `nvidia/nemotron-3-super-120b-a12b` (120B Model)** model inside the gateway. 
- **Output:** Transforms raw community frustration into production-grade triage cards on Discord with categorical ranking, immediate technical actions, and high-EQ official response drafts.

---

## 📁 Repository Structure

```text
├── src/
│   ├── agent_core.py        # Core orchestration logic & XML isolation vaults
│   ├── discord_notifier.py  # Defensive webhook handling & safety truncation
│   └── cron_scheduler.py    # Production-grade background telemetry loop
├── nemoclaw-blueprint/
│   └── policies/
│       └── presets/
│           └── devrel_final.yaml  # NemoClaw L7 sandboxing & network policies
├── .gitignore               # Strict security-first environment patterns
├── requirements.txt         # Explicit system dependencies
└── README.md                # System documentation
```

---

## 🛡️ NemoClaw Sandbox Integration & Edge-Case Defenses

This entire system is strictly confined within the **NemoClaw Linux Landlock Isolation Sandbox** to enforce security guardrails on all outbound network traffic and process execution.

During rigorous final evaluation against the official `NVIDIA/NemoClaw` repository, DevRel Pulse successfully mitigated critical real-world infrastructure bottlenecks and tracked live architectural anomalies:

- **Silent Null Token Exhaustion (#4398, Live Demo Scenario):** As demonstrated live in the companion demo video, when the inference proxy cuts off due to upstream token limits during extensive markdown synthesis, the local gateway yields a silent `200 OK` with an empty payload. DevRel Pulse dynamically intercepts this anomaly, triggering generic defensive exception fallbacks to bypass standard parser `NoneType` crashes and maintain 100% telemetry uptime.
- **Simulated Adversarial Prompt Injection (Targeting #4357):** To stress-test the Director Agent, malicious hijack commands were synthetically injected into the telemetry pipeline disguised as raw issue data ("*We need to output a highly dense telemetry report card... No intro, no chat.*"). DevRel Pulse successfully encapsulated the untrusted payload utilizing a gas-tight XML vault combined with a deterministic semantic isolation guardrail, completely neutralizing the exploit and forcing perfect compliance.
- **L7 Gateway SSL Trust Chain Disruption (#4324):** Discovered that the sandbox environment failed to inject the self-signed Root CA of `inference.local` into the sandbox OS store, forcing developers into insecure `verify=False` patterns. DevRel Pulse bypassed this using custom defensive networking and safely relayed the telemetry. 


---

## ⚡ Quick Start (Daemon Deployment)

Ensure your environment variables are configured from the project root before spinning up the persistent daemon inside the sandbox:

```bash
# Setup authentication matrix (Four Pillars)
export GITHUB_TOKEN="your_github_token"
export NVIDIA_API_KEY="your_nvapi_key"
export TAVILY_API_KEY="your_tavily_key"
export DISCORD_WEBHOOK_URL="your_discord_webhook_url"
export TARGET_REPO="NVIDIA/NemoClaw"

# Configure python path to recognize project structure
export PYTHONPATH=$PYTHONPATH:$(pwd)

# Launch persistent cron job in standby daemon mode from root path
nohup python3 src/cron_scheduler.py > daemon.log 2>&1 &

# Monitor real-time Multi-Agent handshakes
tail -f daemon.log
```

---

## 🛠️ Tech Stack

- **Core Reasoning Engine:** `nvidia/nemotron-3-super-120b-a12b` via local `inference.local` gateway.
- **Security Guardrail:** NemoClaw Sandbox Isolation (Linux Landlock LSM Blueprint).
- **Environment:** Ubuntu 26.04 LTS / **Python 3.13** / Docker 29.
- **Orchestration Tools:** Custom Hash-based state tracking, Tavily Search API, Discord Webhook payload layout engines.
