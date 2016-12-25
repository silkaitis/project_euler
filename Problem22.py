'''
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
containing over five-thousand first names, begin by sorting it into alphabetical
order. Then working out the alphabetical value for each name, multiply this
value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN,
which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
So, COLIN would obtain a score of 938 x 53 = 49714.

What is the total of all the name scores in the file?
'''
import string
import numpy as np

def letter_num_dict():
    soln = {}

    for i, val in enumerate(list(string.ascii_uppercase)):
        soln[val] = i + 1

    return(soln)

def load_data(fname):
    with open(fname, 'r') as f:
        soln = f.readline()

    soln = soln.replace('"', '').split(',')

    return(soln)

def name_score(name, letter_num_dict):
    soln = 0

    for val in list(name):
        soln += letter_num_dict[val]

    return(soln)

def score_list(data):
    order = np.argsort(data)
    code = letter_num_dict()

    soln = 0
    for i, idx in enumerate(order):

        soln += (i + 1) * name_score(data[idx], code)

    return(soln)

if __name__ == '__main__':
    data = load_data('p022_names.txt')

    total = score_list(data)

    print('Total of all name scores is {}'.format(total))
