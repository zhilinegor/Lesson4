
def inp_num_N(): # проверка ввода количества чисел


    while True:
        
        num = (input("\nВведите количество чисел в списке: "))
        number_str = str(num) # для проверки что цифра
       
        if (number_str.isdigit() == False): # проверка, что введена цифра
            print("\nВы должны ввести число(целое) больше 0, попробуйте снова.")
            continue
        
        if (0 < int(num)): # проверка валидного количества
            return num
            break
        
        else:
            
             print("\nВы должны ввести число(целое) ,больше 0, попробуйте снова.")
            
list_of_digit = []
N = int(inp_num_N())
for i in range(N):
    while True:
        
        try:
            print("\nВведите число №",i+1,":")
            list_of_digit.append(float(input()))
            
            break
            
        except ValueError:
            print("\nВы должны ввести число, попробуйте снова.")

print("\nВы ввели список:",list_of_digit)

for i in range(N-1):
    for j in range(N-i-1):
        if list_of_digit[j] > list_of_digit[j+1]:
            list_of_digit[j], list_of_digit[j+1] = list_of_digit[j+1], list_of_digit[j]

print("\nСписок после сортировки:",list_of_digit)
            