import indicoio
indicoio.config.api_key = 'f813d87aeb7c1fec9b38a95f466c414f'

# TODO: improve values?
PASSING_GRADE = 0.56
# the following constants should add up to 1.0
SENTIMENT_WEIGHT = 0.35
ANGER_WEIGHT     = 0.25
SADNESS_WEIGHT   = 0.24
FEAR_WEIGHT      = 0.09
SURPRISE_WEIGHT  = 0.07

#---------------------------------------

def grade(input):
    "Call this function before reading aloud any Reddit text to check if it passes standards"

    # Using the constants listed above, calculate the weighted average of the parameters
    mark = (SENTIMENT_WEIGHT * indicoio.sentiment(input))

    emotion = indicoio.emotion(input)

    mark += (ANGER_WEIGHT * ( 1 - emotion['anger'])) \
          + (SADNESS_WEIGHT * (1 - emotion['sadness'])) \
          + (FEAR_WEIGHT * (1 - emotion['fear'])) \
          + (SURPRISE_WEIGHT * (1 - emotion['surprise']))

    if mark >= PASSING_GRADE:
        return True
    else:
        return False

#-------------------------------

# accepts a list
# returns a dictonary
def gradeMultiple(inputList):
    "Call this function when multiple lines need to be checked"

    # dictonary with numLines number of elements that will contain the marks of all the lines in order of appearance in inputList
    lines = {}

    # for loop that will get the marks of all elements in inputList (assume inputList is a list of strings)
    for i in inputList:
        lines[i] = indicoio.sentiment(i)
        if lines[i] > 0.5:
            lines[i] = "Positive"
        else:
            lines[i] = "Negative"

    return lines

#------------------------------

def sortByGrades(inputDict):
    "Sorts the given dictionary by returning a new dictonary where all the elements with a value of True are first"

    # new dictonary
    sortedDict = {}

    first = []
    second = []

    # loop through the inputDict and determine which elements have values of True
    for k, v in inputDict.iteritems():
        if v == True:
            first.append(k)
        else:
            second.append(k)

    # find the number of items in inputDict
    numItems = inputDict.keys().size()


    return
