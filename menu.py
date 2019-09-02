from working_with_existing import read_f_existing_projects
from working_with_new import add_new_project

def main_menu():
    user_choice = str(input("""CHOOSE OPTION:
1. Add new project
2. Select existing project
3. Exit
-> """))
    if user_choice == '1':
        add_new_project()
    elif user_choice == '2':
        read_f_existing_projects()
    elif user_choice == '3':
        exit()
    else:
        print("{}: '{}'. {}.".format("No option", user_choice, "Try again"))

