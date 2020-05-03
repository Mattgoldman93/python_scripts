
import os
import sys
import createProject_config as config
from github import Github

path = config.projects_directory

def create():
    projectName = str(sys.argv[1])
    print("inside of create")
    os.makedirs(path  + projectName)
    os.chdir(path + projectName)
    os.system("git init")
    with open('README.md', 'w') as f:
        f.write("# " + projectName) 
    os.system("touch .gitignore")
    os.system("git add .")
    os.system("git commit -m \"initial commit \"")
    gh = Github(config.github_access_token)
    user = gh.get_user()
    user.create_repo(projectName)
    os.system("git remote add origin git@github.com:{}/{}.git".format(user.login, projectName))
    os.system("git push -u origin master")
if __name__ == "__main__":
    create()