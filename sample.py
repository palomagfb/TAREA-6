
# sample.py
def metodo1():
    # Aquí va el código del método 1
    comment = input("Ingrese un comentario: ")
    post = f'ポスト: {comment}'
    with open("data.txt", "w", encoding="utf-8") as file_pc:
        file_pc.write(post)
    print("Evaluación completada")

def metodo2():
    # Aquí va el código del método 2
    print('これまでの結果')
    with open("data.txt", "r", encoding="utf-8") as read_file:
        print(read_file.read())

def metodo3():
    # Aquí va el código del método 3
    print('終了します')
    exit()

def main():
    while True:
        num = int(input("Ingrese un número (1-3): "))
        if num == 1:
            metodo1()
        elif num == 2:
            metodo2()
        elif num == 3:
            metodo3()
        else:
            print('1から3で入力してください')

if __name__ == "__main__":
    main()
