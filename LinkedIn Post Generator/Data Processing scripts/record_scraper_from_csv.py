import pandas as pd
import ast

# Load your original CSV
df = pd.read_csv("influencers_data - Copy.csv", low_memory=False)

# print(df.head())


# Function to extract only the hashtags from nested lists
def extract_hashtags(cell):
    try:
        parsed = ast.literal_eval(cell)  # safely convert string to list
        return [tag[0].strip() for tag in parsed if isinstance(tag, list) and len(tag) > 0]
    except Exception:
        return []

# Function to clean and encode content
def clean_content(text):
    if pd.isna(text):
        return ""
    cleaned = text.encode("utf-8", errors="ignore").decode("utf-8")
    cleaned = cleaned.replace("\u202A", "")  # remove LRE character
    cleaned = cleaned.strip().replace("\n", " ").replace("\r", " ")

    return str(cleaned)

# Apply cleaning functions
new_df = pd.DataFrame({
    'content': df['content'].apply(clean_content),
    'hashtags': df['hashtags'].apply(extract_hashtags)
})

# Save to a new CSV
new_df.to_csv("cleaned_content_and_hashtags.csv", index=False)

print("New CSV with content and hashtags saved as 'content_and_hashtags.csv'.")

####################################################################################################################

# Load the cleaned CSV
df = pd.read_csv("cleaned_content_and_hashtags.csv")

# Function to check if content is not empty or just spaces
def is_valid_content(text):
    return isinstance(text, str) and text.strip() != ""

# Filter out invalid rows
filtered_df = df[df['content'].apply(is_valid_content)]

# Save to a new CSV
filtered_df.to_csv("final_cleaned_content_and_hashtags.csv", index=False)

print("Final cleaned CSV saved as 'final_cleaned_content_and_hashtags.csv'.")