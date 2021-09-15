# Challenge

# File: [ncore_tb.v](./ncore_tb.v) [server.py](./server.py)

# Solve:

```python
import os
import shutil
import subprocess

def main():
    print("WELCOME")
    txt = input()
    print(txt)
    addr = os.environ.get("SOCAT_PEERADDR")
    if(os.path.exists(addr)):
        shutil.rmtree(addr)
    os.mkdir(addr)
    shutil.copy("flag.hex",f"{addr}/flag.hex")
    shutil.copy("nco",f"{addr}/nco")
    ramf = open(f"{addr}/ram.hex","w")
    ramf.write(txt)
    ramf.close()
    p = subprocess.Popen(["vvp","nco"],stdout=subprocess.PIPE,cwd=f"./{addr}")
    out = p.communicate()[0]
    print(out)
    shutil.rmtree(addr)
    return

if __name__ == "__main__":
    main()
```

Mở file `server.py` lên thì ta có thể hiểu chương trình nhận input của ta và lưu vào file **ram.hex**, rồi sau đó chạy file **Verilog**.
Mặc dù mình chưa bao giờ RE verilog, nhưng may mắn là chương trình khá dễ hiểu nên không cần tìm hiểu quá nhiều.

```bash
  `define ADD  4'd0
  `define SUB  4'd1
  `define AND  4'd2
  `define OR   4'd3
  `define RES 4'd4
  `define MOVF 4'd5
  `define MOVT 4'd6
  `define ENT  4'd7
  `define EXT  4'd8 
  `define JGT  4'd9
  `define JEQ  4'd10
  `define JMP  4'd11
  `define INC  4'd12
  `define MOVFS 4'd13
```

Đoạn này sẽ `Define` mỗi opcode thành 1 số

```bash
  reg [7:0] safe_rom [0:255];
  reg [7:0] ram [0:255];
  reg [31:0] regfile [0:3];
  reg [31:0] key [0:0];
  reg emode;
  wire [3:0] opcode;
  integer pc = 0;
  // assign opcode = ram[pc][3:0];
  reg clk = 0;
  // file descriptors
  int       read_file_descriptor;
  // memory
  logic [7:0] mem [15:0];
```

Đoạn này chỉ khởi tạo các biến để phục vụ cho việc thực thi chương trình.

```bash
  task increment_pc();
    pc = pc + 2;
  endtask
```

Hàm chỉ tăng biến `pc` lên 2 đơn vị.

```bash
  task load_safeROM();
    $display("loading safe rom, safely...");
    $readmemh("flag.hex",safe_rom);
  endtask
```

Hàm đọc flag.

```bash
  task load_ram();
    $display("loading user controlled memory...");
    $readmemh("ram.hex",ram);
  endtask
```

Hàm đọc input.

```bash
  task open_file();
    $display("Opening file");
    read_file_descriptor=$fopen("flag.txt","rb");
  endtask
```

Hàm này để mở file `flag.txt`.

```bash
  task set_key();
    int tmp;
    // key[0] = 0;
    read_file_descriptor=$fopen("/dev/urandom","rb");
    tmp = $fread(key, read_file_descriptor);
    $readmemh("/dev/urandom",key);
  endtask
```

Hàm để random key.

```bash
  task print_res();
    integer i;
    for( i=0; i<64; i = i + 1) begin
      $write("%h ",ram[255-i]);
    end
    $write("\n");
  endtask
```

Hàm này in ra kết quả của mảng `ram`.

```bash
  task init_regs();
    integer i = 0;
    for(i = 0; i<4; i++) begin
      regfile[i] = 32'd0;
    end
  endtask
```

Khởi tạo mảng `regfile` bằng 0.  
Sau đó là đoạn xử lí opcodes mà chúng ta input vào.  
Tới đây chúng ta đã hiểu cách làm, giờ mình chỉ việc dựng lại trên local để debug. Mình cài **iverilog** và đã sửa lại file `ncore_tb.` vì file này ngay từ đầu đã có sai sót về syntax.  
Sau nhiều thời gian debug thì minh đã tạo ra 2 payload để gửi lên server và lấy 2 phần của flag để ghép lại (Đoạn tạo payload các bạn có thể tự tạo, do payload mình viết khá dở hơi)

`flag{d0nT_mESs_wiTh_tHe_sChLAmi}`