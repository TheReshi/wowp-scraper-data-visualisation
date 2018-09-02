from character import Character
import csv, time

timestr = time.strftime("%Y-%m-%d")

def export_csv(self):
    with open(str(len(self)) + ".csv", mode = "w", newline = '') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter = ",")
        csv_writer.writerow(["Rank", "Name", "Race", "Class", "Guild", "Faction", "Realm", "Region", "Zone", "Spec", "SimDPS"])

        for char in self:
            csv_writer.writerow(char.get_array())