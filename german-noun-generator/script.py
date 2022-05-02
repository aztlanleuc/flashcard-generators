from csv import DictReader, writer
from time import process_time

# the input file should be a tsv with a header row, and 3 columns
# they should be the singular form of the noun, the plural form, and then the translation
input_file = open("input-nouns.csv")
input_content = DictReader(input_file)

# we want to have two output files: one for plural/singular cards and one for definition cards
# the plural/singular file will have two columns, first the singular form then the plural
# the definition file will also have two columns, first the singular form then the translation
plurals_file = open("plurals-cards.csv", "w")
definition_file = open("definition-cards.csv", "w")

# keep track of the number of lines we've processed and 
# the time we started processing for funsies
line_count = 0
start_time = process_time()

# iterate through each row and process
for line in input_content:
    # print out the noun we're currently processing, and write the correct fields to the relevant file
    print(line["singular"])

    if line["plural"] != "":
        # we won't always have a plural form (some nouns are singular only) so in those cases, we don't 
        # want to make a card for the plural
        writer(plurals_file).writerow([line["singular"], line["plural"]])
    writer(definition_file).writerow([line["singular"], line["translation"]])

    line_count += 1

# keep track of when we finished the process
stop_time = process_time()

# print the number of lines processed and how long it took
print(f'processed {line_count} nouns in {stop_time - start_time:.4f}s')

# close all the files
input_file.close()
plurals_file.close()
definition_file.close()
