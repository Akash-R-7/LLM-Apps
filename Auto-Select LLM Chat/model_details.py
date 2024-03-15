import pandas as pd

def models_and_details():
        category_models = {"Personal Talk": "mistral",
                        "Text Writing": "westlake",
                        "Commonsense Reasoning": "phi",
                        "Math": "wizard-math",
                        "Coding or Computer Science": "deepseek-coder",
                        "Science or Tech": "gemma"}

        model_details = {"model": ['mistral', 'westlake', 'phi', 'wizard-math', 'deepseek-coder', 'gemma'],
                        "Paper": ['https://arxiv.org/pdf/2310.06825.pdf', 'https://huggingface.co/senseable/WestLake-7B-v2',
                                'https://www.promptingguide.ai/models/phi-2',
                                'https://arxiv.org/pdf/2308.09583.pdf', 'https://arxiv.org/pdf/2401.14196.pdf', 'https://ai.google.dev/gemma'],
                        "Model Hub": ['https://ollama.com/library/mistral', 'https://huggingface.co/senseable/WestLake-7B-v2',
                                'https://ollama.com/library/phi', 'https://ollama.com/library/wizard-math',
                                'https://ollama.com/library/deepseek-coder', 'https://ollama.com/library/gemma'],
                        "Tags": [['Grouped-Query Attention', 'Sliding-Window Attention', 'Guardrails'],
                                ['Roleplay', 'Text-generation'],
                                ['Data-selection', '2.7B model'],
                                ['Reinforced Evol-Instruct (RLEIF)', 'GSM8k'],
                                ['Code-completition', 'Code-generation', 'Fill-in-the-Middle'],
                                ['CSAM and Sensitive Data Filtering', 'Multi-Query Attention', 'RoPE Embeddings' ]],
                        }
        model_details_df = pd.DataFrame(model_details)

        return (category_models, model_details_df)