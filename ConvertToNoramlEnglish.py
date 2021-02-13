# Some operators have accents in their name. In ScrapeOperatorsicon.py, it scrapes all operator's icons' URL and make a dictionary as (key : Operator Name) : (Value : URL)
# But name like 'jäger' it has accents. Through this code, you can convert to normal english even if there's accents

import unicodedata

def convertToNormalEnglish(text):
    return ''.join(char for char in unicodedata.normalize('NFKD', text) if unicodedata.category(char) != 'Mn')
