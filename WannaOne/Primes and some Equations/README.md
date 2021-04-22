# Đề bài:
`Description: I have been lonely for a long time because I only spent most of the time on doing maths and analyzing the primes . So today I decide to find my lover. How about you? Who is your destiny? Maybe, cracking this challenge will help you find out the answer.`
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