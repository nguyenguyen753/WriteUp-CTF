# Đề bài:
[simple_re.jpg](https://drive.google.com/file/d/15kISiVpwJ74jUE6HqoaHHRA-SMTN7XYK/view?usp=sharing)

# Cách làm:

```bash
$ file simple_re.jpg      
simple_re.jpg: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=33cacc9c4e24e18b6b3e8807a3e8870cbe347ff1, stripped
```

### Chạy thử chương trình:
```bash
$ ./simple_re.jpg       
 _____ _                 _       ______ _____ 
/  ___(_)               | |      | ___ \  ___|
\ `--. _ _ __ ___  _ __ | | ___  | |_/ / |__  
 `--. \ | '_ ` _ \| '_ \| |/ _ \ |    /|  __| 
/\__/ / | | | | | | |_) | |  __/ | |\ \| |___ 
\____/|_|_| |_| |_| .__/|_|\___| \_| \_\____/ 
                  | |                         
                  |_|                         

Input flag: MOCHIZOUUUUUUUU
Incorrect!
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

Có vẻ ta thấy được đoạn chương trình cần tìm trong source code. Nhưng khi đưa vào IDA để debug thử thì mình có một phát hiện khác:
![alt text](https://github.com/nguyenguyen753/WriteUp-CTF/blob/main/WannaOne/Simple%20RE/simple_re.png)
Nếu để ý kĩ thì `xor eax eax` sẽ clear thanh ghi `eax`, tức là `eax = 0`, `div eax` sẽ lấy `eax / eax`, điều này là không thể vì `eax` lúc nào cũng sẽ = 0. Khi quan sát trong lúc debug, ta sẽ thấy chương trình sẽ bị nhảy đến một function khác vì gặp lỗi này.
```C++
void FUN_004007f6(void)

{
  ulong uVar1;
  undefined8 *puVar2;
  undefined8 *puVar3;
  byte bVar4;
  int local_24;
  int local_20;
  __pid_t local_1c;
  undefined8 *local_18;
  uint local_c;
  
  bVar4 = 0;
  local_18 = (undefined8 *)mmap((void *)0x0,0x400,7,0x21,-1,0);
  if (local_18 == (undefined8 *)0xffffffffffffffff) {
                    /* WARNING: Subroutine does not return */
    exit(1);
  }
  local_1c = fork();
  if (local_1c < 0) {
                    /* WARNING: Subroutine does not return */
    exit(1);
  }
  if (local_1c == 0) {
    local_c = 0;
    while (local_c < 0x11a) {
      *(byte *)((long)&DAT_006020e0 + (long)(int)local_c) =
           *(byte *)((long)&DAT_006020e0 + (long)(int)local_c) ^ 1;
      local_c = local_c + 1;
    }
    *local_18 = DAT_006020e0;
    *(undefined8 *)((long)local_18 + 0x112) = DAT_006021f2;
    puVar2 = (undefined8 *)
             ((long)local_18 - (long)(undefined8 *)((ulong)(local_18 + 1) & 0xfffffffffffffff8));
    uVar1 = (ulong)((int)puVar2 + 0x11aU >> 3);
    puVar2 = (undefined8 *)((long)&DAT_006020e0 - (long)puVar2);
    puVar3 = (undefined8 *)((ulong)(local_18 + 1) & 0xfffffffffffffff8);
    while (uVar1 != 0) {
      uVar1 = uVar1 - 1;
      *puVar3 = *puVar2;
      puVar2 = puVar2 + (ulong)bVar4 * -2 + 1;
      puVar3 = puVar3 + (ulong)bVar4 * -2 + 1;
    }
    munmap(local_18,0x400);
  }
  else {
    waitpid(local_1c,&local_24,0);
    if (local_24 == 0) {
      local_20 = (*(code *)local_18)(&DAT_00602210);
      if (local_20 == 0) {
        puts("Incorrect!");
      }
      else {
        printf("Correct! Flag: %s\n",&DAT_00602210);
      }
    }
    munmap(local_18,0x400);
  }
                    /* WARNING: Subroutine does not return */
  exit(0);
}
```
Đây mới chính là đoạn chương trình sẽ kiểm tra flag của chúng ta.
Tóm lại, đoạn chương trình chính kia sẽ dẫn chúng ta tới 1 fake flag nếu như các bạn dùng static analysis, đoạn chương trình khi gặp lỗi sẽ dẫn chúng ta tới đúng đoạn chương trình mình cần. Bây giờ chúng ta chỉ cần debug để tìm flag.
### Tìm flag:
Debug tiếp, ta tới các đoạn chương trình sau:

![alt_text](https://github.com/nguyenguyen753/WriteUp-CTF/blob/main/WannaOne/Simple%20RE/175940674_1188650554904800_7375870996476900416_n.png)

Đi vô đoạn chương trình của thanh ghi `rdx`:

![alt_text](https://github.com/nguyenguyen753/WriteUp-CTF/blob/main/WannaOne/Simple%20RE/simple_re1.png)

Đoạn chương trình tiếp theo sẽ là mấu chốt của vấn đề lấy được flag như thế nào

![alt_text](https://github.com/nguyenguyen753/WriteUp-CTF/blob/main/WannaOne/Simple%20RE/abc.png)

Đoạn chương trình này sẽ xor 2 buffer WannaOne và buffer được tạo ra từ những byte ngẫu nhiên từ đoạn chương trình ta đã thấy

~[alt_text](https://github.com/nguyenguyen753/WriteUp-CTF/blob/main/WannaOne/Simple%20RE/flag.png)

`Flag: flag{4maz1ng_y0u_g0t_1t!!!!!}`
