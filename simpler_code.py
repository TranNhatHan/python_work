from pathlib import Path

path = Path("learning_python.txt")
contents = path.read_text()

for content in contents.splitlines():
    print(content)