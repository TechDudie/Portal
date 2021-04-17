import wolframalpha
import os
client = wolframalpha.Client(os.getenv("WOLFRAM_ALPHA_TOKEN"))
def get(query):
  return client.query(query)["pod"][1]["subpod"]["img"]["@title"]