```
>>=============================================================================<<
||███████╗ █████╗ ███████╗████████╗ ██████╗     ██████╗                        ||
||██╔════╝██╔══██╗██╔════╝╚══██╔══╝██╔═══██╗    ╚════██╗                       ||
||█████╗  ███████║███████╗   ██║   ██║   ██║     █████╔╝                       ||
||██╔══╝  ██╔══██║╚════██║   ██║   ██║▄▄ ██║    ██╔═══╝                        ||
||██║     ██║  ██║███████║   ██║   ╚██████╔╝    ███████╗                       ||
||╚═╝     ╚═╝  ╚═╝╚══════╝   ╚═╝    ╚══▀▀═╝     ╚══════╝                       ||
||                                                                             ||
||███████╗ █████╗ ███████╗████████╗ █████╗                                     ||
||██╔════╝██╔══██╗██╔════╝╚══██╔══╝██╔══██╗                                    ||
||█████╗  ███████║███████╗   ██║   ███████║                                    ||
||██╔══╝  ██╔══██║╚════██║   ██║   ██╔══██║                                    ||
||██║     ██║  ██║███████║   ██║   ██║  ██║                                    ||
||╚═╝     ╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝                                    ||
||                                                                             ||
|| ██████╗ ██████╗ ███╗   ██╗██╗   ██╗███████╗██████╗ ████████╗███████╗██████╗ ||
||██╔════╝██╔═══██╗████╗  ██║██║   ██║██╔════╝██╔══██╗╚══██╔══╝██╔════╝██╔══██╗||
||██║     ██║   ██║██╔██╗ ██║██║   ██║█████╗  ██████╔╝   ██║   █████╗  ██████╔╝||
||██║     ██║   ██║██║╚██╗██║╚██╗ ██╔╝██╔══╝  ██╔══██╗   ██║   ██╔══╝  ██╔══██╗||
||╚██████╗╚██████╔╝██║ ╚████║ ╚████╔╝ ███████╗██║  ██║   ██║   ███████╗██║  ██║||
|| ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝||
||                                                                             ||
>>=============================================================================<<

```
## FASTQ 2 FASTA Converter

FASTQ files are great in that they provide the sequencing quality to each result. Though the information is useful for
determening whether the results are trustworthy, we may just want to compare the sequencing results.
This script allows the conversion of the FASTQ file format to FASTA for less memory and easier sequencing comparison.

## Requirements
### Required dependecies 
Dependencies for script:
```
python 3.2 or above
```
The rest are standard Python libraries.

### Running the script
```
python fastq2fasta.py Sequences.fastq [-w]
```
Input file must be a .fastq, .FASTQ, .fq, or .FQ file extension
The optional "-w" writtenw without the bracket after the fastq file, will wrap the sequences into 100 nt chunks.

### Examples
#### Input FASTQ file

@DNA1<br>
GATGCATACTTCG<br>
+<br>
&%&%''&'+,005<br>
@DNA2<br>
GTTTTGTCG....GCGTTCAG<br>
+<br>
#&12289.....56:7674';

Note that DNA2 is more than 100 nt long.

#### Output FASTA file WITHOUT "-w" option
\>DNA1<br>
GATGCATACTTCG<br>
\>DNA2<br>
GTTTTGTCG....GCGTTCAG

#### Output FASTA file WITH the "-w" option
\>DNA1<br>
GATGCATACTTCG<br>
\>DNA2<br>
GTTTTGTCG....<br>GCGTTCAG

### Notes and Limitations
#### Input file
- A .fastq file.
  - The extension must end with ".fastq", ".fq" , ".FASTQ", ".FQ" for FastQ files.
  - Other extensions, including ".txt" files will not work.
  - Non UTF-8 characters may produce an error.
  - FastQ files are read in blocks of 4. If the FastQ is not properly formated, the file may not be read.

#### Output file.
- File will be named "Sequences.fasta".
  - If wrapping is enabled, it will produce 100 nt lines until end of sequence.

Please let me know if you encounter any bugs or problems.



