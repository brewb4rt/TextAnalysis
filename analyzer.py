##
#@author Danny Behnecke
#@brief calculates some statistical values for a given text
##

from textLoader import textLoader

class TextAnalysis:
    #these characters can separate words
    separators = ['.', ',', ';', ':', '(', ')', ' ', '-', '[', ']', '{', '}', '?', '!', '&', '/']

    def __init__(self):
        self.current_letter = ''
        self.current_word = ''
        self.stat=()
        self.words =[]
        self.letters=[]
        self.text = ''
        self.wordCount = 0
        self.letterCount = 0

    def knownObject(self,list, lw):
        result = None
        for i,sublist in enumerate(list):
            for j,w in enumerate(sublist):
                if lw == w:
                    result = (i,j+1)
                else:
                    pass
        return result


    ##
    #@brief calculates some statistical moments
    #TODO finish function
    #

    def calcStatistic(self):
        tempLetterStat=[]
        tempWordStat = []
        for i, w in enumerate(self.letters):
            tempLetterStat.append([w[0], (w[1]/self.letterCount)])
        for j, v in enumerate(self.words):
            tempWordStat.append([v[0], (v[1]/self.wordCount)])

    ##
    #@param text the text you want to analyze
    #
    def readText(self, text):

        self.wordCount = 0
        self.letterCount = 0

        for i,w in enumerate(text):
            if not w in TextAnalysis.separators:

                self.letterCount += 1
                self.current_letter = w
                self.current_word += w
                availableLetter = self.knownObject(self.letters,self.current_letter)
                if availableLetter is not None:
                    self.letters[availableLetter[0]][availableLetter[1]] += 1
                else:
                    self.letters.append([self.current_letter, 1])

            else:
                availableWord = self.knownObject(self.words,self.current_word)
                if availableWord is not None:
                    self.words[availableWord[0]][availableWord[1]] += 1
                else:
                    if self.current_word is not '':
                        self.words.append([self.current_word, 1])
                self.wordCount += 1
                self.current_word = ''



if __name__ == '__main__':
    testText = "This is a test sentence. This is another test sentence."
    TA = TextAnalysis()
    TL = textLoader()
    TA.readText(testText.lower())

    TA.readText(TL.fromTXT("D:/test.txt"))

    print TA.letters
    print TA.words
