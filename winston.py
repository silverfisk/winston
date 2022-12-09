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
  parser.add_argument("--question",
                      type=str,
                      help="Your question",
                      required=True
                      )
  parser.add_argument("--model",
                      type=str,
                      help="Different models has different capabilities and price points.\n" + \
                              "Available models: text-davinci-003 text-curie-001 text-babbage-001 text-ada-001.",
                      default="text-davinci-003"
                      )
  args = parser.parse_args()


  res = answer(args.question)
  print(res)

def answer(question: str):
  '''
  Use OpenAI to give an intelligent response
  '''
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=question,
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )
  jres = json.loads(str(response))
  return jres['choices'][0]['text'].strip()


if __name__ == "__main__":
    main()
