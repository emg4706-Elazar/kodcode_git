import json




class WeaponsManager:

    def __init__(self):
        self.weapons = []
        self.load_from_json()



    def save_to_json(self):
        with open("weapons.json", "w", encoding="utf-8") as f:
            json.dump(self.weapons, f)


    def load_from_json(self):
        with open("weapons.json", "r", encoding="utf-8") as f:
            weapons = json.load(f)
            for w in weapons:
                self.weapons.append(w)
        return





wm = WeaponsManager()
wm.save_to_json()
for w in wm.weapons:
    print(w)
