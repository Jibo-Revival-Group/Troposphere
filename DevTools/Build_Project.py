import sys
import sll 
from pathlib import Path
import os
import shutil
import TreeLib
import tarfile



SOURCE_DIR = ""
OUTPUT_DIR = ""

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
def file_exists(filepath: str | Path) -> bool:
    path = Path(filepath)
    return path.is_file()

def dir_exists(dirpath: str | Path) -> bool:
    path = Path(dirpath)
    return path.is_dir()
def get_dir_size(folder_path: Path) -> int:
    """Calculates the total size of all files inside a directory (in bytes)."""
    total_size = 0
    for file in folder_path.rglob("*"):
        if file.is_file():
            total_size += file.stat().st_size
    return total_size

def compress_directory(
    source_dir: str | Path,
    output_tar: str | Path,
    progress_callback=None,
):
    """
    Compresses source_dir into a .tar.gz archive at output_tar.
    
    :param source_dir: The directory to compress.
    :param output_tar: Output filename ending in .tar.gz.
    :param progress_callback: A function taking a float (0.0 to 100.0).
    """
    source_path = Path(source_dir).resolve()
    output_path = Path(output_tar).resolve()

    if not source_path.is_dir():
        raise ValueError(f"Source directory '{source_path}' does not exist.")

    # Calculate total bytes for progress tracking
    total_bytes = get_dir_size(source_path)
    processed_bytes = 0

    # Ensure parent output dir exists
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with tarfile.open(output_path, "w:gz") as tar:
        for file_path in source_path.rglob("*"):
            # Compute relative path inside the archive
            arcname = file_path.relative_to(source_path)

            if file_path.is_file():
                tar.add(file_path, arcname=arcname, recursive=False)
                processed_bytes += file_path.stat().st_size

                # Trigger callback with percentage progress
                if progress_callback and total_bytes > 0:
                    percent = (processed_bytes / total_bytes) * 100
                    progress_callback(min(percent, 100.0))
            elif file_path.is_dir():
                tar.add(file_path, arcname=arcname, recursive=False)

    # Final explicit 100% notification
    if progress_callback:
        progress_callback(100.0)

    return output_path

def bundle_dualroot():
    def showBar(percent: float):
        bar = TreeLib.draw_progress_bar(int(percent),20)
        sys.stdout.write(f"\r|-> Part 1 - Bundling filesystem {bar}")
        sys.stdout.flush()

    if file_exists(str(SOURCE_DIR)+"/include/dualrootfs.tar.gz"):
        bar = TreeLib.draw_progress_bar(100,20)
        sys.stdout.write(f"\r|-> Part 1 - Bundling filesystem {bar} -> Using pre bundled tarball")
        sys.stdout.flush()

    else:
        dualroot = compress_directory(str(SOURCE_DIR)+"/include/dual_rootfs",str(OUTPUT_DIR)+"dualrootfs.tar.gz",progress_callback=showBar)



sll.warn("Build Troposphere script... i hope everything goes well :/")

SOURCE_DIR = get_parent_dir()

sll.log(f"Using source directory -> {SOURCE_DIR}")

delete_dir(str(SOURCE_DIR)+"/output")

OUTPUT_DIR = create_dir_os(f"{SOURCE_DIR}/output")

sll.log(f"Creating output dump -> {OUTPUT_DIR}")

sll.log("Checking required source tree")
bundle_dualroot()







