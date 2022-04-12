import os
import sys
# import bd

commit_message = input('commit message >> ')
if not commit_message:
    commit_message = 'aboba'

queue = (
    'git config credential.helper store',
    'git remote rename main origin',
    'git branch --unset-upstream',
    'git branch -m main',

    'cls',
    'git add --all',
    f'git commit . -m "{commit_message}"',
    'git push --set-upstream origin main'
)


for i in queue:
    os.system(i)

# os.system('git remote rename main origin')
