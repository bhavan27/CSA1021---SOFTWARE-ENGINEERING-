EXPERIMENT 15: WORKING WITH GIT BRANCHES AND RESOLVING MERGE CONFLICTS

Aim:
To create and manage Git branches, merge changes, and resolve a merge conflict.

Requirements:
- Git installed
- Terminal / Git Bash
- A local repository

Procedure:
1. Create a folder and initialize a Git repository.
2. Create a sample file and commit it on the main branch.
3. Create a new branch named feature.
4. Edit the sample file on the feature branch and commit the change.
5. Switch back to main and modify the same line in the file.
6. Commit the change on main.
7. Merge the feature branch into main.
8. Observe the merge conflict markers in the file.
9. Edit the file and keep the required final content, removing conflict markers.
10. Stage the resolved file and commit the merge resolution.
11. Verify the commit history and final file content.

Commands:
See Code/branch_conflict_commands.txt or run Code/branch_conflict_demo.sh in a Git Bash terminal.

Expected Output:
A merge conflict is detected when the same line is modified differently in both branches. After manually resolving the conflict and committing, Git reports that the conflict has been resolved.

Result:
Git branches were created and merged successfully, and the merge conflict was resolved by editing the conflicted file and committing the resolution.
