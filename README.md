# Scripts

## Create Project

This script takes in the given command line argument and does the following:
* creates a new directory in the location specified in the project config.
    * `path/in/createProject_config/{command line argument}`
* initializes a git repository in this directory   
* adds a .gitignore and README
* creates initial commit
* creates a repository in github
    * a github access key with correctly configured permissions must be in config file
* adds this repo as a remote
* pushes to the repo

To use, first run `pip install -r requirements.txt`

## Daily logs

`eveninglog.py` and `morninglog.py` use `log_config.py` to generate a list of questions and daily routines. 
The logs are generated such that they appear sequentially in the directory specified in `log_config.py`.

`publish_logs.py` simply runs the commands to commit all logs and push to their remote repo. it assumes that the directory specified in `log_config.py` is a git repo with a remote set up.
