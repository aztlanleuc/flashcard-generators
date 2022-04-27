import csv

# the input file should be a tsv with a header row, and 8 columns
# one for the infinitive form of the verb, and then one each for the various
# conjugated forms (ich, du, er/sie/es, wir, ihr, sie, Sie)
input_file = open("input-verbs.tsv")
input_content = csv.reader(input_file, delimiter="\t")

# the output file will have two columns written to it, the verb infinitive with
# a pronoun in brackets, and the conjugated form
output_file = open("output-cards.tsv", "wt")

tsv_writer = csv.writer(output_file, delimiter="\t")

# keep track of the number of lines we've processed for funsies
# TODO: time how long it takes to process?
line_count = 0

# iterate through each row and process
for line in input_content:
    # skip the header row of the input data
    if line_count == 0:
        line_count += 1
        continue

    # extract out the word and conjugations, and write them to the output file
    word = line[0]
    print(word)
    tsv_writer.writerow([word + " (ich)", line[1]])
    tsv_writer.writerow([word + " (du)", line[2]])
    tsv_writer.writerow([word + " (er/sie/es)", line[3]])
    tsv_writer.writerow([word + " (wir)", line[4]])
    tsv_writer.writerow([word + " (ihr)", line[5]])
    tsv_writer.writerow([word + " (sie)", line[6]])
    tsv_writer.writerow([word + " (Sie)", line[7]])

    line_count += 1

# print the number of lines processed, allowing for an off-by-one error
# since there's a header row
print(f'processed {line_count - 1} verbs')

input_file.close()
output_file.close()
