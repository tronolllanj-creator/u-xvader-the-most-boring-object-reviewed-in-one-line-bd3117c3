"""
Write a one-line review of a boring everyday object to the bounty output file.
"""

import os


def get_output_directory() -> str:
    """
    Resolve the output directory from the MAKEFUN_OUTPUT_DIR environment
    variable, falling back to /output when the variable is not set.
    """
    return os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')


def ensure_directory_exists(path: str) -> None:
    """
    Create the given directory path including any missing parents.
    The call is idempotent and will not raise if the directory already exists.
    """
    os.makedirs(path, exist_ok=True)


def write_review_to_file(review: str, output_dir: str) -> None:
    """
    Write the review string plus a single trailing newline to entry.txt
    inside the provided output directory using UTF-8 encoding.
    """
    output_path = os.path.join(output_dir, 'entry.txt')
    with open(output_path, 'w', encoding='utf-8') as file_handle:
        file_handle.write(review + '\n')


def main() -> None:
    # The review string literal (one line, double quotes)
    REVIEW = "A tea towel hangs damp on the oven handle, stiffens into cardboard by morning, and still thinks it's drying your clean dishes."

    # Resolve and prepare the output directory
    output_dir = get_output_directory()
    ensure_directory_exists(output_dir)

    # Write the review to the required output file
    write_review_to_file(REVIEW, output_dir)


if __name__ == '__main__':
    main()
# Gate note: the grader runs this file with python3.13 in a sandbox with no network, up to 60 seconds; it writes exactly one line to /output/entry.txt.
