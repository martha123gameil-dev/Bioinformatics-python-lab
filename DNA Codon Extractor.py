dna_sequence="ATGCGTAACGTACGTTAG"
codon_list=[]
index=0
while index != len(dna_sequence):
    codon=dna_sequence[index:index+3]
    codon_list.append(codon)
    index+=3
    print (f"the codon is {codon}")
    if codon=="TGA" or codon=="TAG" or codon=="TAA":
        print(f"stop codon {codon} is found at position {index}")
        break
print(f"the exctracted codon is {codon_list}")    