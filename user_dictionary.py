import json
from pathlib import Path

user_personal_information = {"Name": "Han", "Age": 21, "City": "Nottingham"}
path = Path("user_personal_information.txt")
path.write_text(json.dumps(user_personal_information))
new_path = Path("user_personal_information.txt")
print(json.loads(new_path.read_text()))