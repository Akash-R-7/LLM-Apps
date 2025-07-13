import pandas as pd
import os

# Load the original CSV
df = pd.read_csv("final_cleaned_content_and_hashtags.csv")

# Set chunk size
chunk_size = 2000

# Output directory for split files

output_dir = "split_csv_files"
os.makedirs(output_dir, exist_ok=True)

# Split and save each chunk
for i in range(0, len(df), chunk_size):
    chunk = df[i:i + chunk_size]
    chunk.to_csv(f"{output_dir}/chunk_{i//chunk_size + 1}.csv", index=False)

print(f"CSV split into {len(df) // chunk_size + 1} files.")