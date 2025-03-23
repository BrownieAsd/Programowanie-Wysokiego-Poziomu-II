import textanalyzer


class AdvancedTextAnalyzer(textanalyzer.TextAnalyzer):
    def __init__(self, text):
        super(AdvancedTextAnalyzer, self).__init__(text)

    def sentimentAnalysis(self):
        indxsz = 0
        arrpositive = ["wspaniały"]
        arrnegative = ["okropny"]
        txt = self.text.split(" ")
        for word in txt:
            if word in arrpositive:
                indxsz += 1
            if word in arrnegative:
                indxsz -= 1
        if indxsz > 0:
            return print("positive text")
        elif indxsz < 0:
            return print("negative text")
        else:
            return print("neutral text")
