""" Import necessary libraries """
import os
import glob
import argparse


def line_count(directory, extension):
    """
    A function to count number of lines in files of a specific extension in the given
    directory and all of the subdirectories.
            Parameters:
                    directory (string): Path of the directory
                    extension (string): Extension of the file

    """
    # if directory not found
    if not os.path.exists(directory):
        print('The directory does not exist')
        return

    line_data = []
    for filename in glob.glob(f'**/*{extension}', recursive=True):
        with open(os.path.join(directory,filename), 'r', encoding="utf-8") as file_path:
            line_data.append([os.path.join(directory,filename),len(file_path.readlines())])

    # print(line_data)
    num_of_files = 0
    num_of_lines = 0
    for data in line_data:
        num_of_files += 1
        num_of_lines += data[1]
        print(f'{data[0]} \t{data[1]}')
    print('===============')

    print(f'Number of files found:\t{num_of_files}')
    print(f'Total number of lines:\t{num_of_lines}')
    if num_of_files:
        print(f'Average lines per file:\t{num_of_lines/num_of_files}')
    else:
        print(f'Average lines per file:\t{num_of_files}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', help='directory')
    parser.add_argument('--ext', default='.txt', help='file extension')

    args = parser.parse_args()
    line_count(args.dir, args.ext)
