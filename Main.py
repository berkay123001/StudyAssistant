
from QuizGenerator.Sozluk import Sozluk
from SimpleQuizGenerator.Translator import TranslatorService
from SimpleQuizGenerator.UserManager import UserManager
from SimpleQuizGenerator.Voice_Recorder import VoiceRecorder
from SimpleQuizGenerator.Website import WebsiteConnection


def website_menu():
    print("----------Websites-----------")
    print("1-Wikipedia")
    secim = input("İşlem seçiniz")
    if secim == "1":
        source = input("Lütfen aramak istediğiniz konuyu giriniz: ")
        ConnectionWebsite = WebsiteConnection(source)
        ozet=ConnectionWebsite.Wikipedia_Connection()
        print(ozet)


def Translate_Menu():
    while True:
        print("\n--- Çeviri Menüsü ---")
        print("1. Sessiz Çeviri")
        print("2. Sesli Çeviri")
        print("3. Sözlük")
        print("4. Çıkış")

        secim = input("Bir seçenek seçin (1-3): ")

        if secim == "1":
            kaynak_metin = input("Çevirmek istediğiniz metni girin: ")
            hedef_dil = input("Hedef dilin kodunu girin (ör. 'tr' için Türkçe, 'en' için İngilizce): ")
            translator = TranslatorService(kaynak_metin, hedef_dil)
            ceviri = translator.translate()
            print(f"Çeviri: {ceviri}")

        elif secim == "2":
            kaynak_dil = int(input("Kaynak dil kodunu girin (1-Türkçe, 2-İngilizce): "))

            if kaynak_dil == 1:
                hedef_dil = input("Hedef dilin kodunu girin (1-en): ").strip()
                if hedef_dil == "1":
                    recorder = VoiceRecorder()
                    tr_metin = recorder.dinlemeyi_baslat_Tr()
                    print(tr_metin)
                    translator = TranslatorService(tr_metin, "en")
                    ceviri = translator.translate()
                    print(f"Çeviri: {ceviri}")
                else:
                    print("Lütfen geçerli bir kod giriniz.")

            elif kaynak_dil == 2:
                hedef_dil = input("Hedef dilin kodunu girin (1-tr): ").strip()
                if hedef_dil == "1":
                    recorder = VoiceRecorder()
                    en_metin = recorder.dinlemeyi_baslat_En()
                    print(en_metin)
                    translator = TranslatorService(en_metin, "tr")
                    ceviri = translator.translate()
                    print(f"Çeviri: {ceviri}")
                else:
                    print("Lütfen geçerli bir kod giriniz.")
            else:
                print("Geçersiz kaynak dil kodu.")


        elif secim=="3":

            kelime = input("Çevirmek istediğiniz kelimeyi giriniz: ")
            sozluk = Sozluk(kelime)
            sozluk.wordnet_lookup()

        elif secim == "4":
            print("Çıkış yapılıyor...")
            break

        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")


def main_menu():
    user_manager = UserManager()

    while True:
        print("\n--- Ana Menü ---")
        print("1. Kullanıcı Kaydı")
        print("2. Giriş Yap")
        print("3. Çıkış")

        choice = input("Seçiminizi yapın (1-3): ")

        if choice == "1":
            username = input("Kullanıcı adı: ").strip()
            password = input("Şifre: ").strip()
            success, message = user_manager.register_user(username, password)
            print(message)

        elif choice == "2":
            username = input("Kullanıcı adı: ").strip()
            password = input("Şifre: ").strip()
            success, message = user_manager.login_user(username, password)
            print(message)
            if success:
                print("Hangi menüye geçmek istiyorsunuz?")
                print("1-Çeviri")
                print("2-Website")
                secim=input("İşlem seçiniz")
                if secim=="1":
                    Translate_Menu()
                    break
                elif secim=="2":
                    website_menu()
                    break

        elif choice == "3":
            print("Çıkış yapılıyor...")
            break

        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")


if __name__ == "__main__":
    main_menu()
