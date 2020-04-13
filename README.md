# Scripts

## Daily logs

`eveninglog.py` and `morninglog.py` use `log_config.py` to generate a list of questions and daily routines. 
The logs are generated such that they appear sequentially in the directory specified in `log_config.py`.

`publish_logs.py` simply runs the commands to commit all logs and push to their remote repo. it assumes that the directory specified in `log_config.py` is a git repo with a remote set up.
