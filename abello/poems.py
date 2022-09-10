import random

poems = [
    ['SOVINT DIEM',
     '''Sovint diem
això és la fi,
cap música ja no controla
les nostres esperances.
Però hi ha ulls que no coneixem
que escruten l’horitzó,
llavis que xiuxiuegen.
Orelles que perceben,
que amatents escolten
allà al fons de la nit.
Aquesta és la força que busquem,
l’amor que aprenem a sostenir
contra el caire del temps'''],
    [
        ['''El blat del temps (1986)'''],
        ['''Sense voler escolto
el so de paraules
que ja no tenen cap
valor.
Paraules que foren
dites en moments
que creguérem de gran
lucidesa. I ara les
trobem mortes,
llençades vora els cancells
de portes que no ens
atrevim a obrir. ''']
    ]
]


def get_poem():
    x = random.randint(0, len(poems)-1)
    title = poems[x][0]
    poem = poems[x][1]
    return title, poem


def main():
    title, poem = get_poem()
    print(title)
    print(poem)


if __name__ == "__main__":
    main()
