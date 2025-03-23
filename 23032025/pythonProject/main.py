import textanalyzer
import advancedtextanalyzer
import smartphone
import userauth

if __name__ == '__main__':
    #zad1
    text1 = textanalyzer.TextAnalyzer("bardzo lubie wode aguaro wode te bardzo chetnie pije")
    text1.char_counter()
    text1.word_counter()
    text1.unique_words()

    text2 = advancedtextanalyzer.AdvancedTextAnalyzer("To był naprawdę wspaniały dzień")
    text2.sentimentAnalysis()

    text2 = advancedtextanalyzer.AdvancedTextAnalyzer("To był naprawdę wspaniały i okropny dzień")
    text2.sentimentAnalysis()
    #zad2
    sphone1 = smartphone.Smartphone("Apple", "iPhone", "Kinga", "Siema, czy tez lubisz wode saguaro?", "Goodmorning")
    sphone1.send_text()
    sphone1.play_song()
    #zad3
    auth = userauth.UserAuth({"admin": "1234", "user": "abcd"})
    try:
        auth.login("admin", "1234")
    except Exception as e:
        print(f"Błąd:{e}")
    try:
        auth.login("tomm", "2137")
    except Exception as e:
        print(f"Błąd:{e}")
    try:
        auth.login("user", "4201")
    except Exception as e:
        print(f"Błąd:{e}")
