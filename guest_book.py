from pathlib import Path

prompt = "What is your name? "
prompt += "(Enter 'q' to end the program): "

names = []
while True:
    name = input(prompt)
    if name == 'q':
        break
    names.append(name)

content = ""
for name in names:
    content += name + "\n"
path = Path("guest_book.txt")

path.write_text(content)