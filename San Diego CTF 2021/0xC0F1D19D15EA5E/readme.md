# Challenge

<p align="center">
  <img src="./0xC0F1D_1.png" alt="Entry point"/>
</p>

# Solve

```bash
nguyenguyen753@MochiZou:~/CTF/SDctf/0xC0F1D19D15EA5E$ file 0xC0F1D 
0xC0F1D: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=7f973de2918f3c6fd2df19e4a3b751eba9ecf577, for GNU/Linux 3.2.0, stripped
```

Mở IDA xem sơ qua chương trình thử:

<p align="center">
  <img src="./0xC0F1D_2.png" alt="Entry point"/>
</p>

Đầu tiên hàm sẽ lấy `environment variable` tên `MASK_ON`, sau đó sẽ kiểm tra:
  - Chuỗi vừa lấy có độ dài là 4
  - Sau khi MD5 hash thì phải ra giá trị như `unk_55829C0381C0`

Vì độ dài chỉ là 4 nên mình đã bruteforce ra kết quả là `true`, vậy ta set biến:

<p align="center">
  <img src="./0xC0F1D_3.png" alt="Entry point"/>
</p>

Như ta thấy thì nếu không set biến `MASK_ON=true` thì chương trình sẽ không chạy. Ta nhập thử chương trình:

<p align="center">
  <img src="./0xC0F1D_4.png" alt="Entry point"/>
</p>

Và đương nhiên là chương trình đã kick mình đi vì mình khá xàm

Nhưng khi nhìn vào IDA, mình thấy có hàm `BUG()` rất lạ, nhấn vào thì không hiển thị gì cả. Đành phải chuyển sang Assembly để xem tiếp:

<p align="center">
  <img src="./0xC0F1D_5.png" alt="Entry point"/>
</p>

Cái hàm `BUG()` lúc nãy chình là cái `ud2` như trong hình. Lúc này mình nghi ngờ rằng đây là một cái giống `try .. catch` trong python, nghĩa là nếu có xảy ra lỗi gì ngoài ý muốn thì chương trình sẽ chuyển luồng sang chỗ khác, lúc này chỉ có cách debug thì mình mới biết chuyện gì xảy ra.

