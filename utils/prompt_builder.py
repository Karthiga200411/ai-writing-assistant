def build_prompt(content_type, tone, topic, word_count):
    prompt=f"""
You are an expert Content Writer.
Write a {content_type} about the following topic:
{topic}.
Requirements:
- Tone: {tone}
- Approximate Word Counts: {word_count} words.
- Make it engaging and ready to use.
- Do not include any explanations. just the content itself.
Write the content now.

"""
    return prompt

# what the above function is doing.
"""
It takes 4 inputs and combines them into one string that tells 
the AI exactly what to write. That string is called a "prompt."
 The better your prompt, the better the output.
"""