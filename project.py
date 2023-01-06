import csv
import glob
import os
from datetime import datetime

"""
BOILERPLATE
"""
colors = ["blau", "gelb", "gruen", "indigo", "magenta", "orange", "rot"]
newline = "\n"
germans = ["ä", "ö", "ü", "ß"]

class Error(Exception):
    """Base class for other exceptions"""
    pass

class UmlautError(Error):
    """Raise when user inputs german umlaut"""

"""
END BOILERPLATE
"""


class Group:
    def __init__(self, color):
        self.color = color
        self.members = []

    def __str__(self) -> str:
        return f"Group {self.color} : {self.members}"


class Student:
    def __init__(self, id, last, first, group, points):
        self.id = id
        self.last = last
        self.first = first
        self.group = group
        self.points = points

    def __str__(self) -> str:
        return f"Student num.: {self.id}{newline}Nachname: {self.last}{newline}Vorname: {self.first}{newline}Gruppe: {self.group}{newline}Punkte: {self.points}{newline}"

    def __iter__(self):
        return iter([self.id, self.last, self.first, self.group, self.points])

dct = {color: Group(color) for color in colors}

# main             ###########################

def main():
    students = get_students()
    #print(students)
    populate_groups(students, dct)
    selector = get_group()
    change_scores(selector, dct)
    write_new_csv()

#############################################


# Helper functions ##########################

def populate_groups(lst, dictionary):
    for i in colors:
        for j in lst:
            if j.group == dictionary[i].color:
                dictionary[i].members.append(j)

def get_students():
    container = []
    folder_path = os.getcwd()
    files = glob.glob(folder_path + "/*.csv")
    newest_file = max(files, key=os.path.getctime)
    #with open('gitlab_students.csv', 'r') as f: # base case ohne automatische Suche des aktuellsten csvs
    with open(newest_file, 'r') as f:
        reader = csv.reader(f, delimiter = ";")
        reader.__next__()
        for row in reader:
            container.append(Student(*row))

    return container

def get_group():
    while True:
        try:
            sel = input("Welche Gruppe soll bewertet werden: ").lower()

            if not sel:
                raise ValueError

            if not sel.isalpha():
                raise ValueError

            for s in sel.split():
                for t in s:
                    for w in germans:
                        if w == t:
                            raise UmlautError

            return sel

        except ValueError:
            print("Du hast gar nichts eingegeben! Bitte gib einen String ohne Umlaute ein und Zahlen.")

        except UmlautError:
            print("Keine Umlaute! ü = ue, etc.")

def change_scores(group_selector, dictionary):
    for i in range(len(dictionary[group_selector].members)):
        print(dictionary[group_selector].members[i])
        while True:
            change = input(f"Möchtest du die Anzahl der Abgaben von {dictionary[group_selector].members[i].first} {dictionary[group_selector].members[i].last} ändern? [y für Ja und n für Nein]").lower()
            if not ((change == "y") ^ (change == "n")):
                continue
            else:
                break
        if change == "y":
            while True:
                increment = input(f"Hat {dictionary[group_selector].members[i].first} {dictionary[group_selector].members[i].last} die Abgabe bestanden? [y für Ja und n für Nein]").lower()
                if not ((increment == "y") ^ (increment == "n")):
                    continue
                else:
                    break
            if increment == "y":
                to_add = int(dictionary[group_selector].members[i].points)
                to_add += 1
                dictionary[group_selector].members[i].points = str(to_add)
                print(dictionary[group_selector].members[i])

        if i < len(dictionary[group_selector].members) - 1:
            print("########## NÄCHSTER STUDENT IN DIESER GRUPPE ################")
        else:
            while True:
                weiter = input(f"Möchtest du die Anzahl der Abgaben in einer weiteren Gruppe ändern? [y für Ja und n für Nein]").lower()
                if not ((weiter == "y") ^ (weiter == "n")):
                    continue
                else:
                    break

            if weiter == "y":
                auswahl = get_group()
                change_scores(auswahl, dct)


def write_new_csv():
    filename = "gitlab_students_" + datetime.now().strftime("%Y-%m-%d-%H-%M.csv")
    with open(filename, "w", newline='') as stream:
        fieldnames = ['id', 'last', 'first', 'group', 'points']
        writer = csv.DictWriter(stream, fieldnames=fieldnames, dialect='excel', delimiter=';')
        writer.writeheader()
        for i in colors:
            for j in range(len(dct[i].members)):
                writer.writerow(vars(dct[i].members[j]))

#######################################################################################


if __name__ == "__main__":
    main()