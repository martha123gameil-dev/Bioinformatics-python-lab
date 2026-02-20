gene_list=[("gene1","ATGCGTAACGTAC",95),("gene2","GCACGTAACGTTACG",78),("gene3","TAGGTCACCGTACGTAACG",85)]
gene1_set=set(gene_list[0][1])
print(f"the first DNA of first gene is: {gene1_set}")
new_gene=input("please enter the new gene").upper().strip()
score=85
dic=dict.fromkeys(new_gene,score)
print(f"the new gene and its score is: {dic}")
G_content=gene_list[0][1].count("G")
C_content=gene_list[0][1].count("C")
LENGHT=len(gene_list[0][1])
GC_content=(G_content+C_content)/LENGHT*100
print(f"the GC content of the first gene is : {GC_content}")
