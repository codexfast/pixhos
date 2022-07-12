import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "includes": ["tkinter"], "include_files":["src/gui.py"]}

# GUI applications require a different base on Windows (the default is for
# a console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Pixhos",
    version="0.1",
    description="Gerador de Pix dinâmico",
    options={"build_exe": build_exe_options},
    executables=[Executable("src/main.py", base=base)]
)