from openai import OpenAI

# Create client
client = OpenAI(api_key="AIzaSyDNdYAayZ76fJZdo_4umbP-VAcgxegcge4")
def retriever_info(query):
    # Dummy retriever (replace with vector DB / FAISS later)
    return "Elon Musk is the CEO of Tesla and SpaceX."

def rag_query(query):
    retrieved_info = retriever_info(query)

    augmented_prompt = f"""
    Use the following retrieved context to answer the question.

    Context:
    {retrieved_info}

    Question:
    {query}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",  # fast & affordable
        messages=[
            {"role": "user", "content": augmented_prompt}
        ],
        max_tokens=150,
        temperature=0.7,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    return response.choices[0].message.content.strip()

# Example usage
query = "Tell me about Elon Musk"
response = rag_query(query)
print(response)