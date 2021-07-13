def vm_parser():
    opcodes = list(b''.join(open("./prog.bin", "rb").readlines()))
    f = open("./log.txt", "w")
    memory = [0] * 30
    memory1 = [0] * 500

    # print(hex(opcodes[0x3f]))
    # print(opcodes)

    # inp = input("What's the flag? ")
    inp = "z3/;1850|106/732AC;05M7442510REh0/3T\w[B6;742X81/4G5fh231643ac>\\"

    print(inp)

    # print(opcodes)

    id_opcode = 0
    id_mem = 0
    rcx = 0
    id_inp = 0
    check_counter = 0
    state = 0

    #edx: id_opcode

    while (1):
        # if (id_opcode == 622): state = 1
        # print(id_opcode, hex(opcodes[id_opcode]))
        # if (state == 1):
        #     print(memory)

        f.write("\n")
        f.write("{}, {}".format(hex(opcodes[id_opcode]), id_opcode))
        f.write("\n")
        string = "id = {}, rcx = {}".format(id_mem//2, rcx)
        for i in memory1:
            f.write("{} ".format(i))
        f.write("\n")

        for i in memory:
            f.write("{} ".format(i))
        f.write("\n")

        f.write(string)
        f.write("\n")

        if (opcodes[id_opcode] == 0x1):
            val = (memory[id_mem - 1] << 8) + memory[id_mem - 2]
            string = "id += 1, mem[id - 1] = mem[id - 2]"
            f.write(string)
            f.write("\n")
            id_mem += 2
            memory[id_mem - 1] = (val >> 8)
            memory[id_mem - 2] = (val & 0xff)
            id_opcode += 1
            continue


        if (opcodes[id_opcode] == 0x3):
            f.write("checking")
            f.write("\n")
            val = (memory[id_mem - 1] << 8) + memory[id_mem - 2]
            for i in memory:
                f.write("{} ".format(i))
            f.write("\n")
            if (val == -1):
                id_mem -= 2
                id_opcode += 1
            else:
                break

        if (opcodes[id_opcode] == 0x10):
            f.write("mem[id-2] += mem[id-1], id -= 1\n")
            val = (memory[id_mem - 1] << 8) + memory[id_mem - 2]
            val1 = (memory[id_mem - 3] << 8) + memory[id_mem - 4]
            val = (val + val1) & 0xffff
            memory[id_mem - 3] = (val >> 8) & 0xff
            memory[id_mem - 4] = val & 0xff
            id_mem -= 2
            id_opcode += 1
            continue

        if (opcodes[id_opcode] == 0x11):
            f.write('mem[id - 2] = mem[id - 1] - mem[id - 2], id -= 1')
            f.write("\n")
            val = (memory[id_mem - 1] << 8) + memory[id_mem - 2]
            val = (val - ((memory[id_mem - 3] << 8) + memory[id_mem - 4])) & 0xffff
            id_opcode += 1
            id_mem -= 2
            memory[id_mem - 1] = (val >> 8) & 0xff
            memory[id_mem - 2] = val & 0xff
            continue

        if (opcodes[id_opcode] == 0x12):
            val = (memory[id_mem - 3] << 8) + memory[id_mem - 4]
            val1 = (memory[id_mem - 1] << 8) + memory[id_mem - 2]
            string = "id -= 1, mem[id - 1] *= mem[id]\n"
            f.write(string)
            val *= val1
            id_mem -= 2
            id_opcode += 1
            memory[id_mem - 1] = (val >> 8) & 0xff
            memory[id_mem - 2] = val & 0xff
            continue

        if (opcodes[id_opcode] == 0x13):
            f.write("mem[id-2] = mem[id-1] / mem[id-2], id -= 1\n")
            val = (memory[id_mem - 1] << 8) + memory[id_mem - 2]
            val1 = (memory[id_mem - 3] << 8) + memory[id_mem - 4]
            val = (val // val1) & 0xffff
            id_mem -= 2
            memory[id_mem - 1] = (val >> 8) & 0xff
            memory[id_mem - 2] = val & 0xff
            id_opcode += 1
            continue

        if (opcodes[id_opcode] == 0x14):
            f.write("mem[id-2] = mem[id-1] % mem[id-2], id -= 1\n")
            val = (memory[id_mem - 1] << 8) + memory[id_mem - 2]
            val1 = (memory[id_mem - 3] << 8) + memory[id_mem - 4]
            val = (val % val1) & 0xffff
            id_mem -= 2
            memory[id_mem - 1] = (val >> 8) & 0xff
            memory[id_mem - 2] = val & 0xff
            id_opcode += 1
            continue

        if (opcodes[id_opcode] == 0x15):
            string = "a = (mem[id - 3] * mem[id - 2]) % mem[id - 1], id -= 2, mem[id - 1] = a\n"
            f.write(string)
            val = (memory[id_mem - 3] << 8) + memory[id_mem - 4]
            val1 = (memory[id_mem - 5] << 8) + memory[id_mem - 6]
            id_mem -= 4
            v = (memory[id_mem + 3] << 8) + memory[id_mem + 2]
            val *= val1
            v = val % v
            memory[id_mem - 2] = v & 0xff
            memory[id_mem - 1] = (v >> 8) & 0xff
            id_opcode += 1
            continue

        if (opcodes[id_opcode] == 0x16):
            val = (memory[id_mem - 3] << 8) + memory[id_mem - 4]
            val1 = (memory[id_mem - 1] << 8) + memory[id_mem - 2]
            if (val != val1):
                f.write("mem[id-2] != mem[id-1] => mem[id-2] = 0, id -= 1\n")
                memory[id_mem - 3] = 0
                memory[id_mem - 4] = 0
                id_opcode += 1
                id_mem -= 2
            else:
                f.write("mem[id-2] == mem[id-1] => mem[id-2] = 1, id -= 1\n")
                memory[id_mem - 3] = 0
                memory[id_mem - 4] = 1
                id_opcode += 1
                id_mem -= 2
            continue

        if (opcodes[id_opcode] == 0x17):
            val = (memory[id_mem - 1] << 8) + memory[id_mem - 2]
            if (val < 0):   # good
                string = "mem[id-1] < 0 => mem[id-1] = 0xffff\n"
                f.write(string)
                memory[id_mem - 1] = 0xff
                memory[id_mem - 2] = 0xff
                id_opcode += 1
            elif (val > 0): # bad
                string = "mem[id-1] > 0 => mem[id-1] = 1\n"
                f.write(string)
                memory[id_mem - 1] = 0
                memory[id_mem - 2] = 1
                id_opcode += 1
            else:
                string = "mem[id-1] == 0 => do nothing\n"
                f.write(string)
                id_opcode += 1
            continue

        if (opcodes[id_opcode] == 0x20):
            f.write("read some char, id += 1")
            f.write("\n")
            memory[id_mem] = ord(inp[id_inp])
            id_inp += 1
            id_opcode += 1
            id_mem += 2
            continue

        if (opcodes[id_opcode] == 0x21):
            f.write("print some char, id -= 1")
            f.write("\n")
            val = (memory[id_mem - 1] << 8) + memory[id_mem - 2]
            print(chr(val & 0xff), end = "")
            id_mem -= 2
            id_opcode += 1
            continue

        if (opcodes[id_opcode] == 0x22):
            string = "mem[id] = {}, id += 1".format((opcodes[id_opcode + 2] << 8) + opcodes[id_opcode + 1])
            f.write(string)
            f.write("\n")
            # print("mem[id] = ", (opcodes[id_opcode + 2] << 8) + opcodes[id_opcode + 1],", id += 1")
            memory[id_mem] = opcodes[id_opcode + 1]
            memory[id_mem + 1] = opcodes[id_opcode + 2]
            id_mem += 2
            id_opcode += 3
            continue

        if (opcodes[id_opcode] == 0x30):
            val = (memory[id_mem - 1] << 8) + memory[id_mem - 2]
            val1 = val
            id_mem -= 2
            if (val & 32768 == 1): val = 0xffff
            else: val = 0
            id_opcode = ((val ^ val1) - val) & 0xffff
            f.write("modified id_opcode based on {}, id -= 1".format(val))
            f.write("\n")
            continue

        if (opcodes[id_opcode] == 0x31):
            val = (memory[id_mem - 3] << 8) + memory[id_mem - 4]
            if (val != 0):
                f.write("id_opcode += 1, id = 0")
                f.write("\n")
                id_mem = 0
                id_opcode += 1
            else:
                val = (memory[id_mem - 1] << 8) + memory[id_mem - 2]
                string = "modified id_opcode based on {}, id = 0".format(val)
                f.write(string)
                f.write("\n")
                val1 = val
                id_mem = 0
                if (val & 32768 == 1):
                    val = 0xffff
                else:
                    val = 0
                id_opcode = ((val ^ val1) - val) & 0xffff

            # print('a')
            continue

        if (opcodes[id_opcode] == 0x32):
            check_counter += 1
            print(check_counter)
            val = (memory[id_mem - 3] << 8) + memory[id_mem - 4]
            if (val != 0):
                string = "mem[id - 2] != 0\n"
                f.write(string)
                val = (memory[id_mem - 1] << 8) + memory[id_mem - 2]
                val1 = val
                id_mem -= 2
                if (val & 32768 == 1):
                    val = 0xffff
                else:
                    val = 0
                id_opcode = ((val ^ val1) - val) & 0xffff
                continue
            else:
                string = "mem[id - 2] == 0\n"
                f.write(string)
                f.write("===============================\n")
                if (id_opcode == 11289 or id_opcode == 11403 or id_opcode == 11651 or id_opcode == 11819 or id_opcode == 11933 or id_opcode == 12178): id_mem = 2
                else: id_mem = 0
                id_opcode += 1
                continue

        if (opcodes[id_opcode] == 0x40):
            id_mem -= 2
            memory1[rcx * 2] = memory[id_mem]
            memory1[rcx * 2 + 1] = memory[id_mem + 1]
            f.write("mem1[rcx] = mem[id - 1], id -= 1")
            f.write("\n")
            id_opcode += 1
            continue

        if (opcodes[id_opcode] == 0x41):
            memory[id_mem] = memory1[rcx * 2]
            memory[id_mem + 1] = memory1[rcx * 2 + 1]
            f.write("mem[id] = mem1[rcx], id += 1")
            f.write("\n")
            id_mem += 2
            id_opcode += 1
            # print('a')
            continue

        if (opcodes[id_opcode] == 0x50):
            rcx += 1
            id_opcode += 1
            f.write("rcx += 1")
            f.write("\n")
            continue

        if (opcodes[id_opcode] == 0x52):
            rcx += ((memory[id_mem - 1] << 8) + memory[id_mem - 2])
            f.write("rcx += mem[id-1], id -= 1")
            f.write("\n")
            id_opcode += 1
            id_mem -= 2
            # print('a')
            continue

        if (opcodes[id_opcode] == 0x53):
            f.write("rcx -= mem[id-1], id -= 1")
            f.write("\n")
            rcx = rcx - ((memory[id_mem - 1] << 8) + memory[id_mem - 2])
            id_opcode += 1
            id_mem -= 2
            continue
        # break

        string = "{}, {}\n".format(id_opcode, hex(opcodes[id_opcode]))
        f.write(string)
        print(id_opcode, hex(opcodes[id_opcode]))
        break


vm_parser()

# li = [int(i) for i in "50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 1 2 3 4 5 6 7 8 9 10 48 16 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0".split(' ')]
leak = [i.strip() for i in open('./log.txt', 'r'). readlines()]
start = 37021
pre_num = 0
param = []
instruction = ['0x22', '0x53', '0x41', '0x52', '0x22', '0x32']

while (1):

    t = leak[start][:leak[start].find(',')].strip()
    if (t not in instruction):
        print(t)

    command = leak[start + 4]
    num = ""
    if (command.find('mem[id] = ') != -1 and command.find('mem[id] = mem1[rcx]') == -1):
        # print(command, start)
        # print(leak[start + 4])
        if command.find(' = ') != -1:
            num = command[command.find(' = ')+3:command.find(' = ')+10].strip()
        while (num[len(num) - 1] != ','):
            num = num[:-1]
        num = num[:-1]
        num = int(num)
        if (pre_num != num):
            param.append(num)
            pre_num = num

    if (leak[start + 5].find('=======') != -1):
        print(param)
        param = []
        start += 1
        pre_num = 0
        print()
    # print(start)
    start += 6
    if (start + 4 > len(leak)):
        break
    # print(num)
    # break

#37094