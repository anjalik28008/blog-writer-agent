# Blog Writer Agent

An AI agent that automatically researches a topic and writes a full blog post.

## How it works
1. Takes a topic as input
2. Searches the web using DuckDuckGo for latest info
3. Writes a structured 400-600 word blog post using Groq's Llama 3
4. Saves it as a markdown file

## Tech Stack
- Python
- LangChain
- Groq API (Llama 3)
- DuckDuckGo Search

## Setup
1. Clone the repo
2. Install: `pip install langchain langchain-groq ddgs python-dotenv`
3. Add Groq API key in `.env`
4. Run: `python blog_writer.py`
