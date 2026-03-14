import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from ddgs import DDGS

load_dotenv()

llm = ChatGroq(api_key=os.getenv("GROQ_API_KEY"), model_name="llama-3.3-70b-versatile")

def search_web(query):
    print("🔍 Searching the web...")
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=5))
            output = ""
            for r in results:
                output += f"Title: {r['title']}\nSummary: {r['body']}\n\n"
            return output if output else "No results found."
    except Exception as e:
        return f"Search failed: {e}"

def write_blog(topic, research):
    print("✍️ Writing blog post...")
    prompt = f"""
Write a detailed, engaging blog post about: {topic}

Use this research to make it accurate and current:
{research}

Structure it with:
- A catchy title
- Introduction
- 3-4 main sections with headings
- Conclusion
- Make it 400-600 words
"""
    response = llm.invoke(prompt)
    return response.content

def save_blog(filename, content):
    print("💾 Saving blog...")
    with open(f"{filename}.md", "w") as f:
        f.write(content)
    print(f"✅ Blog saved as {filename}.md")

# Main flow
print("\n✅ Blog Writer Agent ready!")
print("Give me a topic and I'll research, write and save a blog post!\n")

topic = input("Enter blog topic: ")

research = search_web(topic)
blog = write_blog(topic, research)
save_blog("blog_output", blog)

print("\n--- BLOG PREVIEW ---\n")
print(blog[:500])
print("\n... (full blog saved in blog_output.md)")