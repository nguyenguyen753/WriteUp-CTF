a = "r27 = 16, r60 = 39, r59 = 3, r7 = 1, r51 = 12, r42 = 16, r16 = 19, r23 = 5, r35 = 73, r39 = 13, r15 = 3, r63 = 42, r18 = 9, r57 = 0, r45 = 50, r26 = 1, r0 = 22, r12 = 5, r6 = 0, r48 = 3, r9 = 1, r46 = 20, r53 = 67, r54 = 60, r3 = 2, r2 = 10, r43 = 0, r20 = 0, r28 = 2, r62 = 6, r4 = 12, r37 = 75, r5 = 5, r8 = 24, r29 = 44, r61 = 41, r33 = 10, r22 = 8, r52 = 65, r31 = 39, r47 = 19, r10 = 2, r55 = 38, r38 = 18, r50 = 48, r14 = 4, r21 = 39, r41 = 2, r1 = 4, r30 = 36, r36 = 79, r49 = 9, r17 = 21, r58 = 5, r56 = 2, r44 = 3, r40 = 7, r34 = 4, r32 = 1, r25 = 3, r24 = 5, r19 = 1, r13 = 8, r11 = 7".split(', ') 
ans = ""
li = []
for i in range(64):
    for string in a:
        if string.find('r{} ='.format(str(i))) != -1:
            li.append(int(string.split(' = ')[1]))
            ans += chr(int(string.split(' = ')[1]) + 0x2f)
            break

print(ans)