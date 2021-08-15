## Do sắp thi học kì nên mình không có viết wu, mà chỉ tóm tắt cách giải.

# find_plut0
Bài này đưa vào z3. Nhưng lưu ý biểu thức cuối cùng xài logical shfit right. nếu xài dấu `>>` có thể sẽ dẫn đến sai kết quả. Tham khảo tại đây: [https://stackoverflow.com/questions/25532563/why-does-z3-say-that-this-equation-is-not-satisfiable-when-i-have-input-that-is](https://stackoverflow.com/questions/25532563/why-does-z3-say-that-this-equation-is-not-satisfiable-when-i-have-input-that-is)

# REplica
Bài này sẽ swap thứ tự input và so sánh với string file cho.

# Miz
Graph Traversal trên ma trận, chi tiết hơn thì mình xài bfs.

# flagchecker
2 layers VM. Bài này có 2 hàm check, hàm check thứ nhất sẽ mod kí tự của mình cho 9 và so sánh với mảng hằng đã cho. check thứ 2 là một VM khác, sẽ encrypt input thành một dãy số, không thể reverse được đoạn check này, nên có thể nói đây là một hàm băm. Nên hàm check thứ 2 mình sẽ bruteforce dựa trên set kí tự của check 1 để tìm ra các kí tự cuối cùng.

# Noodes
Bài này sẽ tạo ra một đống file và một đống directory. Sau đó cho chương trình theo dõi hành vi của chúng ta lên các file. Giả sử nếu ta chọn xoá file hay thay đổi file, chương trình sẽ ghi lại trong bộ nhớ. Chúng ta phải thực hiện các chuỗi hành vi đó đúng thứ tự đề cho thì server sẽ nhả flag. Quan trọng rằng kết quả đã giấu đi một vài process flow nên việc tìm ra kết quả cuối cùng khá khó khăn. Cần phải debug cho kĩ đoạn này mới hiểu thực sự cách hoạt động quá trình giám sát hành vi các file của program.