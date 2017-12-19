from collections import Counter

class DNA():
    ''' This class allows for basic manipulations of DNA sequences as well as
    a determiniation of some sequence characteristics '''

    def __init__(self, sequence):
        ''' Initalize with a DNA sequence(str) of choice '''
        self.sequence = sequence.lower()
        self.bases = ['a', 't' , 'c', 'g']
        self.basecomplement = {'a': 't', 'c': 'g', 'g': 'c', 't': 'a'}

    def complement(self):
        ''' Return the complementary sequence string '''
        bases = list(self.sequence)
        comp = [self.basecomplement[base] for base in bases]
        return ''.join(comp)

    def reverse(self):
        ''' Reverses the sequence string '''
        reverse = self.sequence[::-1]
        return reverse

    def reverse_complement(self):
        ''' Gives the reverse complement of the sequence '''
        reverse = self.sequence.reverse()
        reverse_comp = reverse.complement()
        return reverse_comp

    def count_bases(self):
        ''' Returns a dictionary with the base count '''
        count_dict = Counter(self.sequence)
        return count_dict

    def melting_temp(self):
        ''' Determines the melting temperature for a DNA sequence '''
        count = self.sequence.count_bases()
        return 4*(count['c'] + count['g']) + 2*(count['a'] + count['t'])

    def DNA_to_RNA(sequence):
        ''' Gives the RNA sequence for the given DNA sequence '''
        RNA = sequence.replace('T', 'U')
        return RNA


def nucleotide_count_TM(sequence):
    A_count = sequence.count('A')
    C_count = sequence.count('C')
    G_count = sequence.count('G')
    T_count = sequence.count('T')
    TM = 4*(C_count + G_count) + 2*(A_count + T_count)
    TM = str(TM)
    A_count = str(A_count)
    C_count = str(C_count)
    G_count = str(G_count)
    T_count = str(T_count)
    print 'Melting Temp = ' + TM
    print 'A = ' + A_count
    print 'C = ' + C_count
    print 'G = ' + G_count
    print 'T = ' + T_count
    print 'Sequence ends in G = ' + str(sequence[-1] == 'G')
    print 'Sequence ends in C = ' + str(sequence[-1] == 'C')



if __name__ == '__main__':

    seq1 = DNA("GCCCGATAGTTCGGTACGAGG")

    print(seq1.reverse_complement())
    print(seq1.count_bases())
    print(seq1.melting_temp())
    print(seq1.DNA_to_RNA())

    seq2 = DNA('TCGTCCTGTACCTGTCCGAATAGAGTATCGTCGCATCGATTTGAACCCTACTATGGCATTGATACCAATGCTCTGAGGGTGTTAAAGTTCCGGAAACACAAGAATACGAGTAATGTACGCTGGGCTAAACTGCTAGCACCTCGGGTTGTGTCACTATAGCAAGGGATGATTAACGTTACACGCACCGGCTACATGGGCAGTAGGCGCGGTGGCGTCTTGTACGATCGTTGGCCCTTGTACTTGTTGAAAGATTCGACTTCGATGGAGTCACCCAAGGTTAGGTATCCATGAGTATTTCATCCGAATGCATCATCACCCTTCGAGTTCGTAATACGAAATAACGATGGGATACTTCATTTCGCAAGAGCGTAATTGTTAGGACTGAGGTGCGTGGCAACGGGTACTGCGTGAGCACCGCAACCGACTTGCGACATTCTAACGCCTGGTGTCCCCGCACTCGGTCATTGCGGTTTTGGTTAACGCAGAATGGCTTACTGAGACCGGTCTGTAATGGTCCGTACTGCGGGGTGTCCTACCGCTGGCTCAAACTCATCAAATGACCGGTGTGGCGACCTCCTTAGTTGTGATTAATAAAACTCGTGATGTCCAAAGGTCGCAGCGACTCCCTGATACGCCTCATTCAGTCAGGTAATGCAGACTACCATTCATGTGTGTGAGCGACCGGTGGTTAGTTTTGTCAATACACCCGGAGTTCGATGCACCGGAGCCAGACGAGCACTATGTATCCCGTCCACCGGCCCCTGGCCCTTCCTACTACTGTAAATAAACTGGTTAGCTTCCGAAATGCCGGCTAGTGGAACAATCTGTTTCAGAAATGGTCGCTACACACAAACCTGACTTAGTCGCTATGAATGACGTGAATACAAGCCCTTACTAGGAATTGTAGGTCGGTACATAGACTACGGTGCAGTGGAGCTAGTCGCTAAATT')

    print(seq2.reverse_complement())
    print(seq2.count_bases())
    print(seq2.melting_temp())
    print(seq2.DNA_to_RNA())
