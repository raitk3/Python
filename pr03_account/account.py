"""It's something."""
import time


def ask_name():
    """Ask name."""
    while True:
        name = input("What is your full name, dear fellow?").strip()
        is_title = name.istitle()
        is_spaced = " " in name
        is_alpha = name.replace(" ", "").replace("-", "").isalpha()
        if is_title and is_spaced and is_alpha:
            return name
        else:
            print("Sorry, try again.")


def progress_bar(process_name, seconds):
    """Progress bar n'shit."""
    chr_limit = 25
    cycle_time = seconds / 20
    is_long = len(process_name) > chr_limit - 2
    if is_long:
        process_name = process_name[:20] + "..."
    for i in range(21):
        print(f"\r[{'|' * i:-<20}] | Process: {process_name!r:.{chr_limit}} {0.05 * i:4.0%}", end="")
        time.sleep(cycle_time)
    print()


def print_ok():
    """That is fine..."""
    print("Account created.")


def main():
    """Main stuff..."""
    ask_name()
    progress_bar("Creating account", 5)
    print_ok()


if __name__ == "__main__":
    main()
