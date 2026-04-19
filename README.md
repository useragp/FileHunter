# 📂 FileHunter CLI

FileHunter CLI to lekkie narzędzie w Pythonie działające w terminalu, służące do wyszukiwania plików na podstawie słów kluczowych w nazwach oraz opcjonalnego przenoszenia ich do wybranego folderu.

## 🔍 Opis

Program przeszukuje foldery rekurencyjnie i identyfikuje pliki, których nazwy zawierają podane słowo kluczowe.

Użytkownik może:

- wyświetlić ścieżki dopasowanych plików w terminalu
- przenieść dopasowane pliki do wskazanego folderu
## ✅ Zastosowania
- efektywna organizacja plików
- bezpieczne przeglądanie wyników przed przeniesieniem plików
- automatyzacja powtarzalnych zadań związanych z zarządzaniem plikami

## ▶️ Uruchomienie
Pobierz repozytorium:
 ```bash
git clone https://github.com/twoj-login/FileHunter.git
```
Przejdź do folderu projektu:
```bash
cd FileHunter
```
### Uruchom program:
-  Tylko wyszukiwanie i wyświetlanie:
```bash
python filehunter.py -w log -src C:\Users
```
-  Wyszukiwanie i przenoszenie plików:
```bash
python filehunter.py -w log -src C:\Users --move -dst C:\folder_docelowy --create-path
```

## 🧠 Argumenty
- `-w, --word` → słowo kluczowe do wyszukiwania w nazwach plików
- `-src, --src_path` → folder źródłowy (domyślnie: system root)
- `--move` → włącza tryb przenoszenia plików
- `-dst, --dst_path` → folder docelowy dla przenoszonych plików
- `--create-path` → jeśli podany folder docelowy nie istnieje, program spróbuje go utworzyć

## ⚡ Funkcjonalności
- przeszukiwanie folderów rekurencyjnie
- wyszukiwanie plików po słowie kluczowym (bez względu na wielkość liter)
- opcjonalne przenoszenie plików do innego folderu (`--move`)
- automatyczne tworzenie folderu docelowego (jeśli nie istnieje)
- obsługa przez terminal (CLI)
- obsługa błędów (brak uprawnień, nieistniejące ścieżki)
- walidacja danych wejściowych
## 📌 Uwagi
- Przeszukiwanie całego systemu może trwać długo
- Niektóre foldery mogą zostać pominięte z powodu braku uprawnień
- Pliki o tej samej nazwie nie są nadpisywane
- Jeśli używasz `--move`, ale folder docelowy nie istnieje, możesz użyć `--create-path`, aby został automatycznie utworzony.
## 👩‍💻 Autor
Projekt stworzony w celach edukacyjnych
