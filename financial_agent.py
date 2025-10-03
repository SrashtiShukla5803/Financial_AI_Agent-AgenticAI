from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo


#web search agent
websearch_agent = Agent(
    name= "WebSearchAgent",
    role = "Search the web for relevant information to answer user queries.",
    model = Groq(id = "meta-llama/llama-4-maverick-17b-128e-instruct"),
    tools = [DuckDuckGo()],
    instructions = ["Always include sources in your responses."],
    show_tools_calls = True,
    markdown = True
)

# financial agent
finance_agent = Agent(
    name = "FinanceAgent",
    role = "Assist users with financial data and stock market information.",
    model = Groq(id = "meta-llama/llama-4-maverick-17b-128e-instruct"),
    tools = [
        YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True,
        company_news=True)],
    instructions = ["Use tables to display the data, Provide accurate and up-to-date financial information. Always cite your sources."],
    show_tools_calls = True,
    markdown = True
)

multi_ai_agent = Agent(
    team=[websearch_agent, finance_agent],
    model=Groq(id="meta-llama/llama-4-maverick-17b-128e-instruct"),
    tools=[DuckDuckGo(), YFinanceTools(stock_price=True, analyst_recommendations=True,
    stock_fundamentals=True, company_news=True)],  
    instructions=[
    "Use the FinanceAgent (YFinanceTools) only for stock-related data. Always use the `symbol` parameter with stock tickers (e.g., 'AAPL' for Apple).",
    "Use the WebSearchAgent (DuckDuckGo) only for general company news or background info.",
    "Do not call tools with extra or unknown parameters.",
    "Use tables for financial data and cite sources."
],
    show_tool_calls=True,
    markdown=True
)

#to inititate a conversation with the multi-agent system
# at the bottom of financial_agent.py
if __name__ == "__main__":
    multi_ai_agent.print_response(
        "What is the current stock price of Apple Inc. and any recent news about the company?",
        stream=True
    )

