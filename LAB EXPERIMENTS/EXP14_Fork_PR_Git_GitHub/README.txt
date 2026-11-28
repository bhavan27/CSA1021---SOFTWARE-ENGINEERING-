EXP 14 – Fork-and-Pull-Request Collaboration Workflow using Git and GitHub

Aim:
To collaborate on a GitHub repository by forking it, cloning the fork, creating a feature branch, making changes, pushing the branch, and submitting a Pull Request to the original repository.

Procedure:
1. Open the source GitHub repository and click Fork.
2. Clone your fork to the local system.
3. Create and switch to a feature branch.
4. Make the requested change in a file.
5. Stage and commit the changes.
6. Push the feature branch to your fork.
7. Open a Pull Request from your fork/branch to the original repository.
8. Review the changes and submit the Pull Request.

Commands:
git clone <your-fork-url>
cd <repository>
git checkout -b feature-update
# edit files
git add .
git commit -m "Update documentation"
git push -u origin feature-update

Sample Collaboration Scenario:
Update the project README by adding a contribution note. This demonstrates the fork-and-PR workflow without changing application code.

Result:
A fork was created, changes were committed to a feature branch, pushed to GitHub, and proposed to the original repository through a Pull Request.
