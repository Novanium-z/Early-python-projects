DNA = input("Enter DNA strand: ").upper().strip()
DNA_A = DNA.replace('A', '')
DNA_T = DNA_A.replace('T', '')
DNA_G = DNA_T.replace('G', '')
DNA_C = DNA_G.replace('C', '')
if bool(DNA_C) is False:
    occ_dictionary = {
        "A": DNA.count("A"),
        "T": DNA.count("T"),
        "G": DNA.count("G"),
        "C": DNA.count("C")
    }
    print(f"Count of A: {occ_dictionary.get("A")} ")
    print(f"Count of T: {occ_dictionary.get("T")} ")
    print(f"Count of G: {occ_dictionary.get("G")} ")
    print(f"Count of C: {occ_dictionary.get("C")} ")
else:
    print("This is not a valid DNA strand")
