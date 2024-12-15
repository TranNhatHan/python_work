from pathlib import Path

file_names = ["cats.txt", "dos.txt"]

for file_name in file_names:
    try:
        path = Path(file_name)
        names = path.read_text()
    except FileNotFoundError:
        print(f"Can not find the the file {file_name}")
        break
    for name in names.split(" "):
        print(name)
