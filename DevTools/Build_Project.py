from os.path import exists
import sys
import sll 
from pathlib import Path
import os
import shutil
import TreeLib
import tarfile
import BuildConfig
import git
from git import RemoteProgress
import urllib.request

SOURCE_DIR = ""
OUTPUT_DIR = ""
class GitProgressHandler(RemoteProgress):
    def __init__(self, callback_fn):
        super().__init__()
        self.callback_fn = callback_fn
    def update(self, op_code, cur_count, max_count=None, message=""):
        if max_count:
            percentage = (cur_count / max_count) * 100.0
            self.callback_fn(percentage)
def clone_repo(url: str, target_dir: str| Path, progress_callback=None):
    target = Path(target_dir).resolve()
    progress_handler = (GitProgressHandler(progress_callback) if progress_callback else None)

    git.Repo.clone_from(url,target_dir,progress=progress_handler)
    return target
def download_file(url: str, target_path: str | Path, progress_callback=None):
    """Downloads a file from a URL to target_path while reporting percentage

    progress to progress_callback.
    """
    target = Path(target_path).resolve()
    target.parent.mkdir(parents=True, exist_ok=True)

    # Open connection to read headers and file size
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})

    with urllib.request.urlopen(req) as response:
        # Get total size from headers (Content-Length)
        total_bytes = int(response.headers.get("Content-Length", 0))
        downloaded_bytes = 0
        chunk_size = 8192  # Download in 8 KB chunks

        with open(target, "wb") as f:
            while True:
                chunk = response.read(chunk_size)
                if not chunk:
                    break

                f.write(chunk)
                downloaded_bytes += len(chunk)

                # Send percentage to progress callback if total size is known
                if progress_callback and total_bytes > 0:
                    percent = (downloaded_bytes / total_bytes) * 100.0
                    progress_callback(min(percent, 100.0))

    # Force 100% completion update when finished
    if progress_callback:
        progress_callback(100.0)

    return target

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
def copy_file(source: str | Path, destination: str | Path) -> Path:
  
    src_path = Path(source)
    dst_path = Path(destination)

    if not src_path.is_file():
        raise FileNotFoundError(f"Source file does not exist: {src_path}")

    # Ensure parent destination directory exists
    if dst_path.is_dir() or not dst_path.suffix:
        dst_path.mkdir(parents=True, exist_ok=True)

    # shutil.copy2 preserves file metadata
    copied_path = shutil.copy2(src_path, dst_path)
    return Path(copied_path)
def copy_folder(source_dir: str | Path, destination_dir: str | Path, overwrite=True):
    src = Path(source_dir).resolve()
    dst = Path(destination_dir).resolve()

    if not src.exists():
        sll.warn(f"Source directory for {src} doesnt exist")
    if not src.is_dir():
        sll.warn(f"Source path is not a directory {src}")

    shutil.copytree(src,dst,dirs_exist_ok=overwrite)
    return dst
def dir_exists(dirpath: str | Path) -> bool:
    path = Path(dirpath)
    return path.is_dir()
def get_dir_size(folder_path: Path) -> int:
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





# Install Functions
def git_pull_jibo_wrappers():
    sll.warn("func git_pull_jibo_wrappers NEEDS to be implemented!")


def add_startup_command(command):
    sll.warn("func add_startup_command NEEDS to be implemented!")



def copy_init_dir():
    TreeLib.execute_task_with_spinner("Copying init directory", copy_folder, str(SOURCE_DIR) + "/include/root/etc/init.d", str(OUTPUT_DIR)+ "/root/etc/init.d", indent=5)



def git_pull_jpm():
    def showBar(percent: float):
        bar = TreeLib.draw_progress_bar(int(percent),20)
        sys.stdout.write(f"\r|-> Cloning Jibo Package Manager {bar}")
        sys.stdout.flush()
    
    clone_repo("https://github.com/Jibo-Revival-Group/Jibo-bins.git",str(OUTPUT_DIR)+"/git", progress_callback=showBar)













def bundle_dualroot():
    def showBar(percent: float):
        bar = TreeLib.draw_progress_bar(int(percent),20)
        sys.stdout.write(f"\r|-> Part 1 - Bundling filesystem {bar}")
        sys.stdout.flush()

    if file_exists(str(SOURCE_DIR)+"/include/dualrootfs.tar.gz"):
        bar = TreeLib.draw_progress_bar(100,20)
        sys.stdout.write(f"\r|-> Part 1 - Bundling filesystem {bar} -> Using pre bundled tarball")
        sys.stdout.flush()
        TreeLib.execute_task_with_spinner(
    "Copy pre bundled fs",
    copy_file,  # Function reference without ()
    f"{SOURCE_DIR}/include/dualrootfs.tar.gz",  # 1st argument
    f"{OUTPUT_DIR}/dualrootfs.tar.gz",  # 2nd argument
    indent=5,
)
 



    else:
        dualroot = compress_directory(str(SOURCE_DIR)+"/include/dual_rootfs",str(OUTPUT_DIR)+"/dualrootfs.tar.gz",progress_callback=showBar)

    print("\n")

sll.warn("Build Troposphere script... i hope everything goes well :/")

SOURCE_DIR = get_parent_dir()

sll.log(f"Using source directory -> {SOURCE_DIR}")

delete_dir(str(SOURCE_DIR)+"/output")

OUTPUT_DIR = create_dir_os(f"{SOURCE_DIR}/output")

sll.log(f"Creating output dump -> {OUTPUT_DIR}")

sll.log("Checking required source tree")
bundle_dualroot()

sll.log("Continuing from BuildConfig ...")
copy_init_dir() if BuildConfig.Include_Init_dir else sll.warn("Config : Not Including init dir replacement!")
git_pull_jpm() if BuildConfig.Include_JiboPackageManager else sll.warn("Config : Not Including Jibo Package Manager!")
git_pull_jibo_wrappers() if BuildConfig.Include_JiboBinaryWrappers else sll.warn("Config : Not Including Jibo Binary Wrappers!")



