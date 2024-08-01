def dna_to_rna(dna):
   result = "";
   dna = list(dna.upper());
   for nucleotide in dna:
    if nucleotide == "T":
      result += "U";
    else:
      result += nucleotide;
   return result


print(dna_to_rna(input()))