import os
from pathlib import Path

list_of_files = [
    ".streamlit/config.toml",
    "images/read.txt",
    "tools/__init__.py",
    "tools/browser_tools.py",
    "tools/calculate_tools.py",
    "tools/search_tools.py",
    ".env",
    "api_app.py",
    "arguments_cli.txt",
    "cli_app.py",
    "curl_request.txt",
    "streamlit_app.py",
    "trip_agent.py",
    "trip_task.py",
    "__init__.py"]
    
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir,filename = os.path.split(filepath)
    print(filedir,"-----",filename)
    
    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
    if ((not os.path.exists(filepath)) or (os.path.getsize(filepath)==0)):
        with open(filepath,'w') as f:
            print(filepath)
            pass
    else:
        print(f"file is already present at {filepath}")