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
    r'git remote rename main origin',
    r'git branch --unset-upstream',
    r'git branch -m main',

    'cls',
    r'git add .',
    r'git commit . -m aboba',
    r'git push --set-upstream origin main'
)


for i in queue:
    os.system(i)
