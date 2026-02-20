dna_list=["TACCGTACGATCGAT","ACGTGCGGACTGAA","GCGGATTCAGTCAGTC"]
print(dna_list[0][0:3])
dna_list.reverse()
print(dna_list)
dna_list[1]="GGGGGG"+ dna_list[1][6:]
print(dna_list)
Check= "GGGGGG" in dna_list
print(f"if 'GGGGGG' Present in dna_lis {Check}")