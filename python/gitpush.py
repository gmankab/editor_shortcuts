import os
import sys
# print()
# import bd


queue = (
    'git remote rename main origin',
    'git branch --unset-upstream',
    'git branch -m main',

    'cls',
    'git add .',
    'git commit . -m aboba',
    'git push --set-upstream origin main'
)


for i in queue:
    os.system(i)

# os.system('git remote rename main origin')
