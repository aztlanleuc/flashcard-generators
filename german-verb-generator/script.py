from csv import DictReader, writer

# the input file should be a tsv with a header row, and 8 columns
# one for the infinitive form of the verb, and then one each for the various
# conjugated forms (ich, du, er/sie/es, wir, ihr, sie, Sie)
input_file = open("input-verbs.csv")
input_content = DictReader(input_file)

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
    # extract out the word and conjugations, and write them to the conjugation file
    word = line["verb"]
    print(word)
    writer(conjugation_file).writerow([word + " (ich)", line["ich"]])
    writer(conjugation_file).writerow([word + " (du)", line["du"]])
    writer(conjugation_file).writerow([word + " (er/sie/es)", line["er/sie/es"]])
    writer(conjugation_file).writerow([word + " (wir)", line["wir"]])
    writer(conjugation_file).writerow([word + " (ihr)", line["ihr"]])
    writer(conjugation_file).writerow([word + " (sie)", line["sie"]])
    writer(conjugation_file).writerow([word + " (Sie)", line["Sie"]])

    # write the word and definition to the definition
    writer(definition_file).writerow([word, line["translation"]])

    line_count += 1

# print the number of lines processed
print(f'processed {line_count} verbs')

# close all the files
input_file.close()
conjugation_file.close()
definition_file.close()
