sample=input("please enter your samplde").strip().upper()
GC_content=int(input("please enter your percentage"))
if sample[0:3]=="ATG":
    print(f"the start codon {sample[0:3]} is valid")
    if GC_content > 60:
        print("Perfect gene: ready for sequencing") 
    else:
        print("reject not a codon") 
        if "N" in sample:
            print("the sample is contaminated")
        else:
            print("the sample is good")
else:
    print("warning no start codon detected")
 
