tienLuong = 5000 # kiểu số nguyên int
hsl = 1.475 # kiểu số thực float
hoTen = 'Lê Anh Thư' # kiểu chuỗi str

strTT1 = 'Họ tên: ' + hoTen + '\nTiền lương: ' + str(tienLuong)
print(strTT1)

strTT2 = 'Họ tên: %s \nTiền lương: %i \nHệ số lương: %f'%(hoTen, tienLuong, hsl)
print(strTT2)

strTT3 = 'Họ tên: %s \nTiền lương: %i \nHệ số lương: %.2f'%(hoTen, tienLuong, hsl)
print(strTT3)

print()