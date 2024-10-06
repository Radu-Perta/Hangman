tries = 0  # am creat un counter pentru a putea tine cont incercariile
alphabet = "IERLAOTNUCSĂMDPGBFȚȘZVHÂÎJXK"
# am redus nr total de incercari datorita aranjarii literelor
# din alfabet in acest fel(cel mai eficient pe care l-am gasit eu)


with open('cuvinte.csv', 'r', encoding='utf-8-sig') as file:
    data = file.read()  # citim cele 100 de cuvinte dintr-un fisier csv(comma seperated values)

rows = data.strip().split("\n")  # delimitam randurile

for row in rows:
    x = 0  # index-ul literei din alfabet
    number, masked_word, full_word = row.split(";")
    word = full_word
    guess = masked_word

    while word != guess and x < len(alphabet):
        if alphabet[x] in guess:
            # daca am gasit litera, crestem indexul si trecem la urmatoarea...
            x += 1
            continue

        updated_guess = list(guess)
        matched = False
        for i in range(len(word)):
            if i < len(guess) and i < len(word) and guess[i] == "*" and word[i] == alphabet[x]:
                updated_guess[i] = alphabet[x]
                matched = True

        # daca am gasit cuvantul complet, il adaugam in "updated_guess"
        guess = "".join(updated_guess)
        if matched:
            print(f"Cuvant updatat: {guess}, Incercari: {tries}")
        else:
            tries += 1  # incrementam fiecare incercare pana gasim cuvantul complet

        x += 1  # trecem la urmatoarea litera din alfabet

    print(f"Numar total de incercarci: {tries} ;Maximul admis: 1200")
# afisam rezultatul final(numarul max de incercari acceptat 1200)
