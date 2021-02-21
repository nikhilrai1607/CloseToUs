
Installation:

git clone https://github.com/nikhilrai1607/CloseToUs.git

Version: Python 3
No third party modules used.

-------------------
Steps:

1. cd /to/path/downloaded/repo
2. python3 -m unittest testing
3. If all good! Output file is created "test_out.txt" - This is Result
4. python3 implementation.py
5. open file mentioned on step 4 to configure and test.

-------------------
Information:

** Function is console based
** As per defined input: Code does NOT take any console input
** Code will exit on error with appropriate message on console.

1. All the functions can be tested.
2. test cases are in testing.py
3. Main Class is CloseToUs.py
4. implementation.py gives example and implements the class.

5. There are 2 implementations for the class:
  (As it wasnt mentioned on the test file, if input file is local or url based):
  - Local File Based (Default)
    The program will fetch data from a local file.
  - URL based
    A url can be supplied, with flag "localFile=False" (Example in implementation.py)

6. Output file can also be assigned to the class.
7. Range = 100 and Lat,Long as given in test file.
8. Above can be adjusted in CloseToUs.py
9. test_data folder has 2 files:
 - One regular supplied text
 - Another with couple of entries with malformed json for test case.


-------------------
CLASS Config:

Initializing class takes 3 arguments:
 - filename: can be local path/ URL 
 - localFile: bool flag True if file is local/ False if file is through a URL
 - Outfile: filename for output file.
 
 To test the code yourself manually:
 - Modify the code given in implementation.py. Or import and use based on example given in implementation.py.
 - Make sure to set localFile as False if accessing txt file through URL.
 - implementation.py has a commented code for local file. Uncomment and check if needed.

Problem statement is divided in few sections:

- Read file
   From local path/ URL
- Decode JSON
   Makes sure, parsing line by line, that malformed json are IGNORED.
- Calculate distance
   Base formula applied
   Range calculated
   get sorted list as result
- Write the result to a file

OUTPUT:
- No info provided for the output format
- Hence it is kept consistent as input i.e, JSON format.
- output.txt is available as result of this test.
