# trivial_compression.py
"""
Compress a string representation of a DNA sequence into a 2-bit-per-nucleotide bit string.
"""
from rich import print
import sys
from typing import *


class CompressedGene:
    
    def __init__(self, gene: str) -> None:
        self._compress(gene)
    
    def _compress(self, gene: str) -> None:
        """
        Compress genes so that `self.bit_string` encodes gene string from right to left.
        """
        self.bit_string: int = 1 # sentinel
        
        for nucleotide in gene.upper():
            self.bit_string <<= 2 # add two 0's to the right side to make space for the next nucleotide
            match nucleotide:
                case 'A':
                    self.bit_string |= 0b00	
                case 'C':
                    self.bit_string |= 0b01
                case 'G':
                    self.bit_string |= 0b10
                case 'T':
                    self.bit_string |= 0b11
                case _:
                    raise ValueError(f'Invalid nucleotide: {nucleotide}')
    
    def decompress(self) -> str:
        """
        `self.bit_string` sequences DNA backwards,
        so return the reversed string reprsentation to get the original gene.
        """
        gene: str = ''
        for i in range(0, self.bit_string.bit_length() - 1, 2):
            # subtract by 1 to exclude the last two bits, which is the sentinel
            match bit := self.bit_string >> i & 0b11:
                case 0b00:
                    gene += 'A'
                case 0b01:
                    gene += 'C'
                case 0b10:
                    gene += 'G'
                case 0b11:
                    gene += 'T'
                case _:
                    raise ValueError(f'Invalid bit: {bit}')
        
        return gene[::-1]
    
    def __str__(self) -> str:
        return self.decompress()


if __name__ == '__main__':
    original: str = 'TAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATATAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATA' * 100
    print(f"original is {sys.getsizeof(original)} bytes")
    
    compressed: CompressedGene = CompressedGene(original)
    print(f"compressed gene is {sys.getsizeof(compressed)} bytes")
    
    print(compressed)
    
    assert original == compressed.decompress()
    print('Original and decompressed are the same')