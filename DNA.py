def DNA_strand(dna):
    # code here
    s = list(dna)
    i = 0
    for c in s:
        if c == 'A':
            s[i] = 'T'
        if c == 'T':
            s[i] = 'A'
        if c == 'C':
            s[i] = 'G'
        if c == 'G':
            s[i] = 'C'
        i = i + 1
    dna = "".join(s)

    return dna

dna = "ATTGC"
print(DNA_strand(dna))