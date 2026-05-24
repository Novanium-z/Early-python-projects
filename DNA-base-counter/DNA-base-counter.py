inp_strand = input("Enter DNA Strand: ")
DNA_Strand = inp_strand.upper()
occ_dictionary = {
    "A": DNA_Strand.count("A"),
    "T": DNA_Strand.count("T"),
    "G": DNA_Strand.count("G"),
    "C": DNA_Strand.count("C")
}
print(f"Count of A: {occ_dictionary.get("A")} ")
print(f"Count of T: {occ_dictionary.get("T")} ")
print(f"Count of G: {occ_dictionary.get("G")} ")
print(f"Count of C: {occ_dictionary.get("C")} ")
