# Fork the repository on GitHub first, then clone your fork:
git clone <YOUR_FORK_URL>
cd <REPOSITORY_FOLDER>

# Create feature branch
git checkout -b feature-update

# Edit files, then stage and commit
git add .
git commit -m "Update documentation"

# Push branch to your fork
git push -u origin feature-update

# On GitHub: open Pull Request from your fork's feature-update branch
# to the original repository's main branch.
