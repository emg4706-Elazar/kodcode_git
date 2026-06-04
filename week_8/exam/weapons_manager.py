import json




class WeaponsManager:

    def __init__(self):
        self.weapons = []
        self.load_from_json()


    def create_weapon(self, weapon):
        self.weapons.append(weapon)
        self.save_to_json()
        return


    def update_weapon(self, weapon):
        all_weapons = self.weapons[:]
        for w in all_weapons:
            if w["id"] == weapon["id"]:
                i = all_weapons.index(w)
                del self.weapons[i]
                self.create_weapon(weapon)
                self.save_to_json()
        return


    def delete_weapon(self, id):
        all_weapons = self.weapons[:]
        for w in all_weapons:
            if w["id"] == id:
                i = all_weapons.index(w)
                del self.weapons[i]
                self.save_to_json()
        return


    def get_weapons(self):
        return self.weapons

    def get_new_id(self):
        new_id = 0
        all_id_s = [ w["id"] for w in self.weapons]
        if all_id_s:
            new_id = max(all_id_s) + 1
        return new_id

    def get_one_weapon(self,id: int):
        all_weapon = self.weapons
        for w in all_weapon:
            if w["id"] == id:
                return w
        return None


    def get_by_cond(self, condition):
        all_weapons = self.weapons
        sorted_weapons = []
        for w in all_weapons:
            if w["condition"] == condition:
                sorted_weapons.append(w)
        return sorted_weapons



    def save_to_json(self):
        with open("weapons.json", "w", encoding="utf-8") as f:
            json.dump(self.weapons, f)


    def load_from_json(self):
        with open("weapons.json", "r", encoding="utf-8") as f:
            weapons = json.load(f)
            for w in weapons:
                self.weapons.append(w)
        return






if __name__ == "__main__":

    wm = WeaponsManager()
    wm.save_to_json()
    print(wm.get_new_id())
