import sys

def process():
    u = input("Введите ваше имя: ")
    if len(u) < 3:
        print("Ошибка: слишком короткое имя!")
        return
    res = f"Привет, {u}!"
    print(res)

if __name__ == "__main__":
    process()