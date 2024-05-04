import sys
import shutil
from pathlib import Path

# Constants
DEFAULT_TARGET_FOLDER = "dist"


def getArgs():
    args = {
        'source_dir': None,
        'target_dir': DEFAULT_TARGET_FOLDER,
        'max_depth': 1
    }

    if len(sys.argv) < 2:
        raise ValueError(
            "Insufficient arguments provided. Usage: python task-1.py <source_directory> [target_directory] [max_depth]")

    args['source_dir'] = Path(sys.argv[1])
    if len(sys.argv) == 4:
        args['target_dir'] = Path(sys.argv[2])
        args['max_depth'] = int(sys.argv[3])
    elif len(sys.argv) == 3:
        try:
            args['max_depth'] = int(sys.argv[2])
        except ValueError:
            args['target_dir'] = Path(sys.argv[2])
            print(f"Missing max_depth argument, using {args['max_depth']} as default value.")

    return args


def deep_copy_files(source_dir: Path, target_dir: Path, current_depth: int, max_depth: int):
    if current_depth > max_depth:
        return

    try:
        if not target_dir.exists():
            target_dir.mkdir(parents=True, exist_ok=True)

        for item in source_dir.iterdir():
            if item.is_dir():
                if item != target_dir:
                    deep_copy_files(item, target_dir, current_depth + 1, max_depth)
            else:
                extension = item.suffix[1:] if item.suffix else "no_extension"
                extension_dir = target_dir / extension
                if not extension_dir.exists():
                    extension_dir.mkdir(parents=True, exist_ok=True)
                shutil.copy(item, extension_dir)

    except Exception as error:
        print(f"Error processing {source_dir}: {error}")


def main():
    try:
        args = getArgs()
        deep_copy_files(Path(args['source_dir']), Path(args['target_dir']), 1, args['max_depth'])
        print("Files have been copied and sorted by extension.")
    except Exception as error:
        print(error)


if __name__ == "__main__":
    main()
