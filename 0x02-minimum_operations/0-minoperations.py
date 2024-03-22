#!/usr/bin/python3
'''defines minimum operations coding challenge.
'''


def minOperations(n):
    '''computs the fewest number of operations
    needed to result.
    '''
    if not isinstance(n, int):
        return 0
    opsCount = 0
    clipboard = 0
    done = 1
    # print('H', end='')
    while done < n:
        if clipboard == 0:
            # init (the first copy all and paste)
            clipboard = done
            done += clipboard
            opsCount += 2
            # print('-(11)->{}'.format('H' * done), end='')
        elif n - done > 0 and (n - done) % done == 0:
            # copy all and paste
            clipboard = done
            done += clipboard
            opsCount += 2
            # print('-(11)->{}'.format('H' * done), end='')
        elif clipboard > 0:
            # paste
            done += clipboard
            opsCount += 1
            # print('-(01)->{}'.format('H' * done), end='')
    # print('')
    return opsCount

