# Winston, the helpful command line AI

This is a little command line program that can be used as a command line assistant.


# Usage

* Set the OPENAI_API_KEY environment variable
* see help ./winston.py --help


For example, here how you can generate a requirements.txt for this program (warning: you have to fact check winstons version numbers 😜):
```shell
./winston.py --model text-ada-001   --question "generate a requirements.txt for this python program: $(cat winston.py)" > requirements.txt
```
