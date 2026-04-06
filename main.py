import os
# przenoszenie plików z określonym słowem w nazwie do podanego folderu
def check_word(word):
    if len(word) == 0:      # pusta wartość słowa
        print("BŁĄD!!\t co chcesz wyszukać? :(")
        return True

    if " " in word:         # więcej niż jedno słowo
        print("BŁĄD!!\t możesz wpisać tylko jedno słowo :(")
        return True

    for literka in word:
        if not(literka.isalnum() ): #or literka.isdigit()):
            print("BŁĄD!!\t błędna literka :(")
            return True 
    return 0

def create_path(path):
    try:
        os.mkdir(path)
    except PermissionError:
        print("\nBŁĄD!! brak uprawnień :(")
    except OSError as e:
        print(f"\nInny błąd: {e}")

def check_path(path):
    if os.path.exists(path):
        return 0
    else:
        create_path_decision = input("Ścieżka nie istnieje, czy chcesz ją stworzyć? (T\\N) \n")
        if create_path_decision.upper() == "T":
            path = os.path.normpath(path)
            create_path(path)
            return 0
        elif create_path_decision.upper() == "N":
            print("\n\nOK BYE! ")
            return 1 #koniec zainicjowany przez użytkownika
        else:
            print("\nNie rozumiem, BYEE")
            return 1

def list_dir(root, slowo):
    result = []
    try:
        for file in os.listdir(root):
            path = os.path.join(root, file)

            if os.path.isdir(path):
                list_dir(path, slowo)
            else:
                if slowo in os.path.basename(path):
                    result.append(path)
        return result

    except PermissionError:
        pass    # pomija
    except FileNotFoundError:
        pass



def main():
    try:
        slowo = str(input("Podaj slowo, jakie ma znajdowac sie w nazwie pliku:\n"))
        if check_word(slowo): return 1

        dst_path = str(input("Podaj docelowy folder (domyślny - bieżący):\n"))
        if check_path(dst_path) : return 1

        # input validation - int
        try:
            all_files = int(input("Chcesz sprawdzić:\n[1] każdy plik w systemie (domyślnie - potrwa dłużej), czy\n[2] z konretnego folderu?:\n"))
        except ValueError:
            print("Nie jest to liczbą!")
            return 1
        root = os.path.abspath(os.sep)

        if all_files == 2:
            path = str(input("Podaj ścieżkę:\n"))
            if os.path.exists(path) and os.path.isdir(path):
                root = os.path.normpath(path)
            else:
                print("Podana ścieżka nie istnieje lub nie jest ścieżką folderu :(")
                return 1

        file_paths = (list_dir(root, slowo))


        for file in file_paths:
            target = os.path.join(dst_path, os.path.basename(file))
            if not os.path.exists(target):
                os.replace(file, target)
                print(file, " --> ", target)
            else:
               print("Plik: ", file, "już istnieje, POMIJAM !!")



        print("\n\n----------------- KONIEC")
    except KeyboardInterrupt:
        print("===== BYE BYE =====")

main()
