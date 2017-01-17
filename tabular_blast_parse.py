from collections import Counter
import csv
import sys

def create_blast_summary(infile, outfile, species_column):
    species_index = species_column - 1
    species_list = []
    with open(infile) as blast_results:
        for line in blast_results:
            results = line.rsplit('\t')
            species = results[species_index]
            species_list.append(species)

    summary = Counter(species_list)
    summary_sorted = summary.most_common()

    with open(outfile, 'w') as output:
        tablewriter = csv.writer(output)
        tablewriter.writerow(['species name', 'count'])
        for species, count in summary_sorted[0:100]:
            tablewriter.writerow([species, count])
    
    print('top 100 results written to file. top 10 results: \n', summary_sorted[0:10])

if __name__ == '__main__':
    if len(sys.argv) == 4:
         create_blast_summary(sys.argv[1], sys.argv[2], int(sys.argv[3]))
    else:
         print("Usage: tabular_blast_parse.py blast_results.txt outfile column_to_count")
         sys.exit(0)


