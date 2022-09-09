poem_1 = ['SOVINT DIEM',
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
contra el caire del temps''']

def get_poem():
    title = poem_1[0]
    poem = poem_1[1]
    return title, poem

def main():
    title, poem = get_poem()
    print(title)
    print(poem)

if __name__ == "__main__":
    main()
