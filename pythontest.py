#!/usr/bin/python3
import json 
import subprocess

# Open json file and parse its contents inside the data variable using json.load method
with open("disabled_users.json", "r") as json_file:
    data = json.load(json_file)      
# For loop to iterate the contents of data and delete the users with key 'uid' in dry-run mode
for d in data:
    subprocess.run(["ipa", "user-del", "--preserve", "--dry-run", d['uid'][0]]) 
print(d)