There are small python scripts for running files
and uploading it to github by hotkeys.

## Supported languages:
- python
- pascal


## How to use?

1. Download [multi-command extension](https://marketplace.visualstudio.com/items?itemName=ryuta46.multi-command)
0. Download [run.py](run.py)
and [git.py](../git.py)
0. Open your keybindings.json and paste to it my
[keybindings.json](keybindings.json)
0. replace `"D:\\dev\\python-3.10.1\\python.exe"`
with your python path
0. replace `"E:\\projects\\git.py"`
with your  git.py path
0. replace `"E:\\projects\\run.py"`
with your  run.py path
0. make sure your `git remote` name is `main` and
your `git branch` name is `main`.
0. Use <kbd>F3</kbd> to run file
0. Use <kbd>Ctrl-G</kbd> to git commit and push
0. Reloading vscode not necessary,
but if nothing works, try it.
Also check conflicts between hotkeys.

