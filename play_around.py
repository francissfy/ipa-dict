# CREATED BY SHEN FEIYU
import os
from typing import List

class IPAConverter:
    """convert words to correspnding ipa notations
    """
    def __init__(self, langs: List[str]):
        dirs = os.listdir()
        if "data" not in dirs:
            assert(0), "Wrong working directory, data dir not found"
        self.ipa_dict = {}
        for lang in langs:
            filename = lang + ".txt"
            ipa_files = os.listdir("./data")
            assert(filename in ipa_files), "{} not found, available: {}".format(lang, ' '.join([t.split('.')[0] for t in ipa_files]))
            self.ipa_dict[lang] = {}
            dict  = self.ipa_dict[lang]
            with open("./data/"+filename, 'r') as f:
                while True:
                    line = f.readline()
                    if line == "":
                        break
                    tmp = line.strip().split('\t')
                    dict[tmp[0]] = tmp[1]
        

    def get_ipa(self, word: str, lang: str) -> str:
        if lang not in self.ipa_dict:
            print("language {} not initialized".format(lang))
            return None
        dict = self.ipa_dict[lang]
        if word not in dict:
            print("word {} not found in language {}".format(word, lang))
            return None
        return dict[word]


    def get_batch_ipa(self, words: List[str], langs: List[str]) -> List[str]:
        ipas = [self.get_ipa(w, l) for w, l in zip(words, langs)]
        return ipas


if __name__ == "__main__":
    c = IPAConverter(["en_US", "zh_hans"])
    print(c.get_batch_ipa(["python", "命运"], ["en_US", "zh_hans"]))

