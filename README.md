# Photo Name Sorter

This Python script sorts the lines in a Markdown file based on the numerical part of image file names embedded in the text. It's particularly useful for organizing photo references in Markdown documents.

## Features

- Reads a Markdown file containing image references
- Sorts the lines based on the numerical part of the image file names
- Writes the sorted lines to a new Markdown file
- Handles lines without matching image references gracefully

## Requirements

- Python 3.x

## Usage

1. Ensure your input Markdown file is in the same directory as the script.
2. The default input file name is set to "GC.md". If your file has a different name, update the `FILE_NAME` variable in the script.
3. Run the script:

   ```
   python sort_names.py
   ```

4. The script will create a new file named "sorted_GC.md" (or "sorted_[YOUR_FILE_NAME].md" if you changed the input file name) with the sorted content.

## How it works

1. The script opens and reads the specified Markdown file.
2. It uses a regular expression to find image references in the format `![[IMG_XXXX.jpg]]`, where XXXX is a number.
3. The lines are sorted based on the numerical part of the image file names.
4. Lines without matching image references are placed at the beginning of the sorted list.
5. The sorted lines are written to a new file with "sorted_" prefixed to the original file name.

## Output

The script will print a message indicating the completion of the sorting process and the name of the output file.

## Note

Ensure you have write permissions in the directory where the script is located, as it needs to create a new file for the sorted output.