import os
import sys

base = "https://$site/KeysHandler/"

site = "github.com"

base = base.replace("$site", site)

repos = [
    "Models",
    "Models.Test"
]

isInit = False

isUpdate = False

index = 0

for arg in sys.argv:
    if arg.lower() == "--site":
        if index != len(sys.argv):
            site = sys.argv[index + 1]
        else:
            print("No site provided")
            exit()
    if arg.lower() == "init":
        isInit = True
    if arg.lower() == "update":
        isUpdate = True

    index += 1

current_path = os.getcwd()
parrent_path = os.path.dirname(current_path)

print(">>> " + current_path)
print(">>> " + parrent_path)

print(">>> " + "os.chdir(parrent_path)")

os.chdir(parrent_path)

if isInit:
    for repo in repos:
        clone_cmd = "git clone " + base + repo + ".git"

        print(">>> " + clone_cmd)
        print(os.system(clone_cmd))

if isUpdate:
    for repo in repos:
        cd_cmd = "cd " + repo
        pull_cmd = "git pull"

        full_cmd = "{} && {}".format(cd_cmd, pull_cmd)

        print(">>> " + full_cmd)
        print(os.system(full_cmd))
