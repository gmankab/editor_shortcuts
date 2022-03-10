import os
import sys

args = sys.argv.copy()
for i, arg in enumerate(args):
    args[i] = arg.replace('\\', '/')

file = sys.argv[1]
file_non_ext, ext = file.rsplit('.', 1)
file = f'"{file}"'
args_non_file = args[2:]
args = ' '.join(args[1:])

os.system('clear')

match ext:
    case 'py':
        if '--alt' in sys.argv:
            python = 'wpy'
        else:
            python = sys.executable

        os.system(
            f'{python} {args}'
        )

    case 'bat' | 'cmd':
        os.system(
            args
        )

    case 'pas':
        pascal_file = r'D:\dev_legacy\fpc\bin\i386-win32\ppcrossx64.exe'

        output = os.popen(
            f'{pascal_file} {file}'
        ).readlines()

        print(''.join(output))

        if not output:
            os.system(
                f'"{file_non_ext}.exe"'
            )
