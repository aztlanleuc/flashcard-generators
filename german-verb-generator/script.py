from csv import reader, writer

# the input file should be a tsv with a header row, and 8 columns
# one for the infinitive form of the verb, and then one each for the various
# conjugated forms (ich, du, er/sie/es, wir, ihr, sie, Sie)
input_file = open("input-verbs.csv")
input_content = reader(input_file)

# we want to have two output files: one for conjugation cards and one for definition cards
# the conjugation file will have two columns, first the verb infinitive with a pronoun in brackets,
# followed by the conjugation of the verb for that pronoun. the definition file will have
# two columns as well, first the verb infinitive followed by the english translation
conjugation_file = open("conjugation-cards.csv", "w")
definition_file = open("definition-cards.csv", "w")


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
    writer(conjugation_file).writerow([word + " (ich)", line[2]])
    writer(conjugation_file).writerow([word + " (du)", line[3]])
    writer(conjugation_file).writerow([word + " (er/sie/es)", line[4]])
    writer(conjugation_file).writerow([word + " (wir)", line[5]])
    writer(conjugation_file).writerow([word + " (ihr)", line[6]])
    writer(conjugation_file).writerow([word + " (sie)", line[7]])
    writer(conjugation_file).writerow([word + " (Sie)", line[8]])

    # write the word and defintion to the definition
    writer(definition_file).writerow([word, line[1]])

    line_count += 1

# print the number of lines processed, allowing for an off-by-one error
# since there's a header row
print(f'processed {line_count - 1} verbs')

# close all the files
input_file.close()
conjugation_file.close()
definition_file.close()
