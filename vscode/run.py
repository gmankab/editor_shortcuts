import sys
import os

file_path = sys.argv[1]

file_path_non_ext, ext = file_path.rsplit('.', 1)

os.system('cls')

match ext:
    case 'py':
        os.system(
            f'{sys.executable} {file_path}'
        )
    case 'pas':
        pascal_path = r'D:\dev\fpc\bin\i386-win32\ppcrossx64.exe'

        output = os.popen(
            f'{pascal_path} {file_path}'
        ).readlines()

        print(''.join(output))

        if not output:
            os.system(
                f'{file_path_non_ext}.exe'
            )
