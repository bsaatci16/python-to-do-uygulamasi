from colorama import Fore, Style, init

# colorama kütüphanesini başlat
init(autoreset=True)

print(Fore.GREEN + "To-Do Uygulaması" + Style.RESET_ALL)

def show_menu():
    print("1. Yapılacakları Listele")
    print("2. Yapılacak Ekle")
    print("3. Yapılacak Sil")
    print("4. Çıkış")

def list_tasks(tasks):
    print("Yapılacaklar Listesi:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")

def add_task(tasks, new_task):
    tasks.append(new_task)
    print("Yapılacak eklendi:", new_task)
    save_tasks(tasks)

def remove_task(tasks, task_index):
    if 1 <= task_index <= len(tasks):
        removed_task = tasks.pop(task_index - 1)
        print("Yapılacak silindi:", removed_task)
        save_tasks(tasks)
    else:
        print("Geçersiz görev numarası!")

def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def load_tasks():
    tasks = []
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                tasks.append(line.strip())
    except FileNotFoundError:
        pass
    return tasks

tasks = load_tasks()

while True:
    show_menu()
    choice = input("Seçiminizi yapın: ")

    if choice == '1':
        list_tasks(tasks)
    elif choice == '2':
        new_task = input("Yeni yapılacak girin: ")
        add_task(tasks, new_task)
    elif choice == '3':
        list_tasks(tasks)
        task_index = int(input("Silmek istediğiniz yapılacagın numarasını girin: "))
        remove_task(tasks, task_index)
    elif choice == '4':
        print("To-Do uygulaması kapatılıyor.")
        break
    else:
        print("Geçersiz seçenek! Lütfen tekrar deneyin.")
