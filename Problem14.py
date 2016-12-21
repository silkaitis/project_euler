'''
The following iterative sequence is defined for the set of positive integers:

n -> n/2 (n is even)
n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem),
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?
'''
import operator
import sys

def even_odd_op(num):
    '''
    Perform operation on number given even or odd
    '''
    if bool(i % 2):
        return(3 * num + 1)
    else:
        return(num / 2)

def setup_progress_bar(num):
    '''
    Setup progress bar
    '''
    sys.stdout.write("[%s]" % (" " * num))
    sys.stdout.flush()
    sys.stdout.write("\b" * (num + 1))

def update_progress_bar(num, test, step):
    '''
    Update progress bar
    '''
    if num == test:
        sys.stdout.write("-")
        sys.stdout.flush()
        step += 1
        return(step)
    else:
        return(step)

if __name__ == '__main__':
        limit = int(1e6)

        toolbar_width = 50
        step = 1
        increment = limit / toolbar_width

        setup_progress_bar(toolbar_width)

        lengths = {}
        length_set = set()
        for i in xrange(1, limit + 1):
            test = increment * step
            step = update_progress_bar(i, test, step)

            #Build Chain
            start = i
            terms = 1

            while i > 1:
                i = even_odd_op(i)

                if i in length_set:
                    terms += lengths[i]
                    i = 1
                else:
                    terms += 1

            #Store chain length
            length_set.add(start)
            lengths[start] = terms

        sys.stdout.write("\n")

        soln = max(lengths.iteritems(), key=operator.itemgetter(1))[0]

        print('{} produces the longest chain'.format(soln))
