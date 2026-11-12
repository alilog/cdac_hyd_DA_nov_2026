def fun():
    "Shivam was a wonder boy for hiss class mates"
    print("Shivam")

# fun()
# print("doc",fun.__doc__)
# print(help(fun))

# pip install thefuzz python-Levenshtein

from thefuzz import fuzz

def calc(a,b):
    print(f"[ {a} ] and [ {b} ]",fuzz.ratio(a,b),sep="\t Ratio :\t")

def calc_partial(a,b):
    print(f"[ {a} ] and [ {b} ]",fuzz.partial_ratio(a,b),sep="\t Partial Ratio:\t")

def calc_sort_ratio(a,b):
    print(f"[ {a} ] and [ {b} ]",fuzz.token_sort_ratio(a,b),sep="\t Sort Ratio:\t")

calc("apple","apple")
calc("apple","aple")
calc("apple","apply")
calc("apple","I love apple pie")
calc_partial("apple","I love apple pie")
calc("data science python","python science data")
calc_partial("data science python","python science data")
calc_sort_ratio("data science python","python science data")
print("=" * 60)

from thefuzz import process

choices = ["Apple", "Banana", "Orange", "Pineapple", "Apples"]

# Find the single best match
best_match = process.extractOne("aple", choices)
print(best_match)  # Output: ('Apple', 90)

# Find top 3 matches
top_matches = process.extract("range", choices, limit=3)
print(top_matches)
print("=" * 60)






