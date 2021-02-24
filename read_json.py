import json
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(dir_path,"horror_stories.json"), 'r', encoding="utf-8") as r:
    data = json.load(r)
    print(data)