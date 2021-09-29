from SA_SearchEngine.alphabetize import Alphabetize

ab = Alphabetize()
new = ["aA"]
sorted = ["a", "b", "d", "e", "f"]

ab.addLines(new,sorted)
print(sorted)