"""
uppercase_word_at(s, index): takes a string s and an integer index
as parameters and returns a string which is identical to s except
the letters in s starting from the specified index up to the first
space character are capitalized.
"""


def uppercase_word_at(x, y):
    news = x[0:y] + x[y:len(x)].upper()
    for a in range(0, len(news)):
        if news[a] == " ":
            if a > num:
                return news[0:a] + news[a:len(news)].lower()
    return news
