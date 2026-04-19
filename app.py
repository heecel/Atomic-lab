import sys

# 1. РЕФАКТОРИНГ: Переименовали переменные (было 'u' и 'res', стало 'user_name' и 'greeting')
def process():
    user_name = input("Введите ваше имя: ")
    if len(user_name) < 3:
        print("Ошибка: слишком короткое имя!")
        return
    greeting = f"Привет, {user_name}!"
    print(greeting)

# 2. ФИЧА: Новая функция статуса пользователя
def get_user_status(age):
    if age < 18:
        return "Junior"
    return "Senior"

# 3. ФИКС: Обработка ошибок (блок try-except)
if __name__ == "__main__":
    try:
        process()
    except KeyboardInterrupt:
        print("\nПрограмма принудительно завершена")
        sys.exit(0)



           
            