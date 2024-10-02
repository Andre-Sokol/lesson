class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        p = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for f_n in self.file_names:                             # Переберите названия файлов и открывайте каждый из них
            with open(f_n, 'r', encoding='utf-8') as file:
                file = file.read().lower()                      # открыавем и переводим вайл в нижний регистр
                for i in p:
                    file = file.replace(i, '')            # Избавьтесь от пунктуации
                    all_words.update({self.file_names: file.split()})  # Создаём словарь

            return all_words

    def find(self, word):
        dictionary = {}
        for name_file, text in self.get_all_words().items():    # перебераем словарь
            if word.lower() in text:                            # ищем совпадение
                for number, list_ in enumerate(text, start=1):  # позиция первого такого слова в списке слов этого файла
                    if word.lower() in list_:
                        dictionary.update({name_file: number})
                        break
        return dictionary

    def count(self, word):
        dict_ = {}
        for name_file, text in self.get_all_words().items(): # перебераем словарь
            word = word.lower()
            if word in text:
                repetition = text.count(word)            # количество слова word в списке слов этого файла
                dict_.update({name_file: repetition})
        return dict_











#
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
