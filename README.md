# Friction Analyzer
The friction_analyzer.py script is designed to process files containing results of friction parameter measurements recorded during tribological studies on a nanotribometer. Conducting long-term studies on this device generates a vast amount of data, hence the need for a tool for their rapid analysis.

## Script Features
The program's task is to extract data regarding the friction coefficient, then average them using a moving average, and save the results in a new file. The script handles all .csv files in the specified directory and then saves the results of its work to one consolidated .csv file.

To verify the accuracy of the performed operations, the program saves the results of the conducted operations in the form of a consolidated line chart in a .png file at the end.

## Steps Required to Conduct the Analysis
Run the .py script friction_analyzer.py in a Python interpreter.
Indicate the path to the folder containing the files for analysis.
Select the appropriate data range for calculating the moving average.
To avoid errors related to attempting to process other files, ensure that only files exported by the device's 
measurement system and intended for analysis are located in the specified folder.

## Error Handling
Ensure that you provide the path to the directory without using quotation marks.
If you encounter problems running the script, a containerized version is available.

## Containerized Version
If you encounter problems running the script, its image has been created on Docker Hub. You can download and run it using the following address:

https://hub.docker.com/repository/docker/mariuszkam4/friction_analyzer/general

## Required Libraries
To run the friction_analyzer.py script, the following libraries are needed:

pandas: For data processing and analysis.
os: For interacting with the operating system, e.g., managing file paths.
matplotlib: For creating charts.
You can install these libraries using the pip command:
pip install pandas
pip install matplotlib

PL
# Friction Analyzer
Skrypt friction_analyzer.py jest zaprojektowany do przetwarzania plików z wynikami pomiarów parametrów tarcia rejestrowanych podczas badań tribologicznych na nanotribometrze. Prowadzenie długoterminowych badań na tym urządzeniu generuje ogromną ilość danych, stąd potrzeba narzędzia do ich szybkiej analizy.

## Funkcje Skryptu
Zadaniem programu jest ekstrakcja danych dotyczących współczynnika tarcia, następnie ich uśrednianie przy użyciu średniej ruchomej i zapisanie wyników w nowym pliku. Skrypt obsługuje wszystkie pliki .csv w określonym katalogu, a następnie zapisuje wyniki swojej pracy do jednego skonsolidowanego pliku .csv.

Aby zweryfikować dokładność wykonanych operacji, program zapisuje wyniki przeprowadzonych operacji w postaci skonsolidowanego wykresu liniowego w pliku .png na końcu.

## Kroki Wymagane do Przeprowadzenia Analizy
Uruchom skrypt .py friction_analyzer.py w interpreterze Pythona.
Wskaż ścieżkę do folderu zawierającego pliki do analizy.
Wybierz odpowiedni zakres danych do obliczenia średniej ruchomej.
Aby uniknąć błędów związanych z próbą przetwarzania innych plików, upewnij się, że w określonym folderze znajdują się tylko pliki wyeksportowane przez system pomiarowy urządzenia i przeznaczone do analizy.

## Obsługa Błędów
Upewnij się, że podajesz ścieżkę dostępu do katalogu bez użycia cudzysłowów.
W przypadku problemów z uruchomieniem skryptu, dostępna jest wersja konteneryzowana.

## Wersja Konteneryzowana
Jeśli napotkasz problemy z uruchomieniem skryptu, utworzony jest jego obraz na Docker Hub. Możesz go pobrać i uruchomić korzystając z poniższego adresu:

https://hub.docker.com/repository/docker/mariuszkam4/friction_analyzer/general

## Wymagane Biblioteki
Aby uruchomić skrypt friction_analyzer.py, potrzebne są następujące biblioteki:

pandas: Do przetwarzania i analizy danych.
os: Do interakcji z systemem operacyjnym, np. do zarządzania ścieżkami plików.
matplotlib: Do tworzenia wykresów.
Możesz zainstalować te biblioteki używając polecenia pip:
pip install pandas
pip install matplotlib