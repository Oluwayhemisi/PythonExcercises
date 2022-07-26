import pathlib
from pathlib import Path

home = Path.home() / "file.txt"
home.touch()

print(home)
print(home.exists())
print(home.stem)
print(home.suffix)
print(home.is_file())

path = Path(r"photos/image.jpg")

new_dir = path.home() / "new directory"

print(new_dir.exists())
print(new_dir.is_dir())

nested_dir = new_dir / "folder_a" / "folder_b"
print(nested_dir)

file_path = new_dir / "file1.txt"
print(file_path)

new_dir = path.home() / "new directory"
for path in new_dir.iterdir():
    new_dir.iterdir()
    print(path)
    list(new_dir.iterdir())

for path in new_dir.glob("*.txt"):
    print(path)

paths =[new_dir/"program1.py",

       new_dir/"program2.py",
       new_dir/"folder_a"/"program3.py",
       # new_dir/"folder_a"/"folder_b"/"image1.jpg",
       # new_dir/"folder_a"/"folder_b"/"image2.jpg",
           ]
for path in paths:
    path.touch()