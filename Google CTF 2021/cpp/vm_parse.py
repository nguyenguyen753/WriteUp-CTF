leak = [i.strip() for i in open('./cpp.c', 'r').readlines()]
var = []
num = 1924
# start = 2 + num
# finish = 4291 + num
start = 839
finish = 1919
pad = ""

# for i in range(111, 840):
    # print(leak[i].split(' ')[1].strip()[4:])
    # print('li[\'{}\'] = {}'.format(leak[i].split(' ')[1].strip()[4:], leak[i].split(' ')[2].strip()))

for i in range(start, finish):
    if leak[i - 1].find('#if') != -1:
        pad += '\t'
    if leak[i].find('endif') != -1:
        pad = pad[:-1]

    if (i == start):
        pad = ""

    if leak[i].find('undef') != -1:
        string = pad + leak[i].split(' ')[-1]
        print('{} = 0'.format(string))
    elif leak[i].find('define') != -1:
        string = pad + leak[i].split(' ')[1]
        if leak[i].split(' ')[1].find('ROM') != -1:
            string = pad + 'li[\'{}\']'.format(leak[i].split(' ')[1][4:])
        number = 1
        if len(leak[i].split(' ')) == 3:
            number = int(leak[i].split(' ')[2].strip())
        print('{} = {}'.format(string, number))
        if (leak[i].split(' ')[1] not in var):
            var.append(leak[i].split(' ')[1])
    elif leak[i].find('ifndef') != -1:
        string = pad + 'if {} == 0:'.format(leak[i].split(' ')[1])
        print(string)
    elif leak[i].find('ifdef') != -1:
        string = pad + 'if {} == 1:'.format(leak[i].split(' ')[1])
        print(string)
    elif leak[i].find('else') != -1:
        # if (leak[i-1].find('endif') != -1):
        pad = pad[:-1]
        string = pad + 'else:'
        print(string)
        pad += '\t'
        # else:
        #     pad = pad[:-1]
        #     string = pad + 'else:'
        #     print(string)
    elif leak[i].find('#if ') != -1:
        string = pad + leak[i][1:] + ':'
        if leak[i].find('FLAG') != -1:
            # print(leak[i][1:])
            string = pad + 'if ord(input[{}])'.format(leak[i][1:][8:10].strip())
            if (len(leak[i][1:][8:10].strip()) == 1):
                string += ' '

            string += leak[i][1:][10:] + ':'
        print(string)
        # break
    elif leak[i].find('error') != -1:
        string = pad + 'error({})'.format(leak[i].split(' ')[1])
        print(string)
        # break
    else:
        if leak[i].find('endif') != -1: continue
        print(leak[i], i)
        break

# for i in var:
#     print("{} = 0".format(i))

