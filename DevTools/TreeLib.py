import sys
import time
from concurrent.futures import ThreadPoolExecutor

SPINNER_FRAMES = ["⣾", "⣽", "⣻", "⢿", "⡿", "⣟", "⣯", "⣷"]


def draw_progress_bar(percent, width=10):
    filled = int(width * (percent / 100))
    if filled < width:
        bar = "=" * max(0, filled - 1) + ">" + " " * (width - filled)
    else:
        bar = "=" * width
    return f"[{bar}] {percent:3d}%"


def execute_task_with_spinner(label, task_fn, *args, indent=0, **kwargs):
    """
    Executes task_fn(*args, **kwargs) in a background thread while displaying an
    animated spinner or progress updates next to the label.
    """
    prefix = " " * indent + "|-> " if indent > 0 else ""
    full_prefix = f"{prefix}{label} "

    with ThreadPoolExecutor(max_workers=1) as executor:
        future = executor.submit(task_fn, *args, **kwargs)
        frame_idx = 0

        while not future.done():
            frame = SPINNER_FRAMES[frame_idx % len(SPINNER_FRAMES)]

            sys.stdout.write(f"\r\033[K{full_prefix}{frame}")
            sys.stdout.flush()

            frame_idx += 1
            time.sleep(0.08)

        # Retrieve result or raise exception if task failed
        result = future.result()

        # Clear line and print final status
        sys.stdout.write(f"\r\033[K{full_prefix}[DONE]\n")
        sys.stdout.flush()
        return result




def dummy_bundling():
    """Simulates bundling progress with progress bar updates."""
    for i in range(0, 101, 10):
        bar = draw_progress_bar(i)
        sys.stdout.write(f"\r|-> Part 1 - Bundling {bar}")
        sys.stdout.flush()
        time.sleep(0.15)
    return True


def dummy_file_check(filepath, is_hit=True):
    time.sleep(0.5)  # Simulate file checking / crawling work
    status = "[HIT]" if is_hit else "[MISS]"
    return f"{filepath} {status}"


def dummy_compile():
    time.sleep(1.2)  # Simulate compilation
    return True


# --- Tree Visualizer & Main Execution ---

if __name__ == "__main__":
    print("TEST OUT")

    # 1. Custom Progress Task
    dummy_bundling()
    print()  # newline after bundling finishes

    # 2. Directory Tree Crawl & Checks
    print("|- Troposphere")
    print("|         |- Troposphere_Lib")

    # Perform file checks
    hit_res = execute_task_with_spinner(
        "troposphere_lib.c",
        dummy_file_check,
        "troposphere_lib.c",
        True,
        indent=10,
    )

    miss_res = execute_task_with_spinner(
        "troposphere.version",
        dummy_file_check,
        "troposphere.version",
        False,
        indent=10,
    )

    # 3. Compile Step
    execute_task_with_spinner(
        "Part 6 - Compile Troposphere", dummy_compile, indent=10
    )
