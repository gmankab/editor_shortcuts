There are small python scripts for running files
and uploading it to github by hotkeys.

## Supported languages:
- python
- pascal


## How to use?

1. Download [multi-command extension](https://marketplace.visualstudio.com/items?itemName=ryuta46.multi-command)
1. Download [vscode/run.py](https://github.com/gmankab/vscode_hotkeys/blob/main/vscode/run.py)
and [git.py](https://github.com/gmankab/vscode_hotkeys/blob/main/git.py)
1. Open your keybindings.json and paste to it
[my keybindings](https://github.com/gmankab/vscode_hotkeys/blob/main/keybindings.json)
1. replace `"D:\\dev\\python-3.10.1\\python.exe"`
with your python path
1. replace `"E:\\projects\\git.py"`
with your  git.py path
1. replace `"E:\\projects\\vscode/run.py"`
with your  vscode/run.py path
1. make sure your `git remote` name is `main` and
your `git branch` name is `main`.
1. Use <kbd>F3</kbd> to run file
1. Use <kbd>Ctrl-G</kbd> to git commit and push
1. Reloading vscode not necessary,
but if nothing works, try it.
Also check conflicts between hotkeys.

