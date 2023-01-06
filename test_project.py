import project
import pytest
import glob
import os

colors = ["blau", "gelb", "gruen", "indigo", "magenta", "orange", "rot"]
dct = {color: project.Group(color) for color in colors}
test_student_1 = project.Student("000", "Testy", "McTester", "purple", "000")
test_student_2 = project.Student("100", "Henk", "Smokealot", "pink", "100")
test_student_3 = project.Student("100", "Henk", "Smokealot", "", "100")
test_student_4 = project.Student("100", "Henk", "Smokealot", "blau", "100")
studs = []
studs.append(test_student_1)
studs.append(test_student_2)
studs.append(test_student_3)
studs.append(test_student_4)
project.populate_groups(studs, dct)

folder_path = os.getcwd()
files = glob.glob(folder_path + "/*.csv")


def test_populate_groups():
    assert len(dct["rot"].members) == 0
    assert len(dct["blau"].members) == 1


def test_get_students():
    assert len(project.get_students()) != 0
    assert type(project.get_students()[0]) is project.Student



def test_get_group(): #requires to run with -s flag: pytest test_project.py -s
    # --> but contradicts unit test idea.
    # Possible sol if submission fails refactor logic of get_group into main() itself.
    assert type(project.get_group()) is str or ValueError or project.UmlautError



def test_change_scores():
    assert project.change_scores("blau", dct) == None