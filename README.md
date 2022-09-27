# Python Line Count Exercise

This repository takes a directory as a required argument and a filename extension as optional argument that defaults to “.txt”. line_count.py finds all the files with the given extension in the directory provided and all its subdirectories. It prints the name of all the matching files with the number of lines present in that file.

The program also shows the total number of matching files, total number of lines in all those files and the average number of lines per file.


## To Run
You can use the below commands as unit tests to verify the correctness of the program.

To run line_count.py you need to provide a directory name with --dir flag. The default extension of the files to be searched is *.txt*.
```
$ python line_count.py --dir .
./file2.txt 	7
./file1.txt 	25
./d1/d1fb.txt 	21
./d1/d1fa.txt 	14
===============
Number of files found:	4
Total number of lines:	67
Average lines per file:	16.75
```

You can also specify *.txt* extension explicitly using --ext flag and it will give same result as above.
```
$ python line_count.py --dir . --ext .txt
./file2.txt 	7
./file1.txt 	25
./d1/d1fb.txt 	21
./d1/d1fa.txt 	14
===============
Number of files found:	4
Total number of lines:	67
Average lines per file:	16.75
```

You can also give an extension of your choice e.g., *.pdf* using --ext flag.
```
python line_count.py --dir . --ext .pdf
./file3.pdf 	6
./d1/d1fc.pdf 	12
===============
Number of files found:	2
Total number of lines:	18
Average lines per file:	9.0
```

If there are no files with the given extension:
```
$ python line_count.py --dir . --ext .doc
===============
Number of files found:	0
Total number of lines:	0
Average lines per file:	0
```

If the directry doesn't exists it will print *The directory does not exist* and exit from the program.
```
$ python line_count.py --dir \Users\doc
The directory does not exist
```

## Pylint
The code in this repository passed pylint:
```
$ pylint analog_devices/

--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)
```