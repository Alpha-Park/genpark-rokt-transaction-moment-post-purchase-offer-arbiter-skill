# genpark-rokt-transaction-moment-post-purchase-offer-arbiter-skill

[![Official Hub](https://img.shields.io/badge/GenPark-Official%20Hub-6366f1?style=for-the-badge&logo=compass&logoColor=white)](https://www.genpark.ai)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-GenPark-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/company/92955550)
[![MCP SDK](https://img.shields.io/badge/MCP_SDK-required-blue?style=for-the-badge)](requirements.txt)
[![MCP Compliant](https://img.shields.io/badge/MCP-JSON--RPC%202.0-blue?style=for-the-badge)](https://www.genpark.ai)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

> **Official Website**: [https://www.genpark.ai](https://www.genpark.ai)  
> **LinkedIn**: [https://www.linkedin.com/company/92955550](https://www.linkedin.com/company/92955550)

Rokt-inspired Transaction Moment & Post-Purchase Retail Media Offer Arbiter. Leverages contextual multi-armed bandit sampling, customer brand affinity filtering, and eCPM yield arbitrage to serve the highest-converting third-party and native offers at checkout and thank-you pages.

---

## MCP runtime requirements

Use Python 3.10 or newer. The core `client.py` uses only the standard library; `mcp_server.py` requires the official `mcp` SDK (`mcp>=1.0.0,<2`). From this repository's checkout, create an isolated environment and install its requirements:

```bash
python -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
```

On Windows, use `.venv\Scripts\python.exe` instead. You may use an existing Python environment with the requirements installed. Configure your MCP client with that interpreter's absolute path and the absolute path to `mcp_server.py`. The client launches a local STDIO process; the GitHub repository URL is not a remote MCP endpoint.

Example client configuration (replace the placeholder paths):

```json
{
  "mcpServers": {
    "genpark-rokt-transaction-moment-post-purchase-offer-arbiter-skill": {
      "command": "/absolute/path/to/genpark-rokt-transaction-moment-post-purchase-offer-arbiter-skill/.venv/bin/python",
      "args": [
        "/absolute/path/to/genpark-rokt-transaction-moment-post-purchase-offer-arbiter-skill/mcp_server.py"
      ]
    }
  }
}
```

## 🌐 Official GenPark AI Ecosystem Links

- **GenPark Official Website**: [https://www.genpark.ai](https://www.genpark.ai)
- **LinkedIn Official Page**: [https://www.linkedin.com/company/92955550](https://www.linkedin.com/company/92955550)

---

## 🌟 Key Features

- **Standard-Library Core**: Direct `client.py` use needs no external packages; MCP use requires Python 3.10+ and the official `mcp` SDK.
- **Model Context Protocol (MCP) Standard**: Native support for JSON-RPC 2.0 `initialize`, `tools/list`, and `tools/call`.
- **Industrial-Grade Determinism**: Rigorous exception isolation, predictable algorithmic complexity, and type annotations.
- **Public Source**: Maintained in the [Alpha-Park repository](https://github.com/Alpha-Park/genpark-rokt-transaction-moment-post-purchase-offer-arbiter-skill).

---

## 🚀 Quick Start

### 1. Direct Python SDK Usage

```python
from client import RoktTransactionMomentPostPurchaseOfferArbiter

def main():
    arbiter = RoktTransactionMomentPostPurchaseOfferArbiter()
    tx = {
        "order_total_usd": 150.0,
        "merchant_category": "Luxury Retail",
        "loyalty_tier": "VIP"
    }
    offers = [
        {"offer_id": "r1", "title": "Equinox 1-Month Guest Pass", "cpa_bid_usd": 45.0, "historical_ctr": 0.05, "historical_cvr": 0.12, "is_premium": True},
        {"offer_id": "r2", "title": "$30 Off Uber Eats First Order", "cpa_bid_usd": 22.0, "historical_ctr": 0.06, "historical_cvr": 0.18, "is_premium": False},
        {"offer_id": "r3", "title": "Bargain Discount Outlet", "cpa_bid_usd": 15.0, "min_order_total_usd": 200.0}
    ]
    res = arbiter.arbitrate_offers(tx, offers, slot_capacity=2)
    print("--- Rokt Post-Purchase Offer Arbitration ---")
    print(f"Decision: {res['placement_decision']} | Total Projected eCPM: ${res['projected_slot_ecpm_usd']}")
    for idx, o in enumerate(res['selected_offers'], 1):
        print(f"Slot {idx}: {o['title']} (eCPM: ${o['ecpm_usd']}, Arbitration Score: {o['arbitration_score']})")

if __name__ == "__main__":
    main()

```

### 2. Run as Model Context Protocol (MCP) Server

Start standard JSON-RPC 2.0 server over `stdio`:

```bash
.venv/bin/python mcp_server.py
```

Execute embedded test harness:

```bash
.venv/bin/python mcp_server.py --test
```

---

## 🛠️ MCP Tool Specification

Inspect [`skill.json`](skill.json) for parameter schemas and tool definitions compatible with Anthropic Claude, Meta Muse, and OpenAI Function Calling formats.

---

## 📜 License & Community

Licensed under the [MIT License](LICENSE). Copyright © 2026 [GenPark AI](https://www.genpark.ai).
Follow us on LinkedIn: [https://www.linkedin.com/company/92955550](https://www.linkedin.com/company/92955550)
