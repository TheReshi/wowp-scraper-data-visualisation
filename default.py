RACES = {"human", "dwarf", "night elf", "gnome", "draenei", "worgen", "pandaren", "orc", "undead", "tauren", "troll", "blood elf", "goblin", "void elf",
        "lightforged draenei", "dark iron dwarf", "kul tiran human", "nightborne", "highmountain tauren", "zandalari troll", "mag'har orc"}
CLASSES = {"warrior", "paladin", "hunter", "rogue", "priest", "death knight", "shaman", "mage", "warlock", "monk", "druid", "demon hunter"}
FACTIONS = {"horde", "alliance"}
HORDE_RACES = {"orc", "undead", "tauren", "troll", "blood elf", "goblin", "nightborne", "highmountain tauren", "zandalari troll", "mag'har orc"}
ALLIANCE_RACES = {"human", "dwarf", "night elf", "gnome", "draenei", "worgen", "void elf", "lightforged draenei", "dark iron dwarf", "kul tiran human"}

def get_race_faction(self):
        for rc in HORDE_RACES:
                if rc in self.lower():
                        return rc.title(), "Horde"
        for rc in ALLIANCE_RACES:
                if rc in self.lower():
                        return rc.title(), "Alliance"
        if "pandaren" in self.lower():
                return "Pandaren", ""
        return "", ""

def get_class(self):
        for clss in CLASSES:
                if clss in self.lower():
                        return clss.title()
        return None

def get_faction(self):
        for fac in FACTIONS:
                if fac in self.lower():
                        return fac.title()
        return ""
