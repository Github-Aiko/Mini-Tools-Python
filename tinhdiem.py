import os

def clear():
	os.system('cls' if os.name == 'nt' else 'clear')

def ai():
	print("Chọn tỉ lệ điểm (Chuyên cần - Giữa kì - Cuối kì)")
	print("1. 10% - 30% - 60%")
	print("2. 10% - 40% - 50%")
	print("3. 10% - 20% - 70%")
	choose = float(input("Chọn: "))
	if choose != 1 and choose != 2 and choose != 3:
		print("Lựa chọn không phù hợp!")
		os.exit()
		
	# nhập điểm chuyên cần
	attendance = float(input("Nhập điểm chuyên cần: "))
	# nhập điểm giữa kì
	mid = float(input("Nhập điểm giữa kì: "))
	# nhập điểm cuối kì
	final = float(input("Nhập điểm cuối kì: "))

	if choose == 1:
		attendance = attendance * 0.1
		mid = mid * 0.3
		final = final * 0.6
	elif choose == 2:
		attendance = attendance * 0.1
		mid = mid * 0.4
		final = final * 0.5
	elif choose == 3:
		attendance = attendance * 0.1
		mid = mid * 0.2
		final = final * 0.7
	else:
		print("Lựa chọn không phù hợp!")
		clear()
		os.exit()

	# tính điểm cuối kì
	score = attendance + mid + final

	# lấy số sau dấu phẩy 2 chữ số
	score = round(score, 2)
	# in ra điểm cuối kì
	print("Điểm cuối kì: ", score)

if __name__ == '__main__':
	clear()
	ai()