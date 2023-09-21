# hot-ncdc-python by Oskar Pliżga

## Description

This Python project simulates the construction of buildings with bricks based on a set of instructions. It takes the list of available bricks and instructions for the construction of buildings, and calculates how many buildings can be completed and how many cannot due to lack of necessary bricks.

## Files

The project is contained within a single Python file which includes multiple classes:

- **BricksUsed**: This class is responsible for keeping track of the number of bricks used in the construction process.

- **Instructions**: This class is responsible for storing and retrieving the instructions for building constructions.

- **ConstructionProject**: This is the main class of the project. It handles the construction process and calculates how many buildings can be completed and how many cannot.

## Usage

To run the project, you need to have Python installed on your system. You can run the program by using the following command in the command line:

```bash
python Bricks.py < plik.txt
```
## Task
Limit czasu wykonywania programu wynosi 30 sekund (nieco więcej o tym później).   
Nie ma znaczenia, czy program wykona się szybciej, czy wolniej; byle nie dłużej niż 30 sekund.

Dane jest pudełko z klockami oraz instrukcje składania budowli z klocków. W pudełku znajduje się nie więcej niż 10000000 klocków. Pudełko może też być puste. Klocki oznaczone są kodami w postaci łańcucha dokładnie 4 znaków. Klocki mogą się powtarzać zarówno w pudełku, jak i w instrukcjach. Instrukcji może być nie więcej niż 1000, a każda instrukcja może wymagać użycia nie więcej niż 5000 klocków. Instrukcje są numerowane. Niektóre instrukcje mogły zaginąć – brakujące numery instrukcji mogą w takim przypadku nie być podane i to nie jest błąd. Instrukcje jeżyka Bolka (których numer dzieli się bez reszty przez 3) będą wykonywane w pierwszej kolejności (Etap I). Pozostałe instrukcje będą wykonywane w Etapie II (po realizacji Etapu I). O kolejności składania budowli w ramach danego etapu decyduje numer instrukcji – od najniższego do najwyższego.   

Jeśli jakiś klocek został użyty w budowli, którą udało się zrealizować w całości, to takiego klocka nie można już użyć w kolejnej. Jeśli jakiejś instrukcji nie udało się zbudować, bo brakowało klocka, to nie budujemy jej wcale – wówczas klocki można użyć w kolejnych budowlach, o ile będą potrzebne.  

Dany jest strumień wejściowy. Wiersze prawidłowego strumienia wejściowego mają następujący format:  

<numer>:<znak1><znak2><znak3><znak4>  

gdzie:  

<numer> to numer instrukcji, liczba naturalna; może też być zerem – w takim przypadku oznacza pudełko; może się powtarzać; kolejność numerów w strumieniu wejściowym może być dowolna  
<znak1>/<znak2>/<znak3>/<znak4> to fragmenty kodu oznaczającego klocek. Każdy ze znaków może przyjmować wartość od A do O, tj. ABCDEFGHIJKLMNO, przy czym w instrukcjach występują tylko klocki, których kody składają się ze znaków ABCDEFGHIJKLMN (klocki zawierające w kodzie znak O są z innych grup przedszkolnych). W pudełku mogą pojawić się klocki zawierające w kodzie znak O.  
  
Przykłady niepoprawnych kodów klocków: 

ZZZZ  
ABCDE  
DFAS  
aaaA  

Przykłady poprawnych kodów klocków:  

EJGE  
FAAD  
AAAA  
BBBB  
DDDL  
 
Wynikiem prawidłowego wykonania programu powinno być sześć liczb w kolejnych wierszach, reprezentujących odpowiednio: 

Liczbę klocków użytych w etapie I  
Liczbę klocków użytych w etapie II  
Liczbę klocków, które pozostały w pudełku po zakończeniu budowania  
Łączną liczbę klocków, których brakowało w pudełku podczas realizacji poszczególnych instrukcji  
Liczbę budowli, które udało się zbudować  
Liczbę budowli, których nie udało się zbudować  
## License 

This project is not currently under any license.
