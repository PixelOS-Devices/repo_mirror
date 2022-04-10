from repoList import repos
PAT = os.environ.get("TOKEN")

file = open("run.sh", "w+")
file.close()
file = open("run.sh", "a")
for repo in repos:
    # https://username:your_password@github.com/username/repo_name.git
    command = "rm -rf temp\ngit clone --mirror " + \
        repo[0] + " temp \ncd temp \ngit push -f https://geek0609:" + PAT + "@gitlab.com/PixelOS-Devices/" + \
        repo[1] + ".git --mirror\ncd .\n"
    print(command)
    file.write(command)
