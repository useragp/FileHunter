import os
# przenoszenie plików z określonym słowem w nazwie do podanego folderu
def check_word(word):
    if len(word) == 0:
        print("BŁĄD!!\t co chcesz wyszukać? :(")
        return 1

    if " " in word:
        print("BŁĄD!!\t możesz wpisać tylko jedno słowo :(")
        return 1

    for literka in word:
        if not(literka.isalnum() ): #or literka.isdigit()):
            print("BŁĄD!!\t błędna literka :(")
            return 1
    # return 0

def create_path(path):
    try:
        os.mkdir(path)
    except PermissionError:
        print("BŁĄD!! brak uprawnień :(")
    except OSError as e:
        print(f"Inny błąd: {e}")

def check_path(path):
    if os.path.exists(path):
        return 0
    else:
        create_path_decision = input("Ścieżka nie istnieje, czy chcesz ją stworzyć? (T\\N) \n")
        if create_path_decision == ("T" or "t"):
            create_path(path)
            return 0
        else:
            print("---- BYE ")
            return 1 #koniec zainicjowany przez użytkownika

def list_dir(root, slowo):
    r = []
    try:
        for file in os.listdir(root):
            path = os.path.join(root, file)

            if os.path.isdir(path):
                list_dir(path, slowo)
            else:
                if slowo in path:
                    r.append(path)
        return r

    except PermissionError:
        pass
    except FileNotFoundError:
        pass


def main():
    try:
        while True:
        slowo = str(input("Podaj slowo, jakie ma znajdowac sie w nazwie pliku:\n"))
        if check_word(slowo): return 1


        dst_path = input("Podaj docelowy folder:\n")
        if check_path(dst_path) : return 1

        all_files = int(input("Chcesz sprawdzić:\n[1] każdy plik w systemie (domyślnie - potrwa dłużej), czy\n[2] z konretnego folderu?:\n"))
        root = os.path.abspath(os.sep)

        if all_files == 2:
            path = str(input("Podaj ścieżkę:\n"))
            root = os.path.normpath(path)
        file_paths = (list_dir(root, slowo))

        print("Here")
        for file in file_paths:
            os.replace(file, f"{dst_path}\\{os.path.basename(file)}")
            print(file, f"\t\t{dst_path}\\{os.path.relpath(file)}")


    except KeyboardInterrupt:
        print("===== BYE BYE =====")

main()