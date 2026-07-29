import sll 
from pathlib import Path
import os
import shutil


def get_parent_dir():
    script_dir = Path(__file__).resolve().parent
    return script_dir.parent
def create_dir_os(path):
    os.makedirs(path, exist_ok=True)
    return os.path.abspath(path)
def delete_dir(path):
    target = Path(path)
    if target.exists() and target.is_dir():
        shutil.rmtree(target)
        sll.log(f"Removed tree : {target}")
        return True
    sll.warn(f"Directory non existend or invalid : {target}")
    return False



sll.warn("Build Troposphere script... i hope everything goes well :/")

SOURCE_DIR = get_parent_dir()

sll.log(f"Using source directory -> {SOURCE_DIR}")

delete_dir(str(SOURCE_DIR)+"/output")

OUTPUT_DIR = create_dir_os(f"{SOURCE_DIR}/output")

sll.log(f"Creating output dump -> {OUTPUT_DIR}")




