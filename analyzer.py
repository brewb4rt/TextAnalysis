

class TextAnalysis:
   # global separators
    separators = ['.', ',', ';', ':', '(', ')', ' ', '-', '[', ']', '{', '}', '?', '!', '&', '/']

    def __init__(self):
        self.current_word = ''
        self.stat=()
        self.words =[]
        self.letters=[]

    def knownObject(self,list, lw):
        for i,sublist in enumerate(list):
            for j,w in enumerate(sublist):
                if lw == w:
                    return (i,j)
                else:
                    return None



    def read(self,text):
        for w in text:
            if not w in TextAnalysis.separators:
                self.current_word += w
                availableLetter = self.knownObject(self.letters,w)
                if availableLetter is not None:
                    print availableLetter
                    print availableLetter
                    self.letters[availableLetter[0]][availableLetter[1]] += 1
                else:
                    self.letters.append([w, 1])
                self.letters.append(w)
            else:
                availableWord = self.knownObject(self.words,self.current_word)
                if availableWord is not None:
                    self.words[availableWord[0]][availableWord[1]] += 1
                else:
                    self.words.append([self.current_word, 1])
                self.current_word = ''

if __name__ == '__main__':
    testText = "Dies ist ein Testtext. Zwei Saetze als Test. Dies Dies Dies"
    TA = TextAnalysis()

    TA.read(testText)
    print TA.letters
    print TA.words
