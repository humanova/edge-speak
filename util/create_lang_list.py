import json

voices = {}

with open("voices.txt", "r") as f:
    lines = f.readlines()

for i in range(0, len(lines), 3):
    name = lines[i].strip().split(": ")[1]
    gender = lines[i+1].strip().split(": ")[1]
    language = name.split("-")[0]

    if language not in voices:
        voices[language] = {"male": [], "female": []}

    if gender == "Male":
        voices[language]["male"].append(name)
    elif gender == "Female":
        voices[language]["female"].append(name)

# Create JSON object and write to file
json_obj = {"voices": voices}
with open("voices.json", "w") as f:
    json.dump(json_obj, f, indent=2)