#BAI 1:
print ("BÀI 1:")
x = int (input ("Nhập số nguyên: "))
if x % 2 == 0:
    print("True")
else:
        print("False")
print (x)

#BAI 2:
print ("\nBÀI 2:")
a = int (input ("Nhập số thứ nhất: "))
b = int (input ("Nhập số thứ hai: "))
c = int (input ("Nhập số thứ ba: "))
timmax = a
if b > timmax:
    timmax = b
if c > timmax:
       timmax = c
print("Số lớn nhất trong ba số là: ", timmax)

#BAI 3:
print ("\nBÀI 3:")
d = str(input("Nhập tên của bạn: "))
def greet(name="Student"):
    print(f"Hello {name}!")
greet()
greet(d)

#BAI 4
print ("\nBÀI 4:")
tuoi = int(input("Nhập tuổi của bạn: "))
if 1 <= tuoi <= 120:
    print("Tuổi của bạn hợp lệ!")
else:
    print("Tuổi của bạn không hợp lệ!")

#BAI 5:
print ("\nBÀI 5:")
text = str(input("Nhập văn bản để tìm số chữ cái 'a': "))
so_a = text.count('a')
print(f"Số chữ cái 'a' có mặt trong văn bản là: {so_a}")


#BAI 6:
print ("\nBÀI 6:")
print ("Máy chuyển từ độ C sang độ F: ")
c = float (input ("Nhập độ C: "))
f = c * 9/5 + 32
print ("Độ F là: ", f, " độ")


#BAI 7:
print ("\nBÀI 7:")
weight = int ( input("Nhập số cân nặng: "))
height = float ( input("Nhập chiều cao mét: "))
bmi = weight / (height * height)
print ("BMI của bạn là: \u2248 {:.2f}".format(bmi))

#BAI 8:
print ("\nBÀI 8:")
try:
    so1 = int(input("Nhập số bị chia: "))
    so2 = int(input("Nhập số chia: "))
    ketqua = so1 / so2
    print("Kết quả: ", ketqua)
except ZeroDivisionError:
    print("Lỗi: Không thể chia cho 0!")
except ValueError:
    print("Lỗi: Chỉ nhập chữ số")

#BAI 9:
print ("\nBÀI 9:")
import math
n = float(input("Nhập một số: "))
if n < 0:
    print("Lỗi: Không thể tính số âm!")
else:
    ket_qua = math.sqrt(n)
    print("Căn bậc hai của ", n, " là: ", ket_qua)

#BAI 10:
print ("\nBAI 10: ")
ten1 = str (input ("Nhập tên của sinh viên 1: "))
toan1 = float (input ("Nhập điểm toán của sinh viên 1: "))
ly1 = float (input ("Nhập điểm lý của sinh viên 1: "))
hoa1 = float (input ("Nhập điểm hóa của sinh viên 1: "))

ten2 = str (input ("Nhập tên của sinh viên 2: "))
toan2 = float (input ("Nhập điểm toán của sinh viên 2: "))
ly2 = float (input ("Nhập điểm lý của sinh viên 2: "))
hoa2 = float (input ("Nhập điểm hóa của sinh viên 2: "))

ten3 = str (input ("Nhập tên của sinh viên 3: "))
toan3 = float (input ("Nhập điểm toán của sinh viên 3: "))
ly3 = float (input ("Nhập điểm lý của sinh viên 3: "))
hoa3 = float (input ("Nhập điểm hóa của sinh viên 3: "))
print ("----TỔNG KẾT----")
sv1 = (toan1 + ly1 + hoa1) / 3
print("Tên sinh viên: ", ten1, " - Điểm trung bình ba môn= ", sv1)

sv2 = (toan2 + ly2 + hoa2) / 3
print("Tên sinh viên: ", ten2, " - Điểm trung bình ba môn= ", sv2)

sv3 = (toan3 + ly3 + hoa3) / 3
print("Tên sinh viên: ", ten3, " - Điểm trung bình ba môn= ", sv3)

