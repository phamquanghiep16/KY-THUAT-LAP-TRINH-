import re   # cho phép người dùng sử dụng các biểu thức chính quy như: kiểm tra số, kiểm tra chữ hoa, kiểm tra ký tự đặc biệt,...
mk = []    # khởi tạo 1 danh sách rỗng
items = [x for x in input("nhập mật khẩu: ").split(',')]

for p in items :
    if len(p)<6 or len(p)>12:
        continue
    
    if not re. search("[a-z]",p):    #if not, elif not: kiểm tra ít nhất
        continue
    elif not re. search("[0-9]",p):
        continue
    elif not re. search("[A-Z]",p):
        continue
    elif not re. search("[$#@]",p):
        continue
    elif re.search("\s",p):           # kiểm tra có khoảng trắng không
        continue
    
    mk.append(p)      #nối các phần tử p trong items lại và thêm vào danh sách rỗng m
    print(",".join(mk))
    print("pham quang hiep")
print("mssv:235752020710015")


    
