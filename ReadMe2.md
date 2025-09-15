
# Git Commands Reference

A concise, organized reference of essential Git commands for daily development workflows.

## Table of contents
- [Setup](#setup)
- [Initialize & Clone](#initialize--clone)
- [Staging & Committing](#staging--committing)
- [History & Diff](#history--diff)
- [Branching & Merging](#branching--merging)
- [Remote Repositories](#remote-repositories)
- [Undoing Changes](#undoing-changes)
- [Stashing](#stashing)
- [Tagging](#tagging)
- [Resources](#resources)

## Setup
Configure your identity and view settings:
```bash
git config --global user.name "Your Name"
git config --global user.email "youremail@example.com"
git config --list
```

## Initialize & Clone
Create or copy repositories:
```bash
git init                 # Initialize a new repo
git clone <repository>   # Clone remote repo
```

## Staging & Committing
Prepare and record changes:
```bash
git add <file>           # Stage a specific file
git add .                # Stage all changes
git status               # Show working tree status

git commit -m "message"          # Commit staged changes
git commit -a -m "message"       # Stage tracked files and commit
```

## History & Diff
Inspect commits and changes:
```bash
git log                       # Full commit history
git log --oneline             # Compact history
git diff                      # Show unstaged changes
```

## Branching & Merging
Work on isolated lines of development:
```bash
git branch                    # List branches
git branch <branch-name>      # Create a new branch
git checkout <branch-name>    # Switch branch
git merge <branch-name>       # Merge into current branch
```

## Remote Repositories
Share and retrieve changes:
```bash
git remote add <name> <url>   # Add a remote
git fetch                     # Download objects/refs from remote
git pull                      # Fetch + merge from remote
git push                      # Push commits to remote
```

## Undoing Changes
Recover or discard changes:
```bash
git reset <file>              # Unstage file (keep changes)
git reset --hard <commit>     # Reset working tree to commit (destructive)
git revert <commit>           # Create a new commit that undoes a previous commit
```

## Stashing
Temporarily save uncommitted changes:
```bash
git stash                     # Stash changes
git stash pop                 # Apply and remove latest stash
git stash list                # List stashes
```

## Tagging
Mark important commits:
```bash
git tag <tag-name>                    # Create lightweight tag
git tag -a <tag-name> -m "message"    # Create annotated tag
```

## Resources
- Atlassian Git Tutorials: https://www.atlassian.com/git
- Pro Git book: https://git-scm.com/book/en/v2
- Git documentation: https://git-scm.com/docs
