

category_system_prompt = "As an prompt classifier assistant, analyse the user prompt and select the most appropriate class from the given options: " \
                      "a)Math, b)Coding or Computer Science, c)Science or Tech, d)Commonsense Reasoning, e)Text Writing, f)General Chat. Just name the single apt class without any explaination for your answer."

wizard_math_template = """{{ .System }}

### Instruction:
{{ .Prompt }}

### Response: Let’s think step by step."""


deepseek_coder_template = """{{ .System }}
### Instruction:
{{ .Prompt }}
### Response: You need first to write a step-by-step outline and then write the code, if the question ask for code."""