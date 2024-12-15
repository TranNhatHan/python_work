from pathlib import Path

try:
    path = Path("a_real_cinderella.txt")
    contents = path.read_text()
except FileNotFoundError:
    print("Can not find the file!")

print(contents.lower().count("the "))