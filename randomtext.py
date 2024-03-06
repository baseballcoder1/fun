'''
https://github.com/baseballcoder1

Very basic Markov chain text generator for fun
'''

from collections import deque
from random import choice, choices

if __name__ == '__main__':
    '''
    Number of words in each group, higher = better
    '''
    k = 3
    '''
    File name
    '''
    filename = 'text.txt'
    '''
    Initial words seperated by spaces
    '''
    initial = 'i'
    '''
    Total additional words to generate
    '''
    numwords = 20
    
    maxwords = 100000
    words = []
    with open(filename, 'r', encoding='utf-8') as f:
        for s in f.readlines():
            s = ''.join([ch for ch in s if ch.isalpha() or ch.isspace()])
            words.extend(s.lower().split())
            if len(words) >= maxwords:
                words[maxwords:] = []
                break
    if len(words) < k:
        raise Exception('File ' + filename + ' not enough text')
    print('Total', len(words), 'words')

    window = deque(words[:k])

    def h(x):
        return ' '.join(x)
    count = {}
    
    for word in words[k:]:
        x = h(window)
        window.popleft()
        window.append(word)
        y = h(window)
        if x not in count:
            count[x] = {}
        if y not in count[x]:
            count[x][y] = 0
        count[x][y] += 1

    initialwords = initial.split()
    initialchoices = [x for x in count.keys() if x.split(' ')[:len(initialwords)] == initialwords[:k]]
    if len(initialchoices) == 0:
        raise Exception("Can't match initial" + initial)
    print('Total', len(initialchoices), 'initial choices')
    current = choice(initialchoices)
    print(current, end='')
    for i in range(numwords):
        if len(count[current]) == 0:
            break
        current = choices(list(count[current].keys()), list(count[current].values()))[0]
        print(' ' + current.split(' ')[-1], end='')
    print()
