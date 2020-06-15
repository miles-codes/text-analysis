# Aplikacija za analizu sadržaja tekstualnih datoteka

Aplikacija se pokreće iz terminala/konzole tako da se u argumentima navede putanja do txt datoteke sa sadržajem kojeg treba analizirati.

```
usage: python3 main.py [-h] --file filepath [--length length] [--top n] [--output output]
  -h, --help            show this help message and exit
  --file filepath, -f filepath
                        path to a file to be read
  --length length, -l length
                        length of different characters in a word, default=3
  --top n, -t n         show top n results, default=10
  --output output, -o output
                        write output to this file

```

Analizira se učestalost pojavljivanja različitih znakova unutar iste riječi.
Broj različitih znakova se može odrediti s argumentom --length.

Ukoliko se unutar neke riječi znak ponavlja više puta, u analizu ulazi samo jedno pojavljivanje (npr. ‘jabuka’ se analizira kao ‘jabuk’).
Također, u analizu ulaze samo alfa-numerički znakovi. (npr. 'jabuka!' se analizira kao 'jabuk'')

Rezultati su prikazani kao lista top N najčešćih kombinacija znakova.
N se može odrediti s argumentom --top

```
example: 
python3 main.py -f input/sample.txt
or
python3 main.py -f input/sample.txt -l 3 -t 10 -o output.txt
(('a', 'k', 'u'), 2)
(('a', 'k', 'l'), 1)
(('a', 'l', 'u'), 1)
(('k', 'l', 'u'), 1)
(('a', 'k', 'n'), 1)
(('a', 'n', 'u'), 1)
(('k', 'n', 'u'), 1)
```
