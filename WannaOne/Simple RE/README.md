# Đề bài:
[simple_re.jpg](https://drive.google.com/file/d/15kISiVpwJ74jUE6HqoaHHRA-SMTN7XYK/view?usp=sharing)

# Cách làm:

```bash
$ file simple_re.jpg      
simple_re.jpg: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=33cacc9c4e24e18b6b3e8807a3e8870cbe347ff1, stripped
```
### Ghidra
```C++
undefined8 FUN_0040097c(void)

{
  byte bVar1;
  size_t sVar2;
  long lVar3;
  ulong uVar4;
  undefined8 *puVar5;
  undefined8 *puVar6;
  undefined local_248 [160];
  undefined8 local_1a8;
  int local_20;
  int local_1c;
  
  lVar3 = 0x30;
  puVar5 = (undefined8 *)
                      
           " _____ _                 _       ______ _____ \n/  ___(_)               | |      | ___\\  ___|\n\\ `--. _ _ __ ___  _ __ | | ___  | |_/ / |__  \n `--. \\ | \'_ ` _ \\| \'_\\| |/ _ \\ |    /|  __| \n/\\__/ / | | | | | | |_) | |  __/ | |\\ \\| |___\n\\____/|_|_| |_| |_| .__/|_|\\___| \\_| \\_\\____/ \n                  | |                        \n                  |_|                         \n\nInput flag: "
  ;
  puVar6 = &local_1a8;
  while (lVar3 != 0) {
    lVar3 = lVar3 + -1;
    *puVar6 = *puVar5;
    puVar5 = puVar5 + 1;
    puVar6 = puVar6 + 1;
  }
  *(undefined4 *)puVar6 = *(undefined4 *)puVar5;
  *(undefined2 *)((long)puVar6 + 4) = *(undefined2 *)((long)puVar5 + 4);
  printf((char *)&local_1a8,puVar5,(long)puVar6 + 6);
  local_248._0_8_ = FUN_004007f6;
  sigemptyset((sigset_t *)(local_248 + 8));
  local_248._136_4_ = 0;
  sigaction(8,(sigaction *)local_248,(sigaction *)0x0);
  __isoc99_scanf(&DAT_00400be6,&DAT_00602210);
  local_1c = 0;
  while (uVar4 = SEXT48(local_1c), sVar2 = strlen(&DAT_006020b0), uVar4 < sVar2) {
    bVar1 = (&DAT_006020b0)[local_1c];
    uVar4 = SEXT48(local_1c);
    sVar2 = strlen(s_WannaOne_006020a0);
    (&DAT_006020b0)[local_1c] = bVar1 ^ s_WannaOne_006020a0[uVar4 % sVar2];
    local_1c = local_1c + 1;
  }
  local_20 = 0;
  while( true ) {
    uVar4 = SEXT48(local_20);
    sVar2 = strlen(&DAT_006020b0);
    if (sVar2 <= uVar4) {
      printf("Correct! Flag: %s\n",&DAT_00602210);
      return 0;
    }
    if ((&DAT_00602210)[local_20] != (&DAT_006020b0)[local_20]) break;
    local_20 = local_20 + 1;
  }
  puts("Incorrect!");
  return 0;
}
```
