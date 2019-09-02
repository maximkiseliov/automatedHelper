import os
import shutil
from pathlib import Path
from zipfile import ZipFile
from working_with_new import add_new_script


def read_f_existing_projects():
    FILE_WITH_PROJECTS = Path("created_files\\projects.txt")
    
    if FILE_WITH_PROJECTS.exists():
        projects_as_dict = {}
        file_line = 1
        
        print("PROJECTS (type BACK to return to previous menu):")
        
        with FILE_WITH_PROJECTS.open() as file:
            for line in file:
                projects_as_dict[str(file_line)] = line.rstrip()
                print("{}. {}".format(file_line, line), end = '')
                file_line += 1
        user_choice = str(input("\n-> "))
        
        if user_choice in projects_as_dict.keys():
            work_with_existing(project_name = projects_as_dict[user_choice])
        elif user_choice.lower() == "back":
            pass
        else:
            print("{}: '{}'. {}.".format("No option", user_choice, "Try again"))

    else:
        print("Sorry, no projects are added yet\n")


def work_with_existing(project_name: str):
    USERPROFILE_PATH = os.path.join(os.environ['USERPROFILE'])
    DESKTOP_PATH = os.path.join(USERPROFILE_PATH, 'Desktop')

    project_data = {
        "project_name": project_name,
        "project_PATH": Path(os.path.join(DESKTOP_PATH, project_name)),
        "project_Stories_PATH": Path(os.path.join(DESKTOP_PATH, project_name, "Stories")),
        "project_all_scripts_PATH": Path(os.path.join(DESKTOP_PATH, project_name, "All Scripts")),
        "script_template": Path("script_templates\\basic_template\\NH_.xlsx")
        }

    while(True):
        user_choice = str(input("""CHOOSE OPTION:
1. Add new story
2. View existing stories
3. Collect scripts
4. Exit
-> 
"""))
        if user_choice == '1':
            add_new_script()
        elif user_choice == '2':
            view_existing_stories(project_data["project_Stories_PATH"])
        elif user_choice == '3':
            collect_all_scripts(project_data["project_name"], project_data["project_Stories_PATH"], project_data["project_all_scripts_PATH"])               
        elif user_choice == '4':
            exit()
        else:
            print("{}: '{}'. {}.".format("No option", user_choice, "Try again"))        
        

def view_existing_stories(project_Stories_PATH):
    project_PATH = Path(project_Stories_PATH)
    list_of_stories = [str(story) for story in project_PATH.iterdir() if story.is_dir()]
    
    if len(list_of_stories) != 0:
        for story in list_of_stories:
            print(story.split('\\')[-1])
    else:
        print("No stories")


def collect_all_scripts(name, stories_PATH, all_scripts_PATH):
    xlsx_files = [xlsx_file for xlsx_file in stories_PATH.rglob("*.xlsx")]
    
    if len(xlsx_files) != 0:
        for xlsx_file in xlsx_files:
            source = xlsx_file
            target = all_scripts_PATH / str(xlsx_file).split('\\')[-1]
            shutil.copyfile(source, target)
        print("TOTAL: {} scripts are successfully coppied to {}".format(len(xlsx_files), str(all_scripts_PATH)))

    else:
        print("No files to copy")

# TODO: CREATE ZIP METHOD WHEN HAVE TIME
def all_scripts_to_zip():
    pass

'''
        print("Create {}_all_scripts.zip file with {} scripts of {} project? (Y/N)".format(name, len(xlsx_files), name))
        user_choice = str(input("-> "))
        if user_choice.lower() == 'y':
            with ZipFile(str(all_scripts_PATH / name) + "_all_scripts.zip", "w") as zip_file:
                for script in all_scripts_PATH.rglob("*.xlsx"):
                    zip_file.write(script)   
'''
