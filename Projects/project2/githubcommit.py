
import os
import subprocess
import time  # Import the 'time' module

# GitHub repository information
repository_url = "https://github.com/jivanandham/Applications-of-Networks-main"
branch_name = "main"  # Replace with your branch name (e.g., "master" or "main")

# Directory where your code is located
code_directory = r"C:\Users\HP\Desktop\Applications-of-Networks-main"


# Function to commit and push changes
def commit_and_push():
    os.chdir(code_directory)

    # Add all changes
    subprocess.call(["git", "add", "."])

    # Commit with a timestamp
    commit_message = "Automatic commit at " + time.strftime("%Y-%m-%d %H:%M:%S")
    subprocess.call(["git", "commit", "-m", commit_message])

    # Push the changes to your GitHub repository
    subprocess.call(["git", "push", repository_url, branch_name])


if __name__ == "__main__":
    while True:
        commit_and_push()
        time.sleep(3600)  # Sleep for 1 hour (3600 seconds)
