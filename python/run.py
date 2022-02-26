import os
import sys

args = sys.argv.copy()
for i, arg in enumerate(args):
    args[i] = arg.replace('\\', '/')

path = sys.argv[1]
path_non_ext, ext = path.rsplit('.', 1)
path = f'"{path}"'
path_and_args = ' '.join(args[1:])
args = args[2:]

os.system('clear')

match ext:
    case 'py':
        os.system(
            f'cmd.exe /c py {path_and_args}'
        )

    case 'bat' | 'cmd':
        os.system(
            path_and_args
        )

    case 'pas':
        pascal_path = r'D:\dev_legacy\fpc\bin\i386-win32\ppcrossx64.exe'

        output = os.popen(
            f'{pascal_path} {path}'
        ).readlines()

        print(''.join(output))

        if not output:
            os.system(
                f'"{path_non_ext}.exe"'
            )
