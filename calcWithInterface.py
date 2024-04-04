from tkinter import *
# лист всем символов для того, чтобы брать определенный кусок симовлов, размер зависит от выбранной системы
listOfSymbols = [i for i in "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
# сам по себе этот метод является укоротителем следующего метода "трансформатора", который проверят,
# можно ли с этим числом работать и не вызовет ли он ошибок
def checker(sys, num):
    if sys > 32 or sys < 1:
        return "Введена неверная система счисления"
    # проверка на использование "правильных" символов
    for i in num:
        if i not in listOfSymbols[:sys]:
            return "Введенные символы не находятся в таблице символов выбранной вами системы счисления"
    return ""
def transform_system_to_10(sys, num):
    # в качестве числа, которое мы будем переводить, является строка, т.к. именно ее мы сможем перевести в список чисел
    if len(num) > 1:
        num = str(num).strip().upper().lstrip("0")
    elif len(num) == 0:
        return 0
    else:
        num = str(num).strip().upper()
    # если число отрицательное, то мы уберем минус из нашего числа, чтобы в будущем не возникало проблем с минусом.
    # в конце мы проверим, является ли переменныя "withMinus" истинной, если да, то домножим на -1 и вернем отрицатель-
    # ное число
    withMinus = num[0] == "-"
    if withMinus:
        num = num[1:]
    # в переменную кладем "ответ" checker
    msgOfChecker = checker(sys, num)
    if msgOfChecker != "":  # если ответ будет пустым, то значит, что число подходит.
        # Если нет, то мы говорим пользователю, что конкретно он неверно ввел
        return msgOfChecker
    # чтобы не жрать память, сразу проверим, не находится ли число в десятичной системе.
    # Предыдущие проверки нужны для того, чтобы не было случая того, что в десятичной системе есть буквы.
    if sys == 10:
        return int(num)
    listForWork = listOfSymbols[:sys]  # список символов, которые будут использоваться в системе
    dig = [i for i in num]  # наши цирфы, с которыми будет идти работа со степенями
    # сам перевод
    newNum = 0
    for i in range(len(dig) - 1, -1, -1):
        newNum += (listForWork.index(dig[i]) * sys ** (len(dig) - 1 - i))
    if withMinus:
        return int(num) * (-1)
    return int(newNum)
# метод, в который кладется число в 10-й системе. Его мы будем переводит в определенную иную систему путем деления
def transform_to_another_sys(num, sys):
    # если окажется, что система десятичная, то ничего делать не придется: уже все сделано
    if sys == 10:
        return num
    # в случае, если число является нулем, то ничего с ним делать не будем, просто вернем 0
    if num == 0:
        return "0"
    num = num
    listForWork = listOfSymbols[:sys]  # сокращение списка символов, с которым придется иметь дело
    new_num = list()
    # проверим, является ли число отрицательным и, если это правда, сохраним в памяти то, что число отрицательное
    withMinus = False
    if num < 0:
        withMinus = True
        num = num * (-1)
    while num != 0 and num != 1:
        new_num.insert(0, listForWork[num % sys])
        num = num // sys
    if withMinus:
        if num % sys > 0:
            return "-" + str(num % sys) + "".join(new_num)
        return "-" + "".join(new_num)
    else:
        if num % sys > 0:
            return str(num % sys) + "".join(new_num)
        return "".join(new_num)
# метод, который возвращает итоговые
def math_with_numbers(num1, sys1, num2, sys2, op, sysA):
    # данный блок кладет в переменные значения возвратов функций, если это сообщение об ошибке,
    # то возвращаем это же сообщение, если все в порядке и мы имеем дело с числом, то продолжаем
    num1 = transform_system_to_10(sys1, num1)
    if not isinstance(num1, int):
        return "Ошибка в вводе текста"
    num2 = transform_system_to_10(sys2, num2)
    if not isinstance(num2, int):
        return "Ошибка в вводе 2 текста"
    match op:
        case "-":
            return transform_to_another_sys((num1 - num2), sysA)
        case "+":
            return transform_to_another_sys((num1 + num2), sysA)
        case "*":
            return transform_to_another_sys((num1 * num2), sysA)
        case "/":
            if num2 == 0:
                return "На ноль делить нельзя!"
            return transform_to_another_sys((num1 // num2), sysA)
        case "^":
            return transform_to_another_sys((num1 ** num2), sysA)
        case _:
            return "Ошибка в выборе операции"
def start(op):
    answer.delete("1.0", END)
    answer.insert("1.0", str(math_with_numbers(
        ent_num1.get(), int(ent_sys1.get()),
        ent_num2.get(), int(ent_sys2.get()),
        op, int(ent_sys_Answer.get()))))
    return
# отдельные функции для кнопок, чтобы мы могли передать нужного нам оператора для вычислений
root = Tk()
root.geometry("435x240")
# кнопки
btn_plu = Button(root, width=2, text="+", font=("MS Sans Serif", 15), command = lambda : start("+"))
btn_min = Button(root, width=2, text="-", font=("MS Sans Serif", 15), command = lambda : start("-"))
btn_mul = Button(root, width=2, text="х", font=("MS Sans Serif", 15), command = lambda : start("*"))
btn_div = Button(root, width=2, text="/", font=("MS Sans Serif", 15), command = lambda : start("/"))
btn_pow = Button(root, width=2, text="^", font=("MS Sans Serif", 15), command = lambda : start("^"))
btn_plu.place(x=320,   y=0)
btn_min.place(x=320,  y=40)
btn_mul.place(x=360,  y=0)
btn_div.place(x=360,  y=40)
btn_pow.place(x=400, y=0)
# поля ввода
ent_num1 = Entry(root, font=("MS Sans Serif", 18), textvariable=(StringVar(value="1")))
ent_num2 = Entry(root, font=("MS Sans Serif", 18), textvariable=(StringVar(value="1")))
# textvariable - параметр, с помощью которого можно сделать привязку виджета к переменной
ent_sys1 = Entry(root, font=("MS Sans Serif", 18), textvariable=(StringVar(value="10")), width=3)
ent_sys2 = Entry(root, font=("MS Sans Serif", 18), textvariable=(StringVar(value="10")), width=3)
ent_sys_Answer = Entry(root, font=("MS Sans Serif", 18), textvariable=(StringVar(value="10")), width=3)
ent_num1.place(x=50,y=5 )
ent_num2.place(x=50,y=45)
ent_sys1.place(x=2, y=5 )
ent_sys2.place(x=2, y=45)
ent_sys_Answer.place(x=2, y=90)
# текст с выводом ответа
answer = Text(root, font=("Arial", 15), width=35, height=6, )
answer.place(x=50, y=90)
answer.insert("1.0", "Введите в 1 колонку - системы счислений чисел, во 2 колонку - сами числа, после выберите с помощью кнопок операцию, которую нужно провести над этими числами.")
root.mainloop()
