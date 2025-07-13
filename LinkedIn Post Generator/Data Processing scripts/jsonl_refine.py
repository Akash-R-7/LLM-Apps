import json

# Input and output filenames
input_file = "ins_dataset_8_1.jsonl"
output_file = "ins_dataset_8_1_cleaned.jsonl"


def clean_instruction(text):
    if not isinstance(text, str):
        return text
    text = text.strip()

    # Remove newline and carriage return characters
    text = text.replace('\n', '').strip()
    text = text.replace('\"', '').strip()

    if text.startswith('Instruction: '):
        text = text[len('Instruction: '):]
    elif text.startswith('For example, '):
        text = text[len('For example, '):]
    elif text.startswith('Example: '):
        text = text[len('Example: '):]
    elif text.startswith('For example: '):
        text = text[len('For example: '):]



    return text

with open(input_file, "r", encoding="utf-8") as infile, open(output_file, "w", encoding="utf-8") as outfile:
    for line in infile:
        try:
            obj = json.loads(line)
            obj["instruction"] = clean_instruction(obj.get("instruction", ""))
            json.dump(obj, outfile, ensure_ascii=False)
            outfile.write("\n")
        except Exception as e:
            print(f"Skipping a line due to error: {e}")

################################## For refining final combined dataset ##################################

cleaned = []
with open("combined_instruction_ds.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        try:
            obj = json.loads(line)
            if obj.get("instruction") and obj.get("output"):
                cleaned.append(obj)
        except:
            continue

with open("final_dataset.jsonl", "w", encoding="utf-8") as f:
    for item in cleaned:
        json.dump(item, f)
        f.write("\n")

print(f"✅ Cleaned dataset saved. {len(cleaned)} valid samples.")
