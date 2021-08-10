# Tóm tắt các lời giải của các challenge

## verybabyrev
Sử dụng phép xor cơ bản để kiểm tra input của chúng ta.

## Dotty
Đây là mã morse, đưa vào [https://morsecode.world/international/translator.html](https://morsecode.world/international/translator.html), decode và đưa vào base32 decoder để giải mã.

## RaRPG
Hack đi xuyên tường để nhận flag

## Infinite Free Trial
Bài này sẽ check input của ta bằng 2 lần encryption. Encryption thứ nhất ta không đủ thông tin để reverse nên ta qua encryption thứ 2 thì ta hoàn toàn có đủ thông tin để khôi phục lại input ban đầu cũng chính là flag.

## Very TriVial ReVersing
Hình như sử dụng ngôn ngữ Golang hay gì đó mình không rõ, bài này sẽ encrypt input bằng cách: `((input[i] - 0x37) ^ 0x13) & 0xff` nếu i là vị trí chẵn và `((input[i] - 0x13) ^ 0x37) & 0xff` nếu i là vị trí lẻ (mảng input là base 0)

## boring flag checker
Một bài VM obfuscation. Viết script để mô tả luồng thực thi chương trình và quan sát bộ nhớ để đoán cách kiểm tra flag. Chi tiết ở [bài post này](https://mochinishimiya.github.io/2021/08/09/rarctf-2021.html)

## Down The Rabbit Hole
Một bài self-modified code và sử dụng rất nhiều `fork()`. Cần phải hiểu rõ luồng chương trình trước khi debug. Chi tiết ở [bài post này](https://mochinishimiya.github.io/2021/08/09/rarctf-2021.html)