# autocomplete

AutoComplete word "search" engine. Connects to redis and exposes 2 APIs (using Flask): "Store" a given word and "Suggest" a completion for a given word. gui.py contains a preview of how to use those apis + example of storing words from csv is found in main.py.

Suggest takes 12~ ms for receiving a word with redis containing 330K words + score.
Storage is implemented as a variance of reverse index on redis, when all prefixes of a word is indexed as Prefix -> word.
For example, storing "Rocky" will result in: "_R->Rocky", "_Ro->Rocky)", "_Roc->Rocky)", "_Rock->Rocky)", "_Rocky->Rocky)"

## References:
1) https://gist.github.com/emrahayanoglu/e28510026b6119bb276b4f00eb766e24
2) https://thedatasingh.medium.com/autocomplete-using-redis-and-python-in-40-lines-78b95e36e5e1
3) 330K words + frequenices csv file: https://www.kaggle.com/rtatman/english-word-frequency
