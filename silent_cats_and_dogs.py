from pathlib import Path

file_names = ["cats.txt", "dos.txt"]

for file_name in file_names:
    try:
        path = Path(file_name)
        names = path.read_text()
    except FileNotFoundError:
        pass
        break
    for name in names.split(" "):
        print(name)