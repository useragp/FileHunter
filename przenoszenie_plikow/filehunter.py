import os
import argparse
# (przenoszenie lub ) wyświetlanie ścieżek plików, z określonym słowem w nazwie, (do podanego folderu)
# Logika : False - błąd, True - brak błędu


#--------------------  WORD  - SŁOWO ---------------------------------------------------
def check_word(word):
    # sprawdza czy podane słowo nie jest puste, oraz czy składa się z literek (oraz cyfr) - czy podany string jest słowem.

    if len(word) == 0:      # pusta wartość słowa
        print(f"{red("BŁĄD!!")}\twpisz jakie słowo chcesz wyszukać")
        return False

    for literka in word:
        if not(literka.isalnum() or literka in "_-"):
            print(f"{red("BŁĄD!!")}\t błędna literka :(")
            return False

    return True


#------------------------FOLDER OD KTÓREGO ROZPOCZYNA SIĘ PRZESZUKIWANIE -----------------------------------------------
def get_root(path):
    # zwraca "root" - początkowy folder, od którego rozpoczyna wyszukiwanie
    # domyślnie jest to główny folder w systemie - (np. Windows - C:)
    r = os.path.abspath(os.sep)
    try:

        if os.path.exists(path) and os.path.isdir(path):
            root = os.path.normpath(path)
            return root
        else:
            print(f"\n{red("Błąd!!")} - Podana ścieżka nie istnieje lub nie jest ścieżką folderu :(  -> sprawdzam każdy plik w systemie")
            return r

    except ValueError:
        print("\n -> sprawdzam każdy plik w systemie")
        return r

    except Exception as e:
        print(f"Błąd: {e}")
        return False

# -----------------------ŚCIEŻKA DO KTÓREJ MAJĄ ZOSTAĆ PRZENIESIONE PLIKI  // --move is on ------------------------------------------------
def create_path(path):
    try:
        os.makedirs(path, exist_ok=True)
        return True
    except PermissionError:
        print(f"\n{red("BŁĄD!! brak uprawnień :")}")
        return False
    except OSError as e:
        print(f"\nInny błąd: {e}")
        return False

def check_path(path, if_not_exist):
    if os.path.exists(path):
        return True  # jeśli podana ścieżka istnieje = "brak błędów"
    else:  # jeśli podana ścieżka nie isnieje
        if if_not_exist:
            path = os.path.normpath(path)  # normalizuje podaną ścieżkę
            return create_path(path)

        else:
            print(f"\nThe destination path doesn't exist. \nIf you still want to move files - create one or add {red("--create-path")} argument :)  \n\nBYEEE !! ")
                  # koniec zainicjowany przez użytkownika
    return False  # koniec

def get_path(path, if_not_exist):
    try:
        check_dst_path = check_path(path, if_not_exist)
        if check_dst_path: pass # jeśli check_path nie zwrwaca błędu - break
        else:
            return False
        return path

        # każdy inny przypadek - tylko wyświetlenie ścieżek

    except ValueError:
        print(" -> tylko wyświetlę ścieżki")


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
        print(f"{red("Błąd:")} {e}")
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


def red(text):
    print(f"\033[91m{text}\033[0m")

def main():
    parser = argparse.ArgumentParser()
    try:
        parser.add_argument("-w", "--word", type=str, help="Word to search for in filenames")
        parser.add_argument("-src", "--src-path", type=str , default=os.path.abspath(os.sep), help="Source path - where to search for [default: root]")

        parser.add_argument("--move", action="store_true", help="Print and move found files to specified destination [default: only print]")
        parser.add_argument("-dst", "--dst-path", type=str, help="Destination path - where to move found files [use with -m !!]")
        parser.add_argument("--create-path", action="store_true", help=f"If the destination path doesn't exist - create it {red("[default: OFF]")}")

        args = parser.parse_args()

    # słowo- sprawdzenie jego poprawności
        word = args.word
        if not word or not check_word(word): return 1     # jeśli błąd- return 1

    # folder w którym mają zostać znalezione pliki
        src_path = args.src_path
        root = get_root(src_path)
        if not root: return 1

        dst_path = args.dst_path
    # mają zostać przeniesione?
        if args.move:
            if not args.dst_path:
                print(f"Missing {red("--dst_path")} argument !!")
                return 1
            _create_path_if_not_exist = True
            if not args.create_path:
                _create_path_if_not_exist = False
            print("Moving files...")
            if not get_path(dst_path, _create_path_if_not_exist): return 1

        else:
            print(f"None {red("--move ")}argument\nPrinting files...")

        list_dir(root, word, args.move, dst_path)

        print("\n\nDONE :)")

    except KeyboardInterrupt:
        print("===== BYE BYE =====")

    except Exception as e:
        print(f"Błąd: {e}")
        return 1

main()