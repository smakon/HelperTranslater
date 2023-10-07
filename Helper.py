import pyperclip

class Translation():
    def ru_en(self,sentence=""):
        words_ru_en = {"й": "q",
                 "ц": "w",
                 "у": "e",
                 "к": "r",
                 "е": "t",
                 "н": "y",
                 "г": "u",
                 "ш": "i",
                 "щ": "o",
                 "з": "p",
                 "х": "[",
                 "ъ": "]",
                 "ф": "a",
                 "ы": "s",
                 "в": "d",
                 "а": "f",
                 "п": "g",
                 "р": "h",
                 "о": "j",
                 "л": "k",
                 "д": "l",
                 "ж": ";",
                 "э": "'",
                 "я": "z",
                 "ч": "x",
                 "с": "c",
                 "м": "v",
                 "и": "b",
                 "т": "n",
                 "ь": "m",
                 "б": ",",
                 "ю": ".",
                 " ": " ",
                 "@": "@",
                 "?": "?",
                 "!": "!",
                 }
        trans = ""
        for i in range(len(sentence)):
            if sentence[i] in words_ru_en:
                trans += words_ru_en[sentence[i]]
        pyperclip.copy(f"{trans}")
        print(trans)

    def en_ru(self,sentence=""):
        words_en_ru = {"q":"й",
                 "w":"ц",
                 "e":"у",
                 "r":"к",
                 "t":"е",
                 "y":"н",
                 "u":"г",
                 "i":"ш",
                 "o":"щ",
                 "p":"з",
                 "[":"х",
                 "]":"ъ",
                 "a":"ф",
                 "s":"ы",
                 "d":"в",
                 "f":"а",
                 "g":"п",
                 "h":"р",
                 "j":"о",
                 "k":"л",
                 "l":"д",
                 ";":"ж",
                 "'":"э",
                 "z":"я",
                 "x":"ч",
                 "c":"с",
                 "v":"м",
                 "b":"и",
                 "n":"т",
                 "m":"ь",
                 ",":"б",
                 ".":"ю",
                 " ":" ",
                 "@": "@",
                 "?": "?",
                 "!": "!",
                 }
        trans = ""
        for i in range(len(sentence)):
            if sentence[i] in words_en_ru:
                trans += words_en_ru[sentence[i]]
        pyperclip.copy(f"{trans}")
        print(trans)

words_ru = ("й", "ц",
                    "у", "к",
                    "е", "н",
                    "г", "ш",
                    "щ", "з",
                    "х", "ъ",
                    "ф", "ы",
                    "в", "а",
                    "п", "р",
                    "о", "л",
                    "д", "ж",
                    "э", "я",
                    "ч", "с",
                    "м", "и",
                    "т", "ь",
                    "б", "ю")
words_en = ("q", "w",
                    "e", "r",
                    "t", "y",
                    "u", "i",
                    "o", "p",
                    "a", "s",
                    "d", "f",
                    "g", "h",
                    "j", "j",
                    "k", "l",
                    "z", "x",
                    "c", "v",
                    "b",
                    "n", "m")

sentence = input(">>>")
if sentence[0] in words_ru:
    Translation.ru_en(self=" ",sentence=sentence)
elif sentence[0] in words_en:
    Translation.en_ru(self=" ",sentence=sentence)

