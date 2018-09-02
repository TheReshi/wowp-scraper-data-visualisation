import csv

class Character:

    def __init__(self, rank, name, race, clss, guild, faction, realm, region, zone, spec, sDPS):
        self.rank = rank
        self.name = name
        self.race = race
        self.clss = clss
        self.guild = guild
        self.faction = faction
        self.realm = realm
        self.region = region
        self.zone = zone
        self.spec = spec
        self.sDPS = sDPS

    def __str__(self):
        return ("{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}\n".format(self.rank, self.name, self.race, self.clss, self.guild, self.faction, self.realm, self.region, self.zone, self.spec, self.sDPS))

    def get_array(self):
        return [self.rank, self.name, self.race, self.clss, self.guild, self.faction, self.realm, self.region, self.zone, self.spec, self.sDPS]