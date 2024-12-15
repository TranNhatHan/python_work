from pathlib import Path
import json

path = Path("favourite_number.json")
if not path.exists():
    while True:
        try:        
            favourite_number = int(input("What is your favourite number? "))
            path.write_text(json.dumps(favourite_number))
            break
        except ValueError:
            print("Enter numbers!")
else:
    print(json.loads(path.read_text()))
