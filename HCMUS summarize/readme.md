# Sanity Check
Base 32 => Base 64 => Caesar

# Faded
PyInstaller extractor + Decompyle3

# mixed_vm
Một bài virtual machine obfuscation. Ngồi dò opcodes, ta thấy mỗi một đoạn kí tự thực hiện 2 bước xor và plus và so sánh với các dãy số có sẵn.

# AndroidRev
Flag gồm 5 từ, mỗi từ được hash thành mã md5, sau đó lên mạng mình dò hash md5 trên database và từ từ nối lại thành flag

# EscapeMe
`sudo -l` cho ta biết ta có thể xài python3, sau đó `sudo python -c 'import os; os.system("/bin/sh")'` và `cat flag.txt`

# WeirdProtocol
File PE sẽ tạo ra một file PE khác và kết nối vào để kiểm tra input, một hồi xem xét thì ta biết rằng file PE dùng mã SHA256 để kiểm tra input, lên mạng dò ta ra được chuỗi `hello`

# CrackMe
SHA256-Crypt + rsa, xài hashcat

# Maquerade
một file mp3, một file java class và 1 file zip. file mp3 ra mật khẩu `pwd785$`, còn cái java class crack sẽ cho ra `897268$}`, và ta có được flag

# SaveMe
Đảo từng cặp byte kề nhau, sau đó `xxd -r` cho ra file hình kèm flag