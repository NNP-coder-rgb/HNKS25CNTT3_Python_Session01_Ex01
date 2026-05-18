print(' -- HỆ THỐNG TIEP NHẬN BỆNH NHÂN --- ')
name_patient = input( 'Nhập tên bệnh nhân: ')
age = int(input ('Mời bạn nhập tuổi: '))
symptom = input ('Mời bạn nhập triệu chứng bênh: ')

print(' - PHIẾU KHÁM BỆNH --- ')
print ('Tên bệnh nhân:', symptom)
print('Tuổi:', name_patient)
print ('Trieu chung:', age)

# 1. Phân tích lỗi :
# chương trình không bị crash nhưng dữ liệu in ra sai
# là do tên biến nhập vào một kiểu nhưng khi dùng câu lệch print 
# thì lại truyền biến một kiểu ví dụ như biến age dùng để lưu trữ tuổi nhưng 
# khi print thì lại truyền name_patient khiến dữ liệu sai lệch

# 2. Sửa lỗi :
print('-- HỆ THỐNG TIẾP NHẬN BỆNH NHÂN --')
name_patient = print('Nhập tên bệnh nhân: ')
age = int(input('Mời bạn nhập tuổi: '))
symptom = input('Mời bạn nhập triệu chứng bệnh: ')

print('- PHIẾU KHÁM BỆNH -')
print('Tên bệnh nhân: ', name_patient)
print('Tuổi: ', age)
print('Triệu chứng: ',symptom)