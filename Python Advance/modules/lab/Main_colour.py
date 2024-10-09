from termcolor import colored, cprint
import sys

text = colored("Hello world!", "red", attrs=["bold", "underline"])

print(text)

cprint("Attention!", "red", attrs=["bold", "underline"], file=sys.stderr)
