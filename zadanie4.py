import pymorphy2
numerals234 = 'два, три, четыре'
numerals1 = 'один'

morph = pymorphy2.MorphAnalyzer()

noun = input("Введите существительное: ")
verb = input("Введите глагол: ")
adjective = input("Введите прилагательное: ")
numeral = input("Введите числительное: ")
if numeral in numerals1:
      print(f"У меня есть {(morph.parse(numeral)[0].inflect({'nomn'})).word} {(morph.parse(noun)[0].inflect({'sing', 'nomn'})).word}.\n"
            f"Днем я люблю {(morph.parse(verb)[0].inflect({'INFN'})).word} со своим {(morph.parse(adjective)[0].inflect({'sing', 'ablt'})).word} "
            f"{(morph.parse(noun)[0].inflect({'sing', 'ablt'})).word}.")
elif numeral in numerals234:
      print(f"У меня есть {(morph.parse(numeral)[0].inflect({'nomn'})).word} {(morph.parse(noun)[0].inflect({'sing', 'gent'})).word}.\n"
            f"Днем я люблю {(morph.parse(verb)[0].inflect({'INFN'})).word} со своими {(morph.parse(adjective)[0].inflect({'ablt', 'plur'})).word} "
            f"{(morph.parse(noun)[0].inflect({'plur', 'ablt'})).word}.")
else:
      print(f"У меня есть {(morph.parse(numeral)[0].inflect({'nomn'})).word} {(morph.parse(noun)[0].inflect({'plur', 'gent'})).word}.\n"
            f"Днем я люблю {(morph.parse(verb)[0].inflect({'INFN'})).word} со своими {(morph.parse(adjective)[0].inflect({'plur', 'ablt'})).word} "
            f"{(morph.parse(noun)[0].inflect({'plur', 'ablt'})).word}.")



