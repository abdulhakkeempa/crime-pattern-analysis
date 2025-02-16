from openai import OpenAI

from dotenv import load_dotenv

client = OpenAI()

def analyze_case_relationships(complaints):
  prompt = f"""
  Analyze the following crime complaints and identify any potential relationships between them. 
  Consider similarities in modus operandi, location, victim patterns, suspect behavior, and other relevant connections.

  Complaints:
  {complaints}

  Instructions:
  - Identify recurring patterns or connections between cases.
  - Highlight if the same suspect, group, or vehicle appears in multiple cases.
  - Mention any geographic or temporal correlations.
  - Provide a summary of key relationships and possible investigative leads.
  """
  completion = client.chat.completions.create(
      model="gpt-3.5-turbo",
      seed=12345,
      temperature=0,
      messages=[
          {"role": "system", "content": "You are an intelligent detective."},
          {"role": "user", "content": prompt}
      ]
  )

  return completion.choices[0].message.content
