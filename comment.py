import os

f = open("./result.txt", "r", encoding="utf-8")
comment = f.read()
os.environ["comment"] = comment
f.close()
print(f"Set the comment done!\nComment:\n{comment}")
