from translate import Translator

with open("5_4.txt", "r", encoding='utf-8') as nums_file:
    with open("5_4_out.txt", "a", encoding='utf-8') as out_file:
        for line in nums_file:
            translator = Translator(to_lang="Russian")
            translation = translator.translate(line.split()[0])
            out_file.write(line.replace(line.split()[0], translation, 1), )
