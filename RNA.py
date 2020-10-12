seqs=["UUCGCCGACUGA","AUGCCUUGA","AUGCGGUGAUAA"]
for seq in seqs:
    print(seq)
    if seq.startswith("AUG"):
        print("has start codon")
    if seq.count("UGA")>=0 and not seq.endswith("UGA"):
        print("has selenocysteine")