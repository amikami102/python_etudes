# dna_search.py
"""
A script implementing DNA search.

A nucleotide is represented by A, C, G, and T.
A codon is composed of three nucleotides.
A gene is composed of multiple codons.
"""
from rich import print
from enum import Enum
from typing import *


class Nucleotide(str, Enum):
    ADENINE = 'A'
    CYTOSINE = 'C'
    GUANINE = 'G'
    THYMINE = 'T'
    
Codon = tuple[Nucleotide, Nucleotide, Nucleotide]
Gene = list[Codon]


def slice_by_three(s: str) -> Iterator[tuple[str]]:
    """
    Slice a string of characters into chunks of length 3.
    """
    it = [iter(s)] * 3
    return zip(*it)


def string_to_gene(s: str) -> Gene:
    """
    Convert a gene string (string of 'A', 'C', 'G', 'T') into Gene object.
    """
    gene: Gene = []
    for (first, second, third) in slice_by_three(s):
        codon: Codon = Nucleotide(first), Nucleotide(second), Nucleotide(third)
        gene.append(codon)
    return gene


def binary_contains(gene: Gene, key: Codon) -> bool:
    """
    Binary search the given codon `key` in `gene`.
    Use Python's lexicographical comparison to locate `key` in `gene`.
    """
    low: int = 0
    high: int = len(gene) - 1
    while low <= high:
        mid: int = (low + high) // 2
        if gene[mid] < key:
            low = mid + 1
        if gene[mid] > key:
            high = mid - 1
        else:
            return True
    return False


if __name__ == '__main__':
    
    gene_str: str = 'ACGTGGCTCTCTAACGTACGTACGTACGGGGTTTATATATACCCTAGGACTCCCTTT'
    
    # test Nucleotide, Codon, and Gene instantiation
    a, g, t = Nucleotide('A'), Nucleotide('G'), Nucleotide('T')
    
    # test slice_by_three()
    grouped_by_three = [sliced for sliced in slice_by_three(gene_str)]
    assert all(len(group) for group in grouped_by_three)
    assert len(grouped_by_three) == len(gene_str) // 3
    
    # test string_to_gene()
    my_gene: Gene = string_to_gene(gene_str)
    
    # binary_contains()
    my_gene.sort()
    print(my_gene)
    acg: Codon = tuple(map(Nucleotide, 'ACG'))
    gat: Codon = tuple(map(Nucleotide, 'GAT'))
    assert (acg in my_gene) == binary_contains(my_gene, acg)
    assert (gat not in my_gene) == binary_contains(my_gene, gat)
    