import sys
import os
from datetime import datetime


def main() -> None:
    args = sys.argv[1:]

    if not args:
        print("Usage: python create_file.py [-d dir1 dir2 ...] [-f filename]")
        sys.exit(1)

    dir_parts = []
    filename = None

    i = 0
    while i < len(args):
        if args[i] == "-d":
            i += 1
            while i < len(args) and not args[i].startswith("-"):
                dir_parts.append(args[i])
                i += 1
        elif args[i] == "-f":
            i += 1
            if i < len(args):
                filename = args[i]
                i += 1
            else:
                print("Error: -f flag requires a filename")
                sys.exit(1)
        else:
            print(f"Unknown argument: {args[i]}")
            sys.exit(1)

    # --- Tworzenie katalogów ---
    target_dir = os.path.join(*dir_parts) if dir_parts else "."
    os.makedirs(target_dir, exist_ok=True)

    # --- Obsługa tylko katalogu bez pliku ---
    if not filename:
        print(f"Directory created: {os.path.abspath(target_dir)}")
        return

    # --- Tworzenie pliku z zawartością ---
    filepath = os.path.join(target_dir, filename)

    print("Enter content line (type 'stop' to finish):")
    lines = []
    while True:
        line = input("Enter content line: ")
        if line.strip().lower() == "stop":
            break
        lines.append(line)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(filepath, "a", encoding="utf-8") as f:
        f.write(f"{timestamp}\n")
        for idx, line in enumerate(lines, start=1):
            f.write(f"{idx} {line}\n")
        f.write("\n")

    print(f"File created/updated: {os.path.abspath(filepath)}")


if __name__ == "__main__":
    main()
