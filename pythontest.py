import json 
import subprocess

with open("disabled_users.json", "r") as json_file:
    data = json.load(json_file)
        
for d in data:
    subprocess.run(["ipa", "user-del", "--preserve", "dryrun", d['uid'][0]])
    
print(d)







