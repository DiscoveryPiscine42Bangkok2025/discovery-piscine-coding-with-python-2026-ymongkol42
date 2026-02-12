#!/usr/bin/env python
prompt = "What you gotta say? : "
while True:
    mes = str(input(prompt))
    if mes == "STOP":
        break
    prompt = "I got that! Anything else? : "