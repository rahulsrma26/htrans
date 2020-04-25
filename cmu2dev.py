'''
CMU Phoneme format to Devnagri utf-8 converter
'''

class CMU2DEV:

    PHONEMES = {
        'AA': ['ऑ','ॉ'],
        'AE': ['एै','ै'],
        'AH0': ['अ',''],
        'AH': ['आ','ा'],
        'AO': ['औ','ौ'],
        'AW': ['आव','ाव'],
        'AY': ['आय','ाय'],
        'B': ['ब'],
        'CH': ['च'],
        'D': ['ड'],
        'DH': ['द'],
        'EH': ['ए', 'े'],
        'ER': ['र्'],
        'EY': ['ऐ','े'],
        'F': ['फ़'],
        'G': ['ग'],
        'HH': ['ह'],
        'IH': ['इ','ि'],
        'IY': ['ई','ी'],
        'JH': ['ज'],
        'K': ['ख़'],
        'L': ['ल'],
        'M': ['म'],
        'N': ['न'],
        'NG': ['ंग'],
        'OW': ['ओ','ो'],
        'OY': ['ओए','ोए'],
        'P': ['प'],
        'R': ['र'],
        'S': ['स'],
        'SH': ['श'],
        'T': ['ठ'],
        'TH': ['थ'],
        'UH': ['उ','ु'],
        'UW': ['ऊ','ू'],
        'V': ['व'],
        'W': ['उव'],
        'Y': ['य'],
        'Z': ['ज़'],
        'ZH': ['ज़ॅ']
    }

    @staticmethod
    def convert(ary):
        '''
        Expects a list of CMU Phonemes and returns utf-8 encoded devnagri word
        '''
        string = ''
        for elem in ary:
            if elem not in CMU2DEV.PHONEMES and (elem[-1] == '0' or elem[-1] == '1' or elem[-1] == '2'):
                elem = elem[:-1]
            if elem not in CMU2DEV.PHONEMES:
                raise ValueError(f'Invalid phoneme "{elem}"')
            l = CMU2DEV.PHONEMES[elem]
            string += l[0] if len(l) > 1 and string == '' else l[-1]
        return string
