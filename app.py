import sys

# 1. РЕФАКТОРИНГ: Переименовали переменные (было 'u' и 'res', стало 'user_name' и 'greeting')
def process():
    user_name = input("Введите ваше имя: ")
    if len(user_name) < 3:
        print("Ошибка: слишком короткое имя!")
        return
    res = f"Привет, {u}!"
    print(res)

if __name__ == "__main__":
    process()