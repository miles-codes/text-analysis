import argparse
import re
from itertools import combinations, islice


def analyze(filepath, char_length=3, top_n=10, output_file=None):

    results = {}

    with open(filepath, 'r') as file:
        for line in file:
            for word in line.split():

                # Lowercase the word, remove non-alphanumeric characters, remove duplicate characters, and sort
                word = sorted(set(re.sub(r'\W+', '', word.lower())))

                # get all combinations of chars from a word
                combs = list(combinations(word, char_length))

                # add each triplet to dict and count
                for c in combs:
                    results[c] = results.get(c, 0) + 1

    # order by number of occurrences descending
    results_ordered = {
        key: results[key] for key in sorted(results, key=results.get, reverse=True)
    }

    top_results = list(islice(results_ordered.items(), top_n))

    # write to output file
    if output_file:
        with open('output/' + output_file, 'w') as file:
            for result in top_results:
                file.write(str(result) + '\n')

    # return top n
    return top_results


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Analyze text files.')
    parser.add_argument('--file', '-f', metavar='filepath', type=str,
                        help='path to a file to be read', required=True, dest='filepath')
    parser.add_argument('--length', '-l', metavar='length', type=int,
                        help='length of different characters in a word, default=3', default=3, dest='length')
    parser.add_argument('--top', '-t', metavar='n', type=int,
                        help='show top n results, default=10', default=10, dest='top_n')
    parser.add_argument('--output', '-o', metavar='output', type=str,
                        help='write output to this file', default=None, dest='output_file')

    args = vars(parser.parse_args())

    result = analyze(args['filepath'], args['length'], args['top_n'], args['output_file'])

    for i in result:
        print(i)
