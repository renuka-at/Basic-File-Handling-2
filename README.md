**Overview**
This assignment contains three Python scripts for handling gene level information retrieval. 
The io_utils.pyscript provides functions for handling file operations such as opening file handles
and config.py provides assisting functions for get_gene_level_information.py
The get_gene_level_information.py script takes command-line arguments for host and gene name, and retrieves gene level information based on the configuration provided in the module config file.

**Script 1: io_utils.py**
**Description**
The io_utils.pyscript provides functions for handling file operations such as opening file handles in read or 
write mode, checking if a gene file is valid, and retrieving configuration information from a module config file.

**Functions**
get_filehandle(file, mode): This function takes two arguments - file and mode - and returns a file handle.
It opens the file with the given mode (either "r" for read or "w" for write). If the file cannot be opened, it raises an exception with an error message.

is_gene_file_valid(file): This function takes a file path as an argument and checks if the gene file is valid. It returns a boolean value indicating whether the file exists or not.

**Script 2: config.py**
**Description**
Assists the get_gene_level_information.py script with the following functions
get_directory_for_unigene(): This function returns the directory path for the gene name file.

get_extension_for_unigene(): This function returns the file extension for the gene name file.

get_keyword_for_hosts(): This function returns a dictionary with keywords for host names, both common and scientific names.

get_error_string_4_ValueError(): This function prints an error message for invalid arguments
for a ValueError exception.

get_error_string_4_TypeError(): This function prints an error message for invalid arguments passed 
 for a TypeError exception.

get_error_string_4_PermissionError(file): This function prints an error message for permission errors
when creating a directory for a file.

get_error_string_4_FileNotFoundError(file): This function prints an error message for file not found errors
when creating a directory for a file.

get_error_string_4_opening_file_OSError(file, mode): This function prints an error message for OSError
when opening a file handle with a specific mode.

get_error_string_4_opening_directory_OSError(directory): This function prints an error message for OSError 
when opening or creating a directory.

MyOSError: This is a custom exception class raised for errors related to OSError. 
It takes three arguments - file, mode, and err - and provides a custom error message.

**Script 3: get_gene_level_information.py**
**Description**
The get_gene_level_information.py script takes two command-line arguments for host and gene name, and 
retrieves gene level information based on the configuration provided in the module config file.

**Dependencies**
The get_gene_level_information.py script has the following dependencies:

Python 3.x
argparse module, os module, re module, sys, module
assignment5.config module 
assignment5.utils module

**Usage**
The script can be executed from the command line with the following syntax:

python3 get_gene_level_information.py --host <host_name> --gene <gene_name>
--host: The host name for which gene level information is to be retrieved. 
--gene: The gene name for which information is to be retrieved.

The script requires the argparse module for parsing command-line arguments, as well as the assignment5 module for 
importing configuration and file operation functions from the io_utils.py and config.py scripts.

python get_gene_level_information.py --host "human" --gene "BRCA1"
This will retrieve gene level information for the "BRCA1
"BRCA1" gene in the human host, based on the configuration provided in the module config file.

**Workflow**
The get_gene_level_information.py script follows the following workflow:

Parse the command-line arguments using the argparse module.
Validate the host name and gene name provided as arguments.
Retrieve the configuration information from the module config file using functions from the io_utils.pyscript.
Check if the gene file for the host exists and is valid using functions from the io_utils.pyscript.
Retrieve the gene level information from the gene file for the specified gene name.
Display the retrieved gene level information to the user.

**Output**
example output:
python3 get_gene_level_information.py --host horse --gene API5

Found Gene API5 for Equus caballus
In Equus caballus, There are 3 tissues that API5 is expressed in:

  1. Adult
  2. Blood
  3. Cartilage

**Author**
Renuka Athinarayanan