#!/usr/bin/env python

import os
import logging
import openai
import json
from argparse import ArgumentParser


def main():
  openai.api_key = os.getenv("OPENAI_API_KEY")
  if not openai.api_key:
    logging.error("OPENAI_API_KEY environment variable is not set")
    sys.exit(-1)

  parser = ArgumentParser(description="I am Winston, your very own AI!")
  parser.add_argument("--input",
                      type=str,
                      help="Your embedded input",
                      required=True
                      )
  parser.add_argument("--model",
                      type=str,
                      help="Different models has different capabilities and price points.\n" + \
                              "Available models: text-embedding-ada-002 text-davinci-003 text-curie-001 text-babbage-001 text-ada-001.",
                      default="text-embedding-ada-002"
                      )
  parser.add_argument("--user",
                      type=str,
                      help="A unique identifier representing your end-user.",
                      default="winston" + "-"+ os.getenv("USERNAME") + "-" + os.getenv("TERM")
                      )
  args = parser.parse_args()


  res = embeddings(args.input, args.model, args.user)
  print(res)

def embeddings(input: str, model: str, user: str):
  '''
  Use OpenAI to get a vector representation of a given input that can be consumed by machine lerning models and algorithms.
  '''
  response = openai.Embedding.create(
    model=model,
    input=input,
    user=user
  )
  return response['data'][0]['embedding']

if __name__ == "__main__":
    main()
