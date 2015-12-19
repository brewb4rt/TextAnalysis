class TextAnalysis:

    seperators = ['.', ',', ';', ':', '(', ')', ' ', '-', '[', ']', '{', '}', '?', '!', '&', '/']


    def __init__(self):
        self.current_word = ''
        self.stat=()
        self.words =[]
        self.letters=[]


    def read(self,text):
        for w in text:
            if not self.separators.contains(w):
                self.current_word += w
                self.letters.append(w) #TODO if letter is read twice, increment counter


            else:
                self.words.append(self.current_word)#TODO: if word is read twice, increment counter
                self.current_word = ''
