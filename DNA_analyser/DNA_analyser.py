def analyse_DNA(sequence):
    if sequence.strip() == '':
        return 'Invalid Input(empty string)'
    else:

        # Validity

        def is_valid(sequence):
            DNA = sequence.upper().strip()
            DNA_A = DNA.replace('A', '')
            DNA_T = DNA_A.replace('T', '')
            DNA_G = DNA_T.replace('G', '')
            DNA_C = DNA_G.replace('C', '')
            if bool(DNA_C) is False:
                validity = 'Valid'
            else:
                validity = 'Not valid'
            return validity

        # Base Counter

        def base_counter(sequence, validity):
            if validity == 'Not valid':
                return 'Invalid DNA'
            else:
                DNA = sequence.upper().strip()
                occ_dictionary = {
                    "A": DNA.count("A"),
                    "T": DNA.count("T"),
                    "G": DNA.count("G"),
                    "C": DNA.count("C")
                }
                return occ_dictionary

        # Complement Generator

        def complement_generator(sequence, validity):
            if validity == 'Not valid':
                return 'Invalid DNA'
            else:
                DNA = sequence.upper().strip()
                St = DNA.replace("T", "t")
                SA = St.replace("A", "T")
                AT_S = SA.replace("t", "A")
                Sc = AT_S.replace("C", "c")
                SG = Sc.replace("G", "C")
                Complement_S = SG.replace("c", "G")
                return Complement_S

        # GC percentage

        def GC_percentage(sequence, validity):
            if validity == 'Not valid':
                return 'Invalid DNA'
            else:
                DNA = sequence.upper().strip()
                DNA_A = DNA.replace('A', '')
                DNA_T = DNA_A.replace('T', '')
                gc_percent = (len(DNA_T)/len(sequence))*100
                return gc_percent
        validity = is_valid(sequence)
        return {
            "validity": validity,
            "length": len(sequence),
            "counts": base_counter(sequence, validity),
            "GC_percentage": GC_percentage(sequence, validity),
            "complement": complement_generator(sequence, validity)

        }
