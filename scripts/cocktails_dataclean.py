
import pandas as pd
import regex as re

# remove columns that are not required

df = pd.read_csv("cocktails.csv")
df = df.drop(['date_modified', 'glass', 'iba', 'video', 'measure'], axis=1)

# remove apple cider punch #1 from [drink] as it has no alcohol

df = df[~(df.drink.isin(["Apple Cider Punch #1"]))]

# remove Non alcoholic (case insensitive) from [alcoholic]

df = df[~df['alcoholic'].str.contains('non alcoholic', case=False, na=False)]

# remove Ice, Water from [ingredient]

df = df[~(df.ingredient.isin(["Ice", "Water"]))]

# change all ingredients in [ingredient] to title case, change fresh lemon juice to lemon juice, fresh lime juice to lime juice, lemon peel to lemon...
# ...lime peel to lime, orange peel to orange, orange spiral to orange, whipping cream to whipped cream


df['ingredient'] = df['ingredient'].str.capitalize()

replacements = {
    'Fresh lemon juice': ['Lemon'],
    'Fresh lime juice': ['Lime'],
    'Lemon peel': ['Lemon'],
    'Lime peel': ['Lime'],
    'Orange peel': ['Orange'],
    'Orange spiral': ['Orange'],
    'Whipping cream': ['Whipped cream'],
    'Powdered sugar': ['Sugar'],
    'Maraschino cherry': ['Cherry'],
    'Orange juice': ['Orange'],
    'Lemon juice': ['Lemon'],
    'Lime juice': ['Lime'],
    'Cranberry juice': ['Cranberry'],
    'Pineapple juice': ['Pineapple']}

df['ingredient'] = df['ingredient'].replace(replacements)

df.to_csv(r"C:\Users\thous\OneDrive\Desktop\cocktails_data\cocktails_dataclean.csv", encoding='utf-8', index=False)
