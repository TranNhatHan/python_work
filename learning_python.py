from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text()
print(contents)
for content in contents.split("\n"):
    print(content)