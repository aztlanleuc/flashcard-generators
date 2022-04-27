import csv

# the input file should be a tsv with a header row, and 8 columns
# one for the infinitive form of the verb, and then one each for the various
# conjugated forms (ich, du, er/sie/es, wir, ihr, sie, Sie)
input_file = open("input-verbs.tsv")
input_content = csv.reader(input_file, delimiter="\t")

# we want to have two output files: one for conjugation cards and one for definition cards
# the conjugation file will have two columns, first the verb infinitive with a pronoun in brackets,
# followed by the conjugation of the verb for that pronoun. the definition file will have
# two columns as well, first the verb infinitive followed by the english translation
conjugation_file = open("conjugation-cards.tsv", "wt")
definition_file = open("definition-cards.tsv", "wt")

conj_writer = csv.writer(conjugation_file, delimiter="\t")
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

    # extract out the word and conjugations, and write them to the conjugation file
    word = line[0]
    print(word)
    conj_writer.writerow([word + " (ich)", line[2]])
    conj_writer.writerow([word + " (du)", line[3]])
    conj_writer.writerow([word + " (er/sie/es)", line[4]])
    conj_writer.writerow([word + " (wir)", line[5]])
    conj_writer.writerow([word + " (ihr)", line[6]])
    conj_writer.writerow([word + " (sie)", line[7]])
    conj_writer.writerow([word + " (Sie)", line[8]])

    # write the word and defintion to the definition
    def_writer.writerow([word, line[1]])

    line_count += 1

# print the number of lines processed, allowing for an off-by-one error
# since there's a header row
print(f'processed {line_count - 1} verbs')

# close all the files
input_file.close()
conjugation_file.close()
definition_file.close()
