# Prints the list of [ingredient] and [measure] of a specific cocktail after i type in the name of the cocktail
# Recommend drink after user input two ingredients

import pandas as pd

df = pd.read_csv("cocktails.csv")   # ***
qn1 = str(input('Is this enquiry about cocktail or ingredient?'))
qn2 = None

def get_cocktail(qn2):
    global df
    qn2 = str(input('Please enter the name of cocktail:'))
    df = df.loc[df['drink'] == qn2, ('ingredient', 'measure')]
    print(df.to_string(index=False))

def get_ingredient(qn2):
    global df    # do not need to put 'global df' if you define *** df at the start; the df is considered a local variable within this function; if you define it at start, it will become global variable- eg. def get_file(df)
    qn2 = str(input('Please enter the name of ingredient:'))
    df = df.loc[df['ingredient'] == qn2, 'drink']
    print(df.to_string(index=False))

if qn1 == "cocktail":
    get_cocktail(qn2)

elif qn1 == "ingredient":
    get_ingredient(qn2)
