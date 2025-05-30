# components/prompt_builder.py

def build_prompt(user_query, context_chunks, assistant_name, company_name, skill, tone):
    tone_instruction = {
        ("HR", "Formal"): "You are a formal HR assistant who answers professionally and clearly.",
        ("HR", "Friendly"): "You are a friendly HR assistant who answers warmly and supportively.",
        ("IT", "Formal"): "You are a formal IT support assistant who provides concise and precise answers.",
        ("IT", "Friendly"): "You are a helpful and friendly IT assistant who speaks casually but informatively."
    }

    prompt_prefix = tone_instruction.get((skill, tone), "You are an AI assistant.")
    full_context = "\n".join(context_chunks)

    final_prompt = f"""
{prompt_prefix}

Company: {company_name}
Assistant Name: {assistant_name}

Use the following internal knowledge base to answer the query below. If unsure, say you don’t know.

Knowledge Base:
{full_context}

User Query:
{user_query}
"""

    return final_prompt
