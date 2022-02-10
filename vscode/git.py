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
    r'D:\apps\dev\Git\bin\git.exe remote rename main origin',
    r'D:\apps\dev\Git\bin\git.exe branch --unset-upstream',
    r'D:\apps\dev\Git\bin\git.exe branch -m main',

    'cls',
    r'D:\apps\dev\Git\bin\git.exe add .',
    r'D:\apps\dev\Git\bin\git.exe commit . -m aboba',
    r'D:\apps\dev\Git\bin\git.exe push --set-upstream origin main'
)


for i in queue:
    os.system(i)
