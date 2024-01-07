def solve(date, month):
    if (21 <= date and month == 3) or (date <= 19 and month == 4):
        return "Bach Duong"
    elif (20 <= date and month == 4) or (date <= 20 and month == 5):
        return "Kim Nguu"
    elif (21 <= date and month == 5) or (date <= 20 and month == 6):
        return "Song Tu"
    elif (21 <= date and month == 6) or (date <= 22 and month == 7):
        return "Cu Giai"
    elif (23 <= date and month == 7) or (date <= 22 and month == 8):
        return "Su Tu"
    elif (23 <= date and month == 8) or (date <= 22 and month == 9):
        return "Xu Nu"
    elif (23 <= date and month == 9) or (date <= 22 and month == 10):
        return "Thien Binh"
    elif (23 <= date and month == 10) or (date <= 22 and month == 11):
        return "Thien Yet"
    elif (23 <= date and month == 11) or (date <= 21 and month == 12):
        return "Nhan Ma"
    elif (22 <= date and month == 12) or (date <= 19 and month == 1):
        return "Ma Ket"
    elif (20 <= date and month == 1) or (date <= 18 and month == 2):
        return "Bao Binh"
    elif (19 <= date and month == 2) or (date <= 20 and month == 3):
        return "Song Ngu" 
    
for _ in range(int(input())):
    date, month = map(int, input().split())
    print(solve(date, month))