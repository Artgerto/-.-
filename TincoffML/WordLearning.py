import re
import pickle
import random

class WordLearning(object):
    """Биграммная языковая модель"""

    def fit(self):
        print("Введите путь до файла тестового обучения")
        #alenkiy-cvetochek.txt
        #book_path = "alenkiy-cvetochek.txt"
        book_path = input()
        f = open(book_path, encoding='utf-8')
        dic = {}
        first = []
        for line in f:
            wordList = re.sub("[^\w]", " ",  line).split()
            for i in range(0, len(wordList)): 
                if(i!=len(wordList)-1):
                    if(wordList[i].lower() in dic):
                        array = dic.get(wordList[i].lower()).get("words")
                        last = dic.get(wordList[i].lower()).get("last")
                        if(wordList[i+1][0].isupper()):
                            last = True
                        if (not (wordList[i+1].lower() in array)):
                            array.append(wordList[i+1].lower())
                        dic.update({
                            wordList[i].lower() : {
                                "words": array,
                                "first": wordList[i][0].isupper(),
                                "last": last
                            }
                        })
                    else:
                        dic.update({
                            wordList[i].lower() : {
                                "words": [wordList[i+1].lower()],
                                "first": wordList[i][0].isupper(),
                                "last": wordList[i+1][0].isupper()
                            }
                        })
                    if(wordList[i][0].isupper()):
                        first.append(wordList[i].lower())
        f.close()
        with open('model.pickle', 'wb') as f:
            pickle.dump(dic, f)
        with open('first.pickle', 'wb') as f:
            pickle.dump(first, f)
        



    def generate(self):
        print()
        print("Генерация текста")
        print()
        with open('model.pickle', 'rb') as f:
            dic = pickle.load(f)
        with open('first.pickle', 'rb') as f:
            first = pickle.load(f)
        for i in range(1, 5):
            f = random.choice(first)
            next = (dic.get(f))
            rand = random.randint(3, 5)
            for i in range(1, rand):
                random_next = random.choice(next.get("words"))
                if random_next not in f:
                    f += ' '
                    f += random_next
            f = f.capitalize()
            f += '.'
            print(f)


learning = WordLearning()
learning.fit()
learning.generate()