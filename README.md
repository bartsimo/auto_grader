# auto_grader

#### Description:
Command line tool that assists in grading students homework submissions. Reads and outputs a csv file that documents student submissions.

#### Usage:
python points.py
Currently, it expects a csv file satisfying a specific format to be in the same folder as points.py.
A valid csv file is submitted alongside the python script.
After successful execution, the user is prompted on the command line for actions. The user can enter a group name to be graded as wel as a couple of grading decisions via entering either "y" or "n". The command line tool is actively used in the administration of a university class on econometrics.

#### Implementation:
The script is partly implemented in an **object oriented paradigm**. Two classes are defined: Group and Student. Both feature a couple of fields and custom print formats. A group contains student objects that are collected in a list as a field (of Group).

Class declarations are followed by a main function that calls helper functions:

**get_students()** searches the folder that the python script lies in for the latest csv file. This latest csv is read in. For each row except the header, a Student object is created and subsequently appended to a list. This list is returned.

**populate_groups()** takes this list of students and a dictionary as parameters. The dictionary consists of Group objects whose keys are the colors that denominate student groups. Student objects are matched to their fitting groups based on the respective fields of a Student and a Group.

**get_group** asks the user via input() which group she wants to grade. Sanity checks for user input are performed.

**change_scores()** takes the user input about which group is to be graded as input as well as a dictionary that in practice is initialized as a dict containing Groups (key = color) of Students. For each Student in the selected Group, the user is prompted whether she wants to alter her score. If a score is to be changed, the respetive field of the student is changed. Once all students in the group have been touched or not, the user is prompted whether she wants to change scores for another group. If the user wants to change scores in another group, the function recursively calls itself again. The function changes fields of objects it returns nothing.

**write_new_csv()** once the above functions were called and hence scores changed, an updated csv file is produced that adheres to the required format for this script. The script automatically reads in the latest csv when executed. For better readability in the OS file system, the current date is appended to the csv's name.

#### test_project.py:
Accompanying test file that
uses pytest for testing four helper functions of the script. The way the script currently works, a full automated unit test is not yet possible. For this to be implemented, the main function and subsequent helper functions should be modified to work more with command line args.

#### Modules used:
+ csv
+ glob
+ os
+ datetime
+ pytest

#### Content (Files and Folders)
+ project.py --> main script
+ test_project.py --> kind-of-unit test for the main script
+ requirements.txt --> required modules for external deployment
+ csv files --> for test purposes in the required format
+ README.md

##### Authors
bartsimo (Simon Bartke)

##### License
This project is licensed under CC BY-SA 2.0
