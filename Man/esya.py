print("Добро пожаловать в наше кафе!")
result = 0
i = 0
print("Для начала авторизуйтесь")
parol = input("Придумайте пароль:")
parol_2 = input("Повторите пароль для надежности:")
while parol != parol_2:
    print("Пароли не сходятся, попробуйте еще раз")
    parol_2 = input("Повторите пароль для надежности:")
if parol == parol_2:
    print("Отлично, пароль зарегистрирован")
while i <= 1000:
    choice = input("продолжить выбор пицц?(да/нет)")
    while choice != "нет":
        change = int(input("Гавайская - 1, Дары Моря - 2, Барбекю - 3, Пепперони - 4, Маргарита - 5:    "))
        if change > 5:
            print("Неверный выбор")
        if change == 1:
            size = int(input("Тонкое тесто - 1, Стандартное тесто - 2, Борты с начинкой - 3:    "))
            if size > 3:
                print("Неверный выбор")
            if size == 1:
                price = str(input("Стоимость выбранной пиццы составляет: 699.99 рублей. Добавить в корзину (да/нет)"))
                money = 699.99
                if price == "да":
                    result = result + money
                else:
                    result = result
            elif size == 2:
                price = str(input("Стоимость выбранной пиццы составляет: 399.99 рублей. Добавить в корзину (да/нет)"))
                money = 399.99
                if price == "да":
                    result = result + money
                else:
                    result = result
            else:
                price = str(input("Стоимость выбранной пиццы составляет: 899.99 рублей. Добавить в корзину (да/нет)"))
                money = 899.99
                if price == "да":
                    result = result + money
                else:
                    result = result
        elif change == 2:
            size = int(input("Тонкое тесто - 1, Стандартное тесто - 2, Борт с начинкой - 3:    "))
            if size > 3:
                print("Неверный выбор")
            if size == 1:
                price = str(input("Стоимость выбранной пиццы составляет: 499.99 рублей. Добавить в корзину (да/нет)"))
                money = 499.99
                if price == "да":
                    result = result + money
                else:
                    result = result
            elif size == 2:
                price = str(input("Стоимость выбранной пиццы составляет: 399.99 рублей. Добавить в корзину (да/нет)"))
                money = 399.99
                if price == "да":
                    result = result + money
                else:
                    result = result
            else:
                price = str(input("Стоимость выбранной пиццы составляет: 899.99 рублей. Добавить в корзину (да/нет)"))
                money = 899.99
                if price == "да":
                    result = result + money
                else:
                    result = result
        elif change == 3:
            size = int(input("Тонкое тесто - 1, Стандартное тесто - 2, Борт с начинкой - 3:    "))
            if size > 3:
                print("Неверный выбор")
            if size == 1:
                price = str(input("Стоимость выбранной пиццы составляет: 599.99 рублей. Добавить в корзину (да/нет)"))
                money = 599.99
                if price == "да":
                    result = result + money
                else:
                    result = result
            elif size == 2:
                price = str(input("Стоимость выбранной пиццы составляет: 399.99 рублей. Добавить в корзину (да/нет)"))
                money = 399.99
                if price == "да":
                    result = result + money
                else:
                    result = result
            else:
                price = str(input("Стоимость выбранной пиццы составляет: 899.99 рублей. Добавить в корзину (да/нет)"))
                money = 899.99
                if price == "да":
                    result = result + money
                else:
                    result = result
        elif change == 4:
            size = int(input("Тонкое тесто - 1, Стандартное тесто - 2, Борт с начинкой - 3:    "))
            if size > 3:
                print("Неверный выбор")
            if size == 1:
                price = str(input("Стоимость выбранной пиццы составляет: 599.99 рублей. Добавить в корзину (да/нет)"))
                money = 599.99
                if price == "да":
                    result = result + money
                else:
                    result = result
            elif size == 2:
                price = str(input("Стоимость выбранной пиццы составляет: 399.99 рублей. Добавить в корзину (да/нет)"))
                money = 399.99
                if price == "да":
                    result = result + money
                else:
                    result = result
            else:
                price = str(input("Стоимость выбранной пиццы составляет: 899.99 рублей. Добавить в корзину (да/нет)"))
                money = 899.99
                if price == "да":
                    result = result + money
                else:
                    result = result
        elif change == 5:
            size = int(input("Тонкое тесто - 1, Стандартное тесто - 2, Борт с начинкой - 3:    "))
            if size > 3:
                print("Неверный выбор")
            if size == 1:
                price = str(input("Стоимость выбранной пиццы составляет: 599.99 рублей. Добавить в корзину (да/нет)"))
                money = 599.99
                if price == "да":
                    result = result + money
                else:
                    result = result
            elif size == 2:
                price = str(input("Стоимость выбранной пиццы составляет: 399.99 рублей. Добавить в корзину (да/нет)"))
                money = 399.99
                if price == "да":
                    result = result + money
                else:
                    result = result
            else:
                price = str(input("Стоимость выбранной пиццы составляет: 899.99 рублей. Добавить в корзину (да/нет)"))
                money = 899.99
                if price == "да":
                    result = result + money
                else:
                    result = result
        print("Сейчас в корзине:", result,)
        choice = input("продолжить выбор пицц?(да/нет)")
    if choice == "нет":
            print("Выбор завершен.")
    pay = input("Выберите способ оплаты:(нал/безнал)")
    if pay == "безнал":
        print("Сумма к оплате",result)
        print("Оплата прошла успешно, до свидания!")
        break
    if pay == "нал":
        print("Сумма к оплате", result)
        sum = float(input("Введите вашу сумму:"))
        if sum < result:
            print("У вас не достаточно средств")
        if sum > result:
            lease = sum - result
            print("Ваша сдача:",lease,". До свидания!")
            break








