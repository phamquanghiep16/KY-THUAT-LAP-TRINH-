#yêu cầu người dùng nhập vào một chuỗi ký tự từ bàn phím, lưu vào biến str 
an= input ("Enter a String: ")

#khởi tạo một thư viện dictionary rỗng
dict = {}
for n in an :
    if n in dict:
        dict[n] += 1
    else:
        dict[n] = 1
print(dict)
print("pham quang hiep")
print("mssv:235752020710015")
# chương trình đếm số ký tự xuất hiện trong chuỗi
# thêm lần lượt các ký tự trong biến an vào từ điển, nếu phát hiện ký tự đó đã có trong từ điển rồi thì +1, nếu không thì =1
