A Python function that analyzes a DNA sequence and returns a structured report containing useful information about the sequence.
Features:
- DNA sequence validation
- Base counting (A, T, G, C)
- Complement generation
- GC percentage calculation
- Sequence length calculation
- Handles invalid and empty inputs
Concepts used:
- Functions
- Nested functions
- Dictionaries
- String manipulation
- Conditional statements
Example Output:
{
"validity": "Valid",
"length": 6,
"counts": {"A": 2, "T": 2, "G": 1, "C": 1},
"GC_percentage": 33.33,
"complement": "TACGTA"
}
