# Đề bài:

Description: I have been lonely for a long time because I only spent most of the time on doing maths and analyzing the primes . So today I decide to find my lover. How about you? Who is your destiny? Maybe, cracking this challenge will help you find out the answer.
[chall](https://drive.google.com/file/d/1WqOovtZdNMK1LHiHcGPGS0FiKxrKWdu5/view?usp=sharing)

# Cách làm:

```bash
$ file chall        
chall: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=64a06ea29860338c775a15fbce339e7bd97ec26c, for GNU/Linux 3.2.0, not stripped
```

### Chạy chương trình:

```bash
$ ./chall 12345

Try again!
```

Xài ghidra để xem code:

### Ghidra

```C++
undefined8 main(int param_1,long param_2)

{
  int iVar1;
  int iVar2;
  undefined8 uVar3;
  size_t sVar4;
  void *pvVar5;
  int local_14;
  uint local_10;
  int local_c;
  
  if (param_1 < 2) {
    uVar3 = 0xffffffff;
  }
  else {
    sVar4 = strlen(*(char **)(param_2 + 8));
    iVar1 = (int)sVar4;
    pvVar5 = malloc((long)iVar1);
    local_c = 0;
    while (local_c < iVar1) {
      *(undefined *)((long)pvVar5 + (long)local_c) = 0;
      local_c = local_c + 1;
    }
    local_10 = 0;
    while ((int)local_10 < iVar1) {
      if ((local_10 & 1) == 0) {
        *(byte *)((long)pvVar5 + (long)(int)local_10) =
             (*(byte *)((long)(int)local_10 + *(long *)(param_2 + 8)) ^ 0x13) & 0x7f;
      }
      else {
        *(byte *)((long)pvVar5 + (long)(int)local_10) =
             (*(byte *)((long)(int)local_10 + *(long *)(param_2 + 8)) ^ 0x37) & 0x7f;
      }
      local_10 = local_10 + 1;
    }
    local_14 = 0;
    while (local_14 < iVar1) {
      iVar2 = checkEachEleOfInput((int)*(char *)((long)pvVar5 + (long)local_14),local_14,local_14);
      if (iVar2 == -1) {
        puts("\nTry again!");
        return 0xffffffff;
      }
      local_14 = local_14 + 1;
    }
    puts("\nCongratulation, you entered the right flag!");
    uVar3 = 0;
  }
  return uVar3;
}

```

Nhìn sơ đoạn chương trình thì, hàm `checkEachEleOfInput()` là hàm ta sẽ quan tâm nhất trong bài này, hàm lấy từng số trong input và kiểm tra xem có thoả mãn điều kiện trong hàm hay không, nếu không thoả chương trình sẽ thoát ra, nếu thoả hết thì sẽ dẫn chúng ta tới flag. Mở hàm này trong ghidra ta xem tiếp:

```C++
int * checkEachEleOfInput(char param_1,int param_2)

{
  int iVar1;
  uint uVar2;
  uint *puVar3;
  uint *puVar4;
  int *piVar5;
  int *piVar6;
  int local_20;
  int local_1c;
  int local_18;
  uint local_14;
  int local_10;
  int local_c;
  
  iVar1 = (int)(char)arr2[param_2];
  puVar3 = (uint *)malloc((long)iVar1);
  puVar4 = (uint *)malloc((long)iVar1);
  local_c = 0;
  while (local_c < iVar1) {
    puVar3[local_c] = 0;
    puVar4[local_c] = 0;
    local_c = local_c + 1;
  }
  local_10 = 0;
  local_14 = SEXT14(param_1);
  local_18 = 0;
  while (local_18 < num) {
    uVar2 = SEXT14((char)arr1[local_18]);
    if (local_14 % uVar2 == 0) {
      puVar3[local_10] = uVar2;
      while (local_14 % uVar2 == 0) {
        local_14 = local_14 / uVar2;
        puVar4[local_10] = puVar4[local_10] + 1;
      }
      local_10 = local_10 + 1;
    }
    local_18 = local_18 + 1;
  }
  piVar5 = (int *)malloc((long)iVar1);
  piVar6 = (int *)malloc((long)iVar1);
  if (iVar1 == 3) {
    *piVar5 = *puVar3 + puVar3[1];
    piVar5[1] = puVar3[2] + *puVar3;
    piVar5[2] = puVar3[2] + puVar3[1];
    *piVar6 = *puVar4 + puVar4[1];
    piVar6[1] = puVar4[2] + *puVar4;
    piVar6[2] = puVar4[2] + puVar4[1];
    local_1c = 0;
    while (local_1c < 3) {
      if ((piVar5[local_1c] !=
           *(int *)(three_values_arr0 + ((long)param_2 * 3 + (long)local_1c) * 4)) ||
         (piVar6[local_1c] != *(int *)(three_values_arr1 + ((long)param_2 * 3 + (long)local_1c) * 4)
         )) {
        return (int *)0xffffffff;
      }
      local_1c = local_1c + 1;
    }
    piVar6 = (int *)0x1;
  }
  else {
    if (iVar1 == 2) {
      *piVar5 = *puVar3 + puVar3[1];
      piVar5[1] = puVar3[1] * 0x539 + *puVar3;
      *piVar6 = *puVar4 + puVar4[1];
      piVar6[1] = puVar4[1] * 0x539 + *puVar4;
      local_20 = 0;
      while (local_20 < 2) {
        if ((piVar5[local_20] !=
             *(int *)(two_values_arr0 + ((long)param_2 * 2 + (long)local_20) * 4)) ||
           (piVar6[local_20] != *(int *)(two_values_arr1 + ((long)param_2 * 2 + (long)local_20) * 4)
           )) {
          return (int *)0xffffffff;
        }
        local_20 = local_20 + 1;
      }
      piVar6 = (int *)0x1;
    }
    else {
      if (iVar1 == 1) {
        if (((*puVar3 ^ 0x1337) == *(uint *)(one_value_arr0 + (long)param_2 * 4)) &&
           ((*puVar4 ^ 0x1337) == *(uint *)(one_value_arr1 + (long)param_2 * 4))) {
          piVar6 = (int *)0x1;
        }
        else {
          piVar6 = (int *)0xffffffff;
        }
      }
    }
  }
  return piVar6;
}
```

Ta sẽ phân tích từng đoạn:

```C++
  iVar1 = (int)(char)arr2[param_2];
  puVar3 = (uint *)malloc((long)iVar1);
  puVar4 = (uint *)malloc((long)iVar1);
  local_c = 0;
  while (local_c < iVar1) {
    puVar3[local_c] = 0;
    puVar4[local_c] = 0;
    local_c = local_c + 1;
  }
```

Khởi tạo 2 mảng `puVar3`, `puVar4`, `iVar1` có vẻ là số lượng phần tử của 2 mảng `puVar3` và `puVar4`, `iVar1` lấy giá trị từ mảng `arr2`, ta thử xem giá trị của mảng `arr2`:

![alt_text](https://github.com/nguyenguyen753/WriteUp-CTF/blob/main/WannaOne/Primes%20and%20some%20Equations/prime1.png)

Tiếp tục đoạn chương trình tiếp theo:

```C++
  local_10 = 0;
  local_14 = SEXT14(param_1);
  local_18 = 0;
  while (local_18 < num) {
    uVar2 = SEXT14((char)arr1[local_18]);
    if (local_14 % uVar2 == 0) {
      puVar3[local_10] = uVar2;
      while (local_14 % uVar2 == 0) {
        local_14 = local_14 / uVar2;
        puVar4[local_10] = puVar4[local_10] + 1;
      }
      local_10 = local_10 + 1;
    }
    local_18 = local_18 + 1;
  }
```

Phân tích sâu hơn, ta hiểu rằng đoạn chương trình này sẽ phân tích từng số trong input của ta ra thành các thừa số nguyên tố. Mảng `puVar4` chính là mảng lưu số mũ của các thừa số nguyên tố, còn `puVar3` là mảng thừa số nguyên tố. Ta tiếp tục phân tích đoạn chương trình tiếp theo:

```C++
  piVar5 = (int *)malloc((long)iVar1);
  piVar6 = (int *)malloc((long)iVar1);
  if (iVar1 == 3) {
    *piVar5 = *puVar3 + puVar3[1];
    piVar5[1] = puVar3[2] + *puVar3;
    piVar5[2] = puVar3[2] + puVar3[1];
    *piVar6 = *puVar4 + puVar4[1];
    piVar6[1] = puVar4[2] + *puVar4;
    piVar6[2] = puVar4[2] + puVar4[1];
    local_1c = 0;
    while (local_1c < 3) {
      if ((piVar5[local_1c] !=
           *(int *)(three_values_arr0 + ((long)param_2 * 3 + (long)local_1c) * 4)) ||
         (piVar6[local_1c] != *(int *)(three_values_arr1 + ((long)param_2 * 3 + (long)local_1c) * 4)
         )) {
        return (int *)0xffffffff;
      }
      local_1c = local_1c + 1;
    }
    piVar6 = (int *)0x1;
  }
  else {
    if (iVar1 == 2) {
      *piVar5 = *puVar3 + puVar3[1];
      piVar5[1] = puVar3[1] * 0x539 + *puVar3;
      *piVar6 = *puVar4 + puVar4[1];
      piVar6[1] = puVar4[1] * 0x539 + *puVar4;
      local_20 = 0;
      while (local_20 < 2) {
        if ((piVar5[local_20] !=
             *(int *)(two_values_arr0 + ((long)param_2 * 2 + (long)local_20) * 4)) ||
           (piVar6[local_20] != *(int *)(two_values_arr1 + ((long)param_2 * 2 + (long)local_20) * 4)
           )) {
          return (int *)0xffffffff;
        }
        local_20 = local_20 + 1;
      }
      piVar6 = (int *)0x1;
    }
    else {
      if (iVar1 == 1) {
        if (((*puVar3 ^ 0x1337) == *(uint *)(one_value_arr0 + (long)param_2 * 4)) &&
           ((*puVar4 ^ 0x1337) == *(uint *)(one_value_arr1 + (long)param_2 * 4))) {
          piVar6 = (int *)0x1;
        }
        else {
          piVar6 = (int *)0xffffffff;
        }
      }
    }
  }
```

Đoạn này khá dài, nhưng tóm tắt lại rằng đoạn này chính là đoạn chương trình dùng để so sánh điều kiện của flag, mảng `arr2` được nói ở trên chính là mảng chứa số lượng thừa số nguyên tố của từng kí tự trong flag, sau khi đã được đổi ra ASCII và phân tích thừa số nguyên tố. Khi tới đây, ta đã mường tượng được cách làm bài, từ đó ta sẽ viết script để dẫn chúng ta đến flag cuối cùng:

### Script.py

```Python
sizeInt = [2, 2, 3, 2, 2, 2, 3, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 1, 2, 2, 2]

oneValuePrime = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x1334, 0, 0, 0x1335, 0, 0x1335, 0, 0, 0, 0, 0]
oneValueExpo = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0x1333, 0, 0, 0x1332, 0, 0x1332, 0, 0, 0]

twoValuePrime = [0x10, 0x43E8, 0x14, 0x43EC, 0, 0, 7, 0x1A1F, 0xF, 0x43E7, 9, 0x2491, 0, 0, 0xE, 0x3976, 0x15, 0x633D, 5, 0xFAD, 0x15, 0x633D, 0xF, 0x43E7, 0, 0, 0x1A, 0x7822, 0x15, 0x633D, 0x14, 0x43EC, 0xC, 0x2494, 0x12, 0x43EA, 0x3D, 0x13425, 0x1A, 0x7822, 0x15, 0x633D, 0, 0, 0xC, 0x2494, 0x1A, 0x7822, 0, 0, 0x12, 0x43EA, 0, 0, 0x1A, 0x7822, 0xD, 0x3975, 0x27, 0xC13F, 0, 0, 0, 0]
twoValueExpo = [3, 0x53B, 2, 0x53A, 0, 0, 5, 0x53D, 4, 0x53C, 3, 0x0A73, 0, 0, 3, 0x53B, 3, 0x53B, 2, 0x53A, 2, 0x53A, 4, 0x53C, 0, 0, 2, 0x53A, 3, 0x53B, 2, 0x53A, 2, 0x53A, 2, 0x53A, 2, 0x53A, 2, 0x53A, 3, 0x53B, 0, 0, 2, 0x53A, 2, 0x53A, 0, 0, 2, 0x53A, 0, 0, 2, 0x53A, 3, 0x53B, 2, 0x53A, 0, 0, 0, 0]

threeValuePrime = [0, 0, 0, 0, 0, 0, 5, 0x15, 0x16, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 7, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0x13, 0x14, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
threeValueExpo = [0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

res = []

for i in range(30):
	res.append(0)

for i in range(len(sizeInt)):
	k = 0
	if sizeInt[i] == 1:
		prime = oneValuePrime[i] ^ 0x1337
		exponent = oneValueExpo[i] ^ 0x1337
		k = int(pow(prime, exponent))

	if sizeInt[i] == 2:
		p1 = (twoValuePrime[i*2 + 1] - twoValuePrime[i*2]) // 1336
		p0 = twoValuePrime[i*2] - p1
		e1 = (twoValueExpo[i*2 + 1] - twoValueExpo[i*2]) // 1336
		e0 = twoValueExpo[i*2] - e1
		# print(p1, e1, p0, e0)
		# break
		k = int(pow(p0, e0)) * int(pow(p1, e1))

	if sizeInt[i] == 3:
		v1 = threeValuePrime[i*3]
		v2 = threeValuePrime[i*3 + 1]
		v3 = threeValuePrime[i*3 + 2]

		p2 = (v2 - v1 + v3) // 2
		p1 = v3 - p2
		p0 = v1 - p1

		v1 = threeValueExpo[i*3]
		v2 = threeValueExpo[i*3 + 1]
		v3 = threeValueExpo[i*3 + 2]

		e2 = (v2 - v1 + v3) // 2
		e1 = v3 - e2
		e0 = v1 - e1

		k = int(pow(p0, e0) * pow(p1, e1) * pow(p2, e2))

	if (i % 2 == 0):
		res[i] = k ^ 0x13
	else:
		res[i] = k ^ 0x37

for i in res:
	print(chr(i), end='')
```

`Flag: flag{UIT_15_ur_l0ver_f0r3v3r?}`