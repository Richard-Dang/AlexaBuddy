import indicoio
indicoio.config.api_key = 'f813d87aeb7c1fec9b38a95f466c414f'

PASSING_GRADE = 0.56

# TODO: improve values?
# the following constants should add up to 1.0
SENTIMENT_WEIGHT = 0.35
ANGER_WEIGHT     = 0.25
SADNESS_WEIGHT   = 0.24
FEAR_WEIGHT      = 0.09
SURPRISE_WEIGHT  = 0.07

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
