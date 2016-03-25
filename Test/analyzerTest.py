import unittest
import analyzer
import textLoader


class TestAnalyzerMethods(unittest.TestCase):

    testText = "This is a test sentence. This is another test sentence."
    TA = analyzer.TextAnalysis()
    TL = textLoader.textLoader()
    TA.readText(testText.lower())



    print TA.letters
    print TA.words
    print len(TA.letters)
    print len(TA.words)

    def test_letterCount(self):
      self.assertEqual(len(self.TA.letters) , 12)

    def test_difWordCount(self):
      self.assertEqual(len(self.TA.words, 6))



if __name__ == '__main__':
    unittest.main()