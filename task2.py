number = int(input("Введите двухзначное число: "))
print(number[::-1])

number1 = int(input("Другой метод, Введите число: "))
print(f"{number1 % 10,}{number1 // 10}")

number2 = input("Введите двухзначное число: ")

if 10 <= number2 < 100:
    str_number = str(number)
    swapped_number = int(str_number[1] + str_number[0])
    print(f"В числе {number},\n десятки - {desyatki}, \n"
          f"еденицы - {edenichki},\n сумма - {suma}")
    