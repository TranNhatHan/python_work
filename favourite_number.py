from pathlib import Path
import json

while True:
    try:        
        favourite_number = int(input("What is your favourite number? "))
        break
    except ValueError:
        print("Enter numbers!")

path = Path("favourite_number.json")
path.write_text(json.dumps(favourite_number))
