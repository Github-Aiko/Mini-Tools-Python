import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def diem():
    weights = {1: (0.1, 0.3, 0.6), 2: (0.1, 0.4, 0.5), 3: (0.1, 0.2, 0.7)}

    print("Chọn tỉ lệ điểm (Chuyên cần - Giữa kì - Cuối kì)")
    print("1. 10% - 30% - 60%")
    print("2. 10% - 40% - 50%")
    print("3. 10% - 20% - 70%")

    choose = int(input("Chọn: "))
    if choose not in weights:
        print("Lựa chọn không phù hợp!")
        os.exit()

    attendance, mid, final = map(float, (input(f"Nhập điểm {x}: ") for x in ('chuyên cần', 'giữa kì', 'cuối kì')))

    attendance *= weights[choose][0]
    mid *= weights[choose][1]
    final *= weights[choose][2]

    score = round(attendance + mid + final, 2)
    print("Điểm cuối kì: ", score)

if __name__ == '__main__':
    clear()
    diem()
