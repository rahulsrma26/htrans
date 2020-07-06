import nltk
from functools import lru_cache
from itertools import product as iterprod

try:
    arpabet = nltk.corpus.cmudict.dict()
except LookupError:
    nltk.download('cmudict')
    arpabet = nltk.corpus.cmudict.dict()

def main():
    print(wordbreak('nation'))

@lru_cache()
def wordbreak(s):
    # print(f's: "{s}"')
    s = s.replace("'", "").replace('"', '')
    s = s.lower()
    if s in arpabet:
        return arpabet[s]
    middle = len(s)/2
    partition = sorted(list(range(len(s))), key=lambda x: (x-middle)**2-x)
    # print(f'partition: "{partition}"')
    for i in partition:
        pre, suf = (s[:i], s[i:])
        if pre in arpabet and wordbreak(suf) is not None:
            return [x+y for x,y in iterprod(arpabet[pre], wordbreak(suf))]
    return None

if __name__ == '__main__':
    main()
