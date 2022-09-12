import os

filename=input("bot name")

os.mkdir(f"../{filename}")

with open(f"../{filename}/bot.py",'w') as newfile:
    default=open("default.pydbot","r",encoding="UTF-8").read()
    newfile.write(default)
