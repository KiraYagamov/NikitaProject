days_in_months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

month = int(input("Месяц: "))
day = int(input("День: "))

days_count = 0

for i in range(month-1):
    days_count += days_in_months[i]
days_count += day

print(days_count)
