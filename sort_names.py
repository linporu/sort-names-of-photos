import re


FILE_NAME = "GC.md"


def main():

    with open(FILE_NAME, 'r') as file:
        lines = file.readlines()

        # Sort the lines based on the number in the pattern
        pattern = r'!\[\[IMG_(\d+)\.jpg\]\]'
        sorted_lines = sorted(lines, key=lambda line: int(re.search(pattern, line).group(1)) if re.search(pattern, line) else 0)

        with open(f'sorted_{FILE_NAME}', 'w') as output_file:
            output_file.writelines(sorted_lines)

        print(f"Sorting completed, results have been saved to the sorted_{FILE_NAME} file.")


if __name__ == "__main__":
    main()