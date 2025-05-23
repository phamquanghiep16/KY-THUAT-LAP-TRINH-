# fibonacci là một chuỗi số trong đó mỗi số là tổng của hai số liền trước nó
a, b = 1, 2
total = 0

print(a, end=" ")  # In số Fibonacci đầu tiên

while a <= 4000000-1:
    if a % 2 == 0:   #nếu a là chẵn thì cộng vào biến total
        total += a
    print(a, end=" ")  # In số hiện tại trước khi cập nhật, end=" ": không xuống dòng mà thay vào đó là một khoảng trắng
    a, b = b, a + b  # Cập nhật giá trị Fibonacci

print("\nSum of even Fibonacci numbers:", total)  # Chỉnh lại thông báo in
print("pham quang hiep")
print("mssv:235752020710015")
