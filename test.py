from cmu2dev import CMU2DEV
from eng2cmu import wordbreak


def _main():
    line = input().strip()
    while line != 'exit':
        cmu = [wordbreak(word)[0] for word in line.split(' ')]
        print(cmu)
        out = [CMU2DEV.convert(word) for word in cmu]
        print(' '.join(out))
        line = input().strip()

if __name__ == "__main__":
    _main()

# what are they thinking cant they turn down the temperature
# उवाठ ऑर दे थिंगख़िंग ख़ैनठ दे ठर्न डावन द ठेमपरचर्

# what conditioner theta consider minute accord evident practice intend concern commit issue approach establish utter
# उवाठ ख़नडिशनर् थेठ ख़नसिडर् मिनठ अख़ौरड एवडनठ परैख़ठस इनठेनड ख़नसर्न ख़मिठ इशू अपरोच इसठैबलिश आठर्

# what which when where why whom whose
# उवाठ उविच उवेन उवेर उवाय हूम हूज़
