# Repositories cloner & puller by SPLIT VICE.
# Copyright MIT - SPLIT VICE 2021.
# Version 1.1.2
# Script's dedicated webpage: https://splitvice.github.io/technology/python/repos-cloner-puller/

# ========================================================================
# EDITABLE USER CONFIGURATION
# ========================================================================

# Remote URL where repositories are. Example: https://www.github.com/
git_remote = "https://github.com/"

# Username to clone repositories from
# Concatenation with git_remote variable should look like https://www.github.com/vice/
username = "vice/"

# List of repositories to clone and pull
# Array example: repositories_array = ["app1", "app2"]
# Concatenation with git_remote and username variables should look like https://www.github.com/vice/app1
repositories_array = ["app1", "app2"]

# List of private repositories to clone and pull
private_repositories_array = ["privateApp1", "privateApp2"]

# Select the type of repositories script will work on
# Boolean => True of False
clone_public_repositories = True
clone_private_repositories = False

# ========================================================================
# SCRIPT CODE
# ========================================================================

# ------------------------------------------------------------------------
# HELPER FUNCTIONS
# ------------------------------------------------------------------------

import subprocess

# Does CMD processes
def cmd(command):
    try:
        subprocess.call(command, shell = True)
    except:
        print("Error at cmd " + command)

# ------------------------------------------------------------------------
# PUBLIC REPOSITORIES FUNCTIONS
# ------------------------------------------------------------------------

# Clones repositories listed on repos_array
def clone():
    for repo in repositories_array:
        print("===== Attempting to clone-> " + git_remote + username + repo)
        cmd("git clone " + git_remote + username + repo)

# Executes git pull onto existing repositories
def pull():
    for repo in repositories_array:
        print("===== Attempting to pull-> " + repo)
        cmd("cd " + repo + " && " + "git pull")

# ------------------------------------------------------------------------
# PRIVATE REPOSITORIES FUNCTIONS
# ------------------------------------------------------------------------

# Clones private repositories on private_repos_array
def clone_private():
    for repo in private_repositories_array:
        print("===== Attempting to clone private repository-> " + git_remote + username + repo)
        cmd("git clone " + git_remote + username + repo)

# Executes git pull onto existing private repositories
def pull_private():
    for repo in private_repositories_array:
        print("===== Attempting to pull private repository-> " + repo)
        cmd("cd " + repo + " && " + "git pull")


# ========================================================================
# MAIN
# ========================================================================

if (clone_public_repositories or clone_private_repositories):
    if (clone_public_repositories):
        print("=== Public repositories actions start ===")
        clone()
        pull()
        print("=== Public repositories actions end ===")

    if (clone_private_repositories):
        print("=== Private repositories actions start ===")
        clone_private()
        pull_private()
        print("=== Private repositories actions end ===")
else:
    print("No repositories actions set. Check your configuration")


end = input("=== Script finished. Press any key to close. ===")
