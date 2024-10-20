questions = ("Periyodik tabloda kaç tane element vardır: ",
             "En büyük yumurta hangi hayvana aittir: ",
             "Atmosferde bulunan gazlardan en yüksek orana sahip olan hangisidir: ",
             "Türkiye'nin başkenti neresidir: ",
             "Güneş sistemindeki en sıcak gezeken hangisidir: ")

options = (("A. 116", "B. 117", "C. 118", "D. 119"),
           ("A. Balina", "B. Fil", "C. Penguen", "D. Devekuşu"),
           ("A. Azot", "B. Karbondioksit", "C. Oksijen", "D. Hidrojen")
           ,("A. Ankara", "B. İstanbul", "C. Malatya", "D. Malazgirt")
           ,("A. Merkür", "B. Venüs", "C. Dünya", "D. Mars"))

answers = ("C", "D", "A", "A", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Cevap giriniz (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("DOĞRU")
    else:
        print("YANLIŞ")
        print(f"DOĞRU CEVAP: {answers[question_num]}")
    question_num += 1


print("------------------------")
print("        RESULTS         ")
print("------------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Skorunuz: {score}%")