def wczytaj_baze_probek_z_tekstem(nazwa_pliku_z_wartosciami: str, nazwa_pliku_z_opisem: str) -> tuple[list[list[str]], list[bool], list[str]]:
    probki = []
    czy_atr_symb = []
    nazwy_atr = []

    with open(nazwa_pliku_z_wartosciami) as f:
        lines = f.readlines()
    for line in lines:
        probki.append(line.split())
    
    with open(nazwa_pliku_z_opisem) as f:
        lines = f.readlines()
    for line in lines:
        if len(line.split()) < 2:
            continue
        name, symb = line.split()
        nazwy_atr.append(name)
        czy_atr_symb.append(symb == "s")

    return probki, czy_atr_symb, nazwy_atr