import sys
import argparse
import textwrap

parser = argparse.ArgumentParser(
        description = ("Converts FastQ files to FastA files. \n"
                        "Input must be a '.fastq' or '.fq' file. \n"
                        "Due to the nature of conversion, the sequencing quality will be lost. \n"
                        "Optional '-w' option will wrap sequences into 100 nt chunks"
                        ),
        epilog = "Outputs a .fasta file with the name and sequence \n"
                                )

parser.add_argument("file", metavar = "-file", help = "A FastQ file. \n"
                                                        "Accepts common extensions including '.fastq', '.fq', '.FASTQ', '.FQ'"
                    )

parser.add_argument("-w", "--wrap", action = "store_true",
                    help = "optional argument placed after the file that wraps sequences into 100 nt chunks"
                    )

args = parser.parse_args()

def fastQ_to_dict(file_input):
    #Start empty dict
    parsed_fastq = {}
    
    try:
        with open(file_input, "r") as file:
            #Makes sures to keep on looping until there are no more '@' lines
            while True:
                #First line should the the header if not, it ends loop
                header = file.readline().strip()
                if not header:
                    break
                #Second line should be sequence
                sequence = file.readline().strip()
                #Third line is '+' and fourth line is seq quality to ignore
                _ = file.readline().strip()
                _ = file.readline().strip()
                
                #Add sequence name and sequence to dictionary
                parsed_fastq[header[1:]] = sequence
            
            return parsed_fastq
   
    except:
        return "Not a compatible FastQ file"

def dict_to_fasta(parsed_fastq_2):
    #Writes the dictionary to file without wrapping
    with open("Sequences.fasta", "w") as file_output:
        for (key, value) in parsed_fastq_2.items():
            #Prints name and sequences as a fasta format
            file_output.write(">" + str(key) + "\n" + str(value) + "\n")

def dict_to_fasta_wrap(parsed_fastq_3):
    with open("Sequences.fasta", "w") as file_output:
        for (key, value) in parsed_fastq_3.items():
            #Prints the 'Name' of the sequence first
            file_output.write(">" + str(key) + "\n")
            #Then prints the sequence in a new line wrapped at 100 characters
            file_output.write(textwrap.fill(str(value), 100) + "\n")

if __name__ == "__main__":
    try:
        #Checks if inputs arguments are greater than 2
        if len(sys.argv) >= 2:
            if len(sys.argv) == 2:
                #Checks for fastq extensions
                if sys.argv[1].endswith((".fastq", ".fq", ".FASTQ", ".FQ")):
                    #Then converts to dictionary then fasta file
                    seqs = fastQ_to_dict(sys.argv[1])
                    dict_to_fasta(seqs)
                    print("Sequences.fasta successfully created")
                else:
                    raise FileNotFoundError
            elif len(sys.argv) == 3 and sys.argv[2] == "-w":
                if sys.argv[1].endswith((".fastq", ".fq", ".FASTQ", ".FQ")):
                    seqs = fastQ_to_dict(sys.argv[1])
                    dict_to_fasta_wrap(seqs)
                    print("Sequences.fasta successfully created")
                else:
                    raise FileNotFoundError
            else:
                raise IOError
        else:
            raise IOError
    except (FileNotFoundError, IOError):
        sys.exit("The file does not exists or it is not an acceptable input file, incorrect arguments, or too many inputs. Check file extension.")
    