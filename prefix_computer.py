import os
import matplotlib.pyplot as plt
from collections import defaultdict

# Directory containing text files
directory = "APPS/test/"

# Function to get common prefix counts
def count_prefixes(file_path, max_length=20):
    prefix_counts = defaultdict(lambda: defaultdict(int))  # {length: {prefix: count}}
    
    for i in range(4999):
        filename = str(i).zfill(4) + "/question.txt"
        with open(os.path.join(directory, filename), "r", encoding="utf-8") as f:
            first_line = f.readline().strip().split()  # Read the first line of each file
        
        for length in range(1, max_length + 1):
            if len(first_line) >= length:
                prefix = " ".join(first_line[:length])
                prefix_counts[length][prefix] += 1

    return prefix_counts

# Get all text files

# Compute prefix counts
prefix_counts = count_prefixes(directory)

# Plot results for each prefix length
plt.figure(figsize=(12, 6))
for length, counts in prefix_counts.items():
    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)[:20] # Take top 50 most common prefixes # Sort by frequency
    top_prefix, top_count = sorted_counts[0] 
    plt.plot([c[1] for c in sorted_counts], label=f"Prefix Length {length}") # Take top 50 most common prefixes
    # Most common prefix 
    
    print(f"Prefix Length {length}: Most Common Prefix = '{top_prefix}' (Count: {top_count})")

for length, counts in prefix_counts.items():
    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)[:50] # Take top 50 most common prefixes # Sort by frequency
    top_prefix2, top_count2 = sorted_counts[1] 
    # Most common prefix 
    
    print(f"Prefix Length {length}: Second Most Common Prefix = '{top_prefix2}' (Count: {top_count2})")


for length, counts in prefix_counts.items():
    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)[:50] # Take top 50 most common prefixes # Sort by frequency

    top_prefix3, top_count3 = sorted_counts[2] 
    # Most common prefix 
    print(f"Prefix Length {length}: Third Most Common Prefix = '{top_prefix3}' (Count: {top_count3})")
    # plt.plot(sorted_counts, label=f"Prefix Length {length}")
    # print(counts)

plt.xlabel("Unique Prefixes (Sorted)")
plt.ylabel("Number of Files Sharing Prefix")
plt.title("File Prefix Sharing Distribution")
plt.legend()
plt.grid()
plt.show()
