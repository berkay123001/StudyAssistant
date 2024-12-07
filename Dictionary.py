import nltk
from nltk.corpus import wordnet

# NLTK veritabanını indiriyoruz (sadece bir kez çalıştırmanız yeterli)
nltk.download("wordnet")

class Sozluk:
    def __init__(self, vocabulary):
        self.vocabulary = vocabulary

    def wordnet_lookup(self):
        """Verilen kelimenin anlamlarını ve örnek cümlelerini getirir."""
        anlamlar = wordnet.synsets(self.vocabulary)
        if anlamlar:
            for index, anlam in enumerate(anlamlar, start=1):
                print(f"{index}. Anlam: {anlam.definition()}")
                if anlam.examples():
                    print("   Örnek Cümleler:")
                    for example in anlam.examples():
                        print(f"   - {example}")
                else:
                    print("   Örnek Cümle bulunamadı.")
                print()
        else:
            print("Kelime bulunamadı.")