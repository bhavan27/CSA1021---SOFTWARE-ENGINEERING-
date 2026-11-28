#!/usr/bin/env bash
set -e
mkdir -p git-merge-conflict-demo
cd git-merge-conflict-demo
git init
git config user.name "Student"
git config user.email "student@example.com"
echo "Project status: Initial" > status.txt
git add status.txt
git commit -m "Initial commit"
git branch feature
git switch feature
echo "Project status: Feature branch update" > status.txt
git add status.txt
git commit -m "Update status on feature branch"
git switch main
echo "Project status: Main branch update" > status.txt
git add status.txt
git commit -m "Update status on main branch"
git merge feature || true
echo "Resolve status.txt manually by replacing conflict markers with:"
echo "Project status: Main and feature updates combined"
echo "Then run:"
echo "git add status.txt"
echo 'git commit -m "Resolve merge conflict"'
