from SimpleQuizGenerator.Translator import TranslatorService
from SimpleQuizGenerator.Voice_Recorder import VoiceRecorder


def ana_menu():
    while True:
        print("\n--- Çeviri Menüsü ---")
        print("1. Sessiz Çeviri")
        print("2. Sesli Çeviri")
        print("2. Çıkış")

        secim = input("Bir seçenek seçin (1-2): ")

        if secim == "1":
            kaynak_metin = input("Çevirmek istediğiniz metni girin: ")
            hedef_dil = input("Hedef dilin kodunu girin (ör. 'tr' için Türkçe, 'en' için İngilizce): ")
            Translator = TranslatorService(kaynak_metin, hedef_dil)
            ceviri = Translator.translate()
            print(f"Çeviri: {ceviri}")

        elif secim == "2":

            kaynak_dil=int(input("Kaynak dil kodunu girin (1-tr,2-en)"))

            if kaynak_dil==1:
                hedef_dil = input("Hedef dilin kodunu girin (1-en) ")

                if hedef_dil == "1":
                    TryRecorder = VoiceRecorder()
                    Tr_metin = TryRecorder.dinlemeyi_baslat_Tr()
                    print(Tr_metin)
                    Translator = TranslatorService(Tr_metin, "en")
                    ceviri = Translator.translate()
                    print(f"Çeviri: {ceviri}")

                if hedef_dil == "2":
                  pass

                else:
                    print("Lütfen geçerli bir kod giriniz")

            if kaynak_dil==2:
                hedef_dil = input("Hedef dilin kodunu girin (1-Tr) ")

                if hedef_dil=="1":
                    TryRecorder = VoiceRecorder()
                    En_metin = TryRecorder.dinlemeyi_baslat_En()
                    print(En_metin)
                    Translator = TranslatorService(En_metin, "tr")
                    ceviri = Translator.translate()
                    print(f"Çeviri: {ceviri}")

                else:
                    print("Lütfen geçerli bir kod giriniz")


        elif secim == "3":
            print("Çıkış yapılıyor...")
            break


if __name__ == "__main__":
    ana_menu()