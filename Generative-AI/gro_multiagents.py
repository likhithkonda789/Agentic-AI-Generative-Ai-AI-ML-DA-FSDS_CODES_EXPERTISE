import sys
sys.stdout.reconfigure(encoding='utf-8')  # Fix Unicode error

import time
import random
import os
from dotenv import load_dotenv

from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools

# Load API key
load_dotenv()

# ✅ Company → Symbol mapping (FIXED)
def lookup_company_symbol(company: str) -> str:
    symbols = {
        "Infosys": "INFY",
        "Tesla": "TSLA",
        "Apple": "AAPL",
        "Microsoft": "MSFT",
        "Amazon": "AMZN",
        "Google": "GOOG"   # ✅ FIXED (important)
    }
    return symbols.get(company, "Unknown")


# ✅ Stock Agent
stock_agent = Agent(
    name="Stock Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            stock_fundamentals=True
        )
    ],
    instructions=[
        "Use only valid Yahoo Finance stock symbols like AAPL, GOOG, TSLA.",
        "Do not guess symbols. Always use correct symbols."
    ],
)

# ✅ Company Lookup Agent
company_lookup_agent = Agent(
    name="Company Lookup Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[lookup_company_symbol],
    instructions=[
        "Return correct stock symbol for given company name."
    ],
)

# ✅ Finance Team (Multi-agent)
finance_team = Agent(
    name="Finance Team",
    model=Groq(id="llama-3.3-70b-versatile"),
    team=[stock_agent, company_lookup_agent],
    instructions=[
        "First find correct stock symbols, then fetch stock data.",
        "Ensure valid symbols before calling tools."
    ],
)

# ✅ Retry Function (SAFE)
def run_with_retry(agent, query, retries=3, delay=5):
    for attempt in range(retries):
        try:
            response = agent.run(query)

            if response:
                return response

        except Exception as e:
            print(f"⚠️ Error: {e}")

        wait_time = random.uniform(delay, delay + 3)
        print(f"Retrying in {wait_time:.2f} seconds...")
        time.sleep(wait_time)

    print("❌ Max retries reached.")
    return None


# ✅ Run Query (use symbols explicitly for best results)
response = run_with_retry(
    finance_team,
    "Compare stock data for Apple (AAPL) and Google (GOOG)"
)

# ✅ Clean Output
if response:
    print("\n📊 Final Answer:\n")
    print(response.content)
else:
    print("Failed to get a response.")