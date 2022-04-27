import csv

# the input file should be a tsv with a header row, and 3 columns
# they should be the singular form of the noun, the plural form, and then the translation
input_file = open("input-nouns.tsv")
input_content = csv.reader(input_file, delimiter="\t")

# we want to have two output files: one for plural/singular cards and one for definition cards
# the plural/singular file will have two columns, first the singular form then the plural
# the definition file will also have two columns, first the singular form then the translation
plurals_file = open("plurals-cards.tsv", "wt")
definition_file = open("definition-cards.tsv", "wt")

plural_writer = csv.writer(plurals_file, delimiter="\t")
def_writer = csv.writer(definition_file, delimiter="\t")

# keep track of the number of lines we've processed for funsies
# TODO: time how long it takes to process?
line_count = 0

# iterate through each row and process
for line in input_content:
    # skip the header row of the input data
    if line_count == 0:
        line_count += 1
        continue

    # print out the noun we're currently processing, and write the correct fields to the relevant file
    print(line[0])

    if line[1] != "":
        # we won't always have a plural form (some nouns are singular only) so in those cases, we don't 
        # want to make a card for the plural
        plural_writer.writerow([line[0], line[1]])
    def_writer.writerow([line[0], line[2]])

    line_count += 1

# print the number of lines processed, allowing for an off-by-one error
# since there's a header row
print(f'processed {line_count - 1} nouns')

# close all the files
input_file.close()
plurals_file.close()
definition_file.close()
