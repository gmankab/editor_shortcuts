import os
import subprocess


def silent_run():
    out, err = subprocess.Popen(
        i,
        shell=True,
        stdin=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        stdout=subprocess.PIPE,
        close_fds=True).communicate()


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
