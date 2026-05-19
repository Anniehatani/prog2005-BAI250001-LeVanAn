#BAI 1
print ("BAI 1:")
so_nguyen = 5
print("Số nguyên:", so_nguyen)
so_thuc = 3.14
print("Số thực:", so_thuc)
chuoi = "Annie"
print("Chuỗi ký tự:", chuoi)
print ("\n")

#BAI 2
print ("BAI 2:")
pi = 3.14
r = 5
chu_vi = 2 * pi * r
print ("Số pi \u2248 ", pi)
print ("Bán kính hình tròn =", r)
print ("Chu vi hình tròn: 2 x r x pi \u2248 {:.2f}".format(chu_vi))
print ("\n")

#BAI3
print ("BAI 3:")
a = int(input("Nhập số nguyên thứ nhất: "))
b = int(input("Nhập số nguyên thứ hai: "))
print("Phép cộng 2 số =", a + b)
print("Phép trừ 2 số =", a - b)
print("Phép nhân 2 số =", a * b)
print("Phép chia 2 số = {:.4f}".format( a / b))
print ("\n")

#BAI 4
print ("BAI 4:")
def sum_two_number(a,b):
    return a + b
tong = sum_two_number(29,9)
print("Tồng của 2 số là: ", tong)
print ("\n")

#BAI 5
print ("BAI 5:")
name = "Lê Văn An"
age = 19
average_score = 9.5
print("Kiểu dữ liệu của name là: ", type(name))
print("Kiểu dữ liệu của age là: ", type(age))
print("Kiểu dữ liệu của average_score là: ", type(average_score))
age_next_year = age + 1
double_score = average_score * 2
print("Tên của bạn là: ", name, type(name))
print("Tuổi của bạn là: ", age, type(age))
print("Điểm trung bình của bạn là: ", average_score, type(average_score))
print("Tuổi của bạn vào năm sau sẽ là: ", age_next_year, type(age_next_year))
print("Điểm trung bình nhân đôi là: ", double_score, type(double_score))