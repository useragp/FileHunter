import os
# (przenoszenie lub ) wyświetlanie ścieżek plików, z określonym słowem w nazwie, (do podanego folderu)
# Logika : False - błąd, True - brak błędu


#--------------------  WORD  - SŁOWO ---------------------------------------------------
def check_word(word):
    # sprawdza czy podane słowo nie jest puste, oraz czy składa się z literek (oraz cyfr) - czy podany string jest słowem.

    if len(word) == 0:      # pusta wartość słowa
        print("BŁĄD!!\t wpisz jakie słowo chcesz wyszukać")
        return False

    for literka in word:
        if not(literka.isalnum()) or literka in "_-":
            print("BŁĄD!!\t błędna literka :(")
            return False

    return True

def get_word():
    # pobiera słowo i sprawdza czy spełnia kryteria - check_word

    try:
        while True:
            slowo = str(input("\nPodaj slowo, jakie ma znajdowac sie w nazwie pliku:\n"))
            if check_word(slowo): break     # jeśli podane słowo nie spełnia kryteriów, prosi o wpisanie słowa ponownie

        return slowo

    except Exception as e:
        print(f"Błąd: {e}")
        return False

# -----------------------ŚCIEŻKA DO KTÓREJ MAJĄ ZOSTAĆ PRZENIESIONE PLIKI ------------------------------------------------
def create_path(path):
    try:
        os.mkdir(path)
        return True
    except PermissionError:
        print("\nBŁĄD!! brak uprawnień :(")
        return False
    except OSError as e:
        print(f"\nInny błąd: {e}")
        return False

def check_path(path):
    if os.path.exists(path):
        return True  # jeśli podana ścieżka istnieje = "brak błędów"
    else:  # jeśli podana ścieżka nie isnieje
        while True:
            create_path_decision = input("Ścieżka nie istnieje, czy chcesz ją stworzyć? (T\\N) \n")
            if create_path_decision.upper() == "T":
                path = os.path.normpath(path)  # normalizuje podaną ścieżkę
                return create_path(path)
                break
            elif create_path_decision.upper() == "N":
                print("\nOK BYE! ")
                break  # koniec zainicjowany przez użytkownika
            # jeśli podana zosranie inna wartość - pyta jeszcze raz

        return False  # koniec

def get_path():
    try:
        print_move = int(
            input("\nChcesz:\n\t[1] tylko wyświetlić ścieżki (domyślnie),\n\t[2] przenieść pliki i wyświetlić ścieżki??\n"))

        # wybrór + przeniesienie plików
        if print_move == 2:
            while True:
                dst_path = str(input(
                    "\nPodaj docelowy folder, do którego mają zostać przeniesione znalezione pliki (domyślny - bieżący):\n"))
                check_dst_path = check_path(dst_path)
                if check_dst_path:
                    break  # jeśli check_path nie zwrwaca błędu - break
                else:
                    return False
            return dst_path

        # każdy inny przypadek - tylko wyświetlenie ścieżek
        else:
            print(" -> wyświetlę ścieżki")
            return "PRINT_ONLY"  # tylko wyświetlić
    except ValueError:
        print(" -> wyświetlę ścieżki")
        return "PRINT_ONLY"

    except Exception as e:
        print(f"Błąd: {e}")
        return False

#------------------------FOLDER OD KTÓREGO ROZPOCZYNA SIĘ PRZESZUKIWANIE -----------------------------------------------
def get_root():
    # zwraca "root" - początkowy folder, od którego rozpoczyna wyszukiwanie
    root = os.path.abspath(os.sep)      # domyślnie jest to główny folder w systemie - (np. Windows - C:)
    try:
        # pobiera odpowiedź
        while True:
            directory = int(input("\nChcesz sprawdzić:\n\t[1] każdy plik w systemie (domyślnie - potrwa dłużej), czy\n\t[2] z konretnego folderu?:\n"))
            if directory in [1, 2]: break
            else: print("\nBłąd!!")

        if directory == 2:
            while True:
                path = str(input("\nPodaj ścieżkę:\n"))
                print()
                if os.path.exists(path) and os.path.isdir(path):
                    root = os.path.normpath(path)
                    break
                else:
                    print("\nBłąd!! - Podana ścieżka nie istnieje lub nie jest ścieżką folderu :(")
        return root

    except ValueError:
        print("\n -> sprawdzam każdy plik w systemie")
        return root

    except Exception as e:
        print(f"Błąd: {e}")
        return False

#------------------------PRZENOSZENIE / WYŚWIETLANIE PLIKÓW -----------------------------------------------
def move_file(dst_path, path):
    # przenosi znaleziony plik (path) do wybranego folderu (dst_path)
    try:
        target = os.path.join(dst_path, os.path.basename(path))     # docelowy folder- tworzony jest plik o tej konkretnej nazwie
        if os.path.exists(target):  # jeśli taki plik już istnieje- wyświetla ścieżkę i pomija
            print("Plik: ", path, "\tjuż istnieje, POMIJAM !!")
        else:
            # przenosi i wyświetla
            os.replace(path, target)
            print(path, " --> ", target)

    except Exception as e:
        print(f"Błąd: {e}")
        return False

def list_dir(root, slowo, path_move, dst_path):
    try:
        for file in os.listdir(root):   # przez każdy plik zawarty w root
            path = os.path.join(root, file)     # absolutna ścieżka każdego pliku

            if os.path.isdir(path):     # jeśli plik jest folderem
                list_dir(path, slowo, path_move, dst_path)   # rekurencyjne wywołanie funkcji list_dir
            else:
                # Jeśli w nazwie pliku znajduje się "slowo" (podane wcześniej)...
                # Ignorowana jest wielkość literek. Wielkość literek podanego słowa i tych występujących w nazwie pliku jest nieistotna.
                if slowo.lower() in os.path.basename(path).lower():

                    # Jeśli wybrano wcześniej opcję, z przenoszeniem znalezionych plików:
                    if path_move:
                       move_file(dst_path, path)

                    # Jeśli nie- ścieżka jest tylko wyświetlana.
                    else:
                        print(path)

    except PermissionError:
        pass    # pomija
    except FileNotFoundError:
        pass
    except Exception as e:
        print(f"Błąd: {e}")
        return False


def main():
    try:
        slowo = get_word()
        if not slowo: return 1     # jeśli błąd - return 1

        dst_path = get_path()
        if not dst_path: return 1

        path_move = True
        if dst_path == "PRINT_ONLY": path_move = False      #- TYLKO PRINT

        root = get_root()
        if not root: return 1


        paths = list_dir(root, slowo, path_move, dst_path)


        print("\n\n------------ DONE")

    except KeyboardInterrupt:
        print("===== BYE BYE =====")

    except Exception as e:
        print(f"Błąd: {e}")
        return 1

main()
