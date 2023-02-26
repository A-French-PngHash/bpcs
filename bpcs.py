import getopt
import sys
"""
bpcs

Command line options.

    -v "vessel image": provides the path to the host image.
    -h "hidden data file": provides the path to the secret data.
    -c {complexity}: Set the desired complexity threshold, must be strictly inferior to 0.5.

    -a: Analyses the storage capacity/needed (if vessel/if hidden) of the file provided.


"""

def main():
    opts = getopt.getopt(sys.argv[1:], "v:h:c:a:", [])
    complexity = None
    host_path = None
    hidden_path = None
    analyse = False

    for opt in opts:
        if opt[0] == "-c":
            complexity = opt[1]
        elif opt[0] == "-v":
            host_path = opt[1]
        elif opt[0] == "-h":
            hidden_path = opt[1]



if __name__ == "__main__":
    main()