# 📂 FileHunter CLI

FileHunter CLI to lekkie narzędzie w Pythonie działające w terminalu, służące do wyszukiwania plików na podstawie słów kluczowych w nazwach oraz opcjonalnego przenoszenia ich do wybranego folderu.

## 🔍 Opis

Program przeszukuje foldery rekurencyjnie i identyfikuje pliki, których nazwy zawierają podane słowo kluczowe.

Użytkownik może:

- wyświetlić ścieżki do dopasowanych plików w terminalu
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
Uruchom program:
```bash
python main.py
```

## ⚡ Funkcjonalności
- przeszukiwanie folderów rekurencyjnie
- dopasowanie nazw plików bez uwzględniania wielkości liter
- opcjonalne przenoszenie plików
- obsługa błędów (brak uprawnień, nieistniejące ścieżki)
- walidacja danych wejściowych
## 📌 Uwagi
- Przeszukiwanie całego systemu może trwać długo
- Niektóre foldery mogą zostać pominięte z powodu braku uprawnień
- Pliki o tej samej nazwie nie są nadpisywane
## 👩‍💻 Autor
Projekt stworzony w celach edukacyjnych
