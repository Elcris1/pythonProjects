# From this https://github.com/Elcris1/pythonProjects.git
# To this: https://<github-token>@github.com/<user-name>/<your-git-code>.git

# Template for the url
URL_TEMPLATE = "https://<github-token>@github.com/<user-name>/<your-git-code>"

# Getting token and Repo
token = input("Enter your git token: ")
repo = input("Enter your git repo to use your token with: ")

# splitting the repo
splitRepo = repo.split("/")

# Getting username and code from the repo
userName = splitRepo[3]
gitCode = splitRepo[4]

# Replacing the values on the template
template = URL_TEMPLATE.replace("<github-token>", token)
template = template.replace("<user-name>", userName)
template = template.replace("<your-git-code>", gitCode)

# Printing the replaced value
print("Replaced Git: " + template)

# Asking if he needs any command
question = input("Witch command do you require: clone(1) or set origin(2)? ")

if question == "1" or question == "clone":
    print("git clone " + template)
elif question == "2" or question == "set" or question == "origin" or question == "set origin":
    print("git remote set-url origin " + template)
else:
    print("Invalid input, here's your git repo using token: " + template)
