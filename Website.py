import wikipediaapi


class WebsiteConnection:
    def __init__(self, source):
        self.source = source

    def Wikipedia_Connection(self):
        try:
            # Kullanıcı aracısını tanımlayın
            wiki_Tr = wikipediaapi.Wikipedia(
                language='tr',
                user_agent='MyApp/1.0 (myemail@example.com)'  # Kendi kullanıcı aracınızı belirleyin.Wikipedia politikası için gerekli.
            )
            page_Tr = wiki_Tr.page(self.source)

            if page_Tr.exists():
                print("Daha fazlası için: " + page_Tr.fullurl)
                return page_Tr.summary
            else:
                return "İçerik Bulunamadı"

        except Exception as e:
            return f"Hata oluştu: {e}"
