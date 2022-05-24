from sqlalchemy import select

def getMagicKey(category1, category2, category3):
    return (category1*category2*category3%5)+1

""" stmt = select(Movie).where(Movie.preference_key == 1)
print(stmt) """

