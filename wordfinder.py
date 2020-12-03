import random

class WordFinder:
    """Word Finder: finds random words from a dictionary."""
    
    def __init__(self, filee):
        file = open(filee)
        self.listt = []
        self.words = self.count(file)
        print(f'{len(self.listt)} words read')

    def count(self, file):
        for line in file:
            (self.listt).append(line)

    def random(self):
        return random.choice(self.listt).strip()
        

class RandomWordFinder(WordFinder):
    """ 
    >>> rwf = RandomWordFinder('words.txt')
    235886 words read

    >>> rwf.random() in self.listt
    True

    """
    def __init__(self, filee):
        file = open(filee)
        self.listt = []
        self.words = self.count(file)
        print(f'{len(self.listt)} words read')


    def count(self, file):
        for line in file:
            if line.strip() and not line.startswith('#'):
                (self.listt).append(line)
                
wf = WordFinder("words.txt")
wf.random()



            
    
