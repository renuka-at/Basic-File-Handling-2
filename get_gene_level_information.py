"""
This script takes two command-line arguments of host and gene name and returns the gene level information
"""
import sys
import re
import argparse
from assignment5 import config, io_utils


def main():
    """Business Logic"""
    # get command line arguments
    args = get_args()
    host_n = args.host
    gene = args.gene
    # get the updated host and temp host names
    host, temp_host = update_host_name(host_n)
    # get the file name using assignment5.config module
    file = "/".join(
        (config.get_directory_for_unigene(), host, gene + "." + config.get_extension_for_unigene())
                )
    # check for the existence of file else exit the program
    if io_utils.is_gene_file_valid(file):
        print(f"\nFound Gene {gene} for {temp_host}")
    else:
        print("Not found")
        print(f'Gene {gene} does not exist for {temp_host}. exiting now...', file=sys.stderr)
        sys.exit(1)
    # tissues names sorted in ascending order
    sorted_tissues = get_data_for_gene_file(file)
    # print info regarding, host, gene and in which tissues they are found
    output = print_host_to_gene_name_output(temp_host, gene, sorted_tissues)
    print(output)


def update_host_name(host_name):
    """
    checks if the host name given in the command-line exists in the dict output of
    config.get_keyword_for_hosts()
    :param host_name: name of the host given from the command-line
    :return: returns an updated host name and temp host name by accessing it from the dict
        if host name not found, it exits the program
    """
    host_name = host_name.replace("_", " ")
    host_name = host_name.lower()    # convert host names to lower case
    ky_host_dict = config.get_keyword_for_hosts()
    for keys, _ in ky_host_dict.items():
        if host_name in keys:
            name = ky_host_dict[keys]
            temp_name = name.replace("_", " ")
            break
    else:
        # the helper function that returns the accepted names and host directory names
        _print_directories_for_hosts()
        sys.exit()
    return name, temp_name


def _print_directories_for_hosts():
    """
    A helper function that prints the directories for hosts and common names of the host that can be provided as
    command-line arguments for host name
    :return: none
    """
    print(f'\nEither the Host Name you are searching for is not in the database\n'
          f'\nor If you are trying to use the scientific name please put the name in double quotes:\n'
          f'\n"Scientific name"\n'
          f'\nHere is a (non-case sensitive) list of available '
          f'\nHosts by scientific name\n')
    dict_ = config.get_keyword_for_hosts()
    num = 1
    values = dict_.values()
    values = set(set(values))
    for val in values:
        print(f'{num:2}. {val}')
        num += 1
    print(f'\nHere is a (non-case sensitive) list of available'
          f'\nHosts by a common name\n')
    kie = list(dict_)
    kie = [i.title() for i in kie]
    keys = sorted(kie)
    s_num = 1
    for key in keys:
        # list of values of common names from the dict_ for each key
        print(f'{s_num:2}. {key.capitalize ()}')
        s_num += 1


def get_data_for_gene_file(gene_file):   # function call with (file)
    """
    Gets the path for the file as the input, opens it using io_utils.get_filehandle(file,mode);
    looks for the pattern to extract the name of the tissues and returns a list of sorted tissues
    :param gene_file: gene file path
    :return: a sorted list of tissues
    """
    f_open = io_utils.get_filehandle(gene_file, "r")
    try:
        for line in f_open:
            match = re.search(r"\bEXPRESS\s+([\w\s()|/-]+)", line)
            if match:
                tissue_string = match.group(1).split('|')
                tissue_list = [st.strip() for st in tissue_string]
                tissue_sorted = sorted(tissue_list)
                return tissue_sorted
        return None
    finally:
        f_open.close()    # Close the file in the 'finally' block


def print_host_to_gene_name_output(host_name, gene_name, lst_sort_tis):
    """
    Takes 3 parameters and prints that the gene is found that particular host along with the number and
    name of the tissues where the gene is found in that host
    :param host_name: name of the host, (updated host name)
    :param gene_name: gene name given at the command-line
    :param lst_sort_tis: the sorted tissue list
    :return: two f'string statements for printing the output
    """
    tis_count = len(lst_sort_tis)
    first_line = f'In {host_name}, There are {tis_count} tissues that {gene_name} is expressed in:\n'
    second_line = ''
    num = 1
    for tissues in lst_sort_tis:
        tissues = tissues.capitalize()
        second_line += f'\n{num:2}. {tissues}'
        num += 1
    return first_line + second_line


def get_args():
    """
    Gets the input arguments of host and gene name from the command-line.
    Command line options using argparse
    :return: Instance of argparse arguments
        """
    parser = argparse.ArgumentParser(description=' Give Host name and Gene name')
    parser.add_argument('--host', metavar='HOST', type=str,
                        help='Name of Host', default='Homo sapiens')
    parser.add_argument('--gene', metavar='GENE', type=str, help='Name of Gene', default='TGM1')
    return parser.parse_args()


if __name__ == '__main__':
    main()
