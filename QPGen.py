'''
QPGen v1.0
    A question paper generator based on number of marks and distribution of marks based 
    on levels of difficulty."
'''

from res.QReader import QReader
from res.QSelector import QSelector

selectedQuestions = []

def calcLevelMarks(level):
    maxMarks = reader.read_maxmarks()
    levelMarkPerc = reader.read_level(level)
    return int((levelMarkPerc / 100) * maxMarks) 


reader = QReader("QList.json")

total = reader.read_total()
levels = ["easy", "medium", "hard"]

levelwiseMarks = dict(zip(levels, list(map(calcLevelMarks, levels))))

print("\n\n> Levels & Marks\n\tEasy: %(easy)d\n\tMedium: %(med)d\n\tHard: %(hard)d" % \
     { "easy": levelwiseMarks["easy"], "med": levelwiseMarks["medium"], "hard": levelwiseMarks["hard"]})

selector = QSelector()

for k, v in levelwiseMarks.items():
    selectedQuestions.extend(selector.select(k, v))

print("\n> Selected Questions\n\tQID \t\tDIFFICULTY\t\tMARKS")
for question in selectedQuestions:
    print("\t{}\t\t{}\t\t\t{}".format(question["qID"], question["difficulty"], question["marks"]))






