import random

# -------------------------------
# DNA Aptamer Mutation Generator
# -------------------------------

# Original DNA aptamer sequence
template_seq = "CGACACCTCCAGACGCACGCTCGACACGACACCTCCAGACCGCCTCGTCCACTGTGCCTC"

# Mutation range (0-based indexing)
mutation_start = 20
mutation_end = 48

# Nucleotides
nucleotides = ['A', 'T', 'C', 'G']

def mutate_sequence(template):
    """
    Generates a single mutated sequence by randomly mutating bases
    within the specified mutation range.
    """
    seq_list = list(template)
    mutation_positions = [pos for pos in range(mutation_start, mutation_end) if random.random() < 0.5]

    for pos in mutation_positions:
        original_base = seq_list[pos]
        new_base = random.choice([n for n in nucleotides if n != original_base])
        seq_list[pos] = new_base

    return "".join(seq_list)

# Generate 500 unique sequences
unique_sequences = set()
while len(unique_sequences) < 500:
    mutated_seq = mutate_sequence(template_seq)
    unique_sequences.add(mutated_seq)

# Save sequences to a file
with open("mutated_sequences.txt", "w") as f:
    for seq in unique_sequences:
        f.write(seq + "\n")

print("mutated_sequences.txt created with 500 unique sequences.")

