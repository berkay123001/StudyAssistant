import speech_recognition as sr
import keyboard


class VoiceRecorder:
    def __init__(self):
        self.taniyici = sr.Recognizer()
        self.mikrofon = sr.Microphone()

    def dinlemeyi_baslat_Tr(self):
        print("Dinlemeye hazır. 'a' tuşuna basınca dinleme başlıyor, 'q' tuşuna basınca duruyor.")
        while True:
            if keyboard.is_pressed("a"):
                print("Dinlemeye başlandı... 'q' tuşuna basarak durdurabilirsiniz.")
                with self.mikrofon as kaynak:
                    self.taniyici.adjust_for_ambient_noise(kaynak)
                    ses = self.taniyici.listen(kaynak)
                print("Ses kaydedildi, metne çevriliyor...")

                try:
                    metin = self.taniyici.recognize_google(ses, language="tr-TR")
                    return metin  # Metni return ederek döndürme
                except sr.UnknownValueError:
                    print("Sesi anlayamadım.")
                    return None
                except sr.RequestError:
                    print("İnternet bağlantısı hatası.")
                    return None

    def dinlemeyi_baslat_En(self):
        print("Dinlemeye hazır. 'a' tuşuna basınca dinleme başlıyor, 'q' tuşuna basınca duruyor.")
        while True:
            if keyboard.is_pressed("a"):
                print("Dinlemeye başlandı... 'q' tuşuna basarak durdurabilirsiniz.")
                with self.mikrofon as kaynak:
                    self.taniyici.adjust_for_ambient_noise(kaynak)
                    ses = self.taniyici.listen(kaynak)
                try:
                    metin = self.taniyici.recognize_google(ses, language="en-US")
                    return metin  # Metni return ederek döndürme
                except sr.UnknownValueError:
                    print("Sesi anlayamadım.")
                    return None
                except sr.RequestError:
                    print("İnternet bağlantısı hatası.")
                    return None




