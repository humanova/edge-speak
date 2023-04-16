import json

f = open("util/voices.json", "r")
data = json.load(f)

def find_suitable_voice(detected_language_code, gender):
    if detected_language_code not in data["voices"]:
        return None
    
    return data["voices"][detected_language_code][gender.lower()]