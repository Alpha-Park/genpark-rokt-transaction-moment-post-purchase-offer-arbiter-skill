#!/usr/bin/env python3
import json
import sys
from client import RoktTransactionMomentPostPurchaseOfferArbiter

from typing import Any, Dict, List, Optional

try:
    from mcp.server.fastmcp import FastMCP
except ImportError as exc:
    raise SystemExit("MCP requires the mcp package. Run: python -m pip install -r requirements.txt") from exc

mcp = FastMCP('genpark-rokt-transaction-moment-post-purchase-offer-arbiter-skill')

@mcp.tool()
def arbitrate_offers(transaction_context: Optional[Dict[str, Any]] = None, candidate_offers: Optional[List[Dict[str, Any]]] = None, slot_capacity: int = 2) -> str:
    """Rank supplied post-purchase offers for the available slots."""
    return json.dumps(RoktTransactionMomentPostPurchaseOfferArbiter().arbitrate_offers(transaction_context if transaction_context is not None else {}, candidate_offers if candidate_offers is not None else [], slot_capacity))

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        arbiter = RoktTransactionMomentPostPurchaseOfferArbiter()
        tx = {"order_total_usd": 125.0, "merchant_category": "Apparel", "loyalty_tier": "VIP"}
        offers = [
            {"offer_id": "rokt_1", "title": "$25 Off HelloFresh", "cpa_bid_usd": 20.0, "historical_ctr": 0.04, "historical_cvr": 0.15, "is_premium": False},
            {"offer_id": "rokt_2", "title": "Complimentary WSJ 3-Month Access", "cpa_bid_usd": 35.0, "historical_ctr": 0.03, "historical_cvr": 0.12, "is_premium": True},
            {"offer_id": "rokt_3", "title": "Casino Spin Bonus", "cpa_bid_usd": 50.0, "excluded_merchant_categories": ["Apparel"]}
        ]
        res = arbiter.arbitrate_offers(tx, offers, slot_capacity=2)
        assert len(res["selected_offers"]) == 2
        assert res["placement_decision"] == "RENDER_TRANSACTION_MOMENT_WIDGET"
        print(f"[TEST PASS] Rokt Offer Arbiter Passed! Projected eCPM: ${res['projected_slot_ecpm_usd']}")
        sys.exit(0)

    mcp.run(transport="stdio")

if __name__ == "__main__":
    main()
