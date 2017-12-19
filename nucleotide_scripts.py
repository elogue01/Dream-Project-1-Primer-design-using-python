from collections import Counter

class DNA():
    ''' This class allows for basic manipulations of DNA sequences as well as
    a determiniation of some sequence characteristics '''

    def __init__(self, sequence):
        ''' Initalize with a DNA sequence(str) of choice '''
        self.sequence = sequence.lower()
        self.bases = ['a', 't' , 'c', 'g']
        self.basecomplement = {'a': 't', 'c': 'g', 'g': 'c', 't': 'a'}

    def complement(self,sequence):
        ''' Return the complementary sequence string '''
        bases = list(sequence)
        comp = [self.basecomplement[base] for base in bases]
        return ''.join(comp)

    def reverse(self, sequence):
        ''' Reverses the sequence string '''
        reverse = self.sequence[::-1]
        return reverse

    def reverse_complement(self):
        ''' Gives the reverse complement of the sequence '''
        reverse = self.reverse(self.sequence)
        reverse_comp = self.complement(reverse)
        return reverse_comp

    def count_bases(self):
        ''' Returns a dictionary with the base count '''
        count_dict = Counter(self.sequence)
        return count_dict

    def melting_temp(self):
        ''' Determines the melting temperature for a DNA sequence '''
        count = self.count_bases()
        return 4*(count['c'] + count['g']) + 2*(count['a'] + count['t'])

    def DNA_to_RNA(self):
        ''' Gives the RNA sequence for the given DNA sequence '''
        RNA = self.sequence.replace('t', 'u')
        return RNA


if __name__ == '__main__':

    seq1 = DNA("GCCCGATAGTTCGGTACGAGG")
    print(seq1.reverse_complement())
    print(seq1.count_bases())
    print(seq1.melting_temp())
    print(seq1.DNA_to_RNA())
