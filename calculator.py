#калькулятор оценок для учителя с рассчётом итоговых оценок
#Вводные данные 
name = input ("Введите ФИО ученика(цы): ")
ball_1 = float(input ("Введите первую оценку: "))
ball_2 = float(input ("Введите вторую оценку: "))
ball_3 = float(input ("Введите третью оценку: "))

#if range (90, 100):
 #   print (A)
#elif range (80, 89):
#    print(B)
#elif range (70, 79):
#    print(C)
#elif range (60, 69):
#    print(D)
#elif range (0, 59):
#    print(F)
print ("Результаты: ")
print (f" ФИО ученика {name}")
#первая оценка 
if 90 <= ball_1 <= 100:
    print (f"Первая оценка: A ")
elif 80 <= ball_1 <= 89:
    print(f"Первая оценка: B")
elif 70 <= ball_1 or 79:
    print(f"Первая оценка: C")
elif 60 <= ball_1 or 69:
    print(f"Первая оценка: D")
elif 0 <= ball_1 or 59:
    print(f"Первая оценка: F")
#вторая  оценка 
if 90 <= ball_2 <= 100:
    print (f"Вторая оценка: A ")
elif 80 <= ball_2 <= 89:
    print(f"Вторая оценка: B")
elif 70 <= ball_2 or 79:
    print(f"Вторая оценка: C")
elif 60 <= ball_2 or 69:
    print(f"Вторая оценка: D")
elif 0 <= ball_2 or 59:
    print(f"Вторая оценка: F")
#Третья  оценка 
if 90 <= ball_3 <= 100:
    print (f"Третья оценка: A ")
elif 80 <= ball_3 <= 89:
    print(f"Третья оценка: B")
elif 70 <= ball_3 or 79:
    print(f"Третья оценка: C")
elif 60 <= ball_3 or 69:
    print(f"Третья оценка: D")
elif 0 <= ball_3 or 59:
    print(f"Третья оценка: F")
    
    