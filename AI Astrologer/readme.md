# AI Astrologer

AI Astrologer is a fun demo app that combines **astrology chart calculations** with **local LLM-powered interpretations**.  
Users enter their **birth details (name, date, time, place)** and ask free-form questions.  
The app computes the **Sun, Moon, and Ascendant signs** (with correct geolocation & timezone) and then generates a personalized astrology-based response using a locally hosted LLM.

---

## Features
- Collects user **birth details** via Streamlit UI (pickers or raw text).  
- Calculates **astrology chart** using Flatlib library.  
- Detects **latitude, longitude, and timezone** using geopy and timezonefinder libraries from the entered place.  
- Integrates with **Ollama** (usese LLMs like Mistral, Gemma) for natural, astrology-style responses.  
- Displays **fun rotating astrology facts** while loading results.  

---

## ⚙️ Setup

### 1. Clone the repo
```bash
git clone https://github.com/Akash-R-7/LLM-Apps.git
cd "LLM-Apps/AI Astrologer"
```
---
### 2. Set up environment
```bash
# For conda:
conda create -n ai-astro python=3.10.13
conda activate ai-astro
```
---
### 3. Install dependencies
```bash
pip install -r requirements.txt
```
---
### 4. Installing ollama and downloading LLM
Download & install [Ollama](https://ollama.com/)

Ollama allows one to run various open-source large language models (LLMs), (full and quantized) even on your CPU's. To download and use a model, use the command 
```bash
ollama run <model_name>
```
Here I used **gemma3:1b** a very lightweight model by Google. It can easily be run on CPU.

---
### 5. Running the app
```bash
python streamlit run app.py
```
Open your browser at your localhost address, if the previous command doesn't automatically opens.

## Notes:
- Make sure the ollama application is turned on (wroks in background) before runnig the astro app.
- Use of Chat-GPT is acknowledged in laying out workflow, and generating excerpts of code which are then edited and changed as per the requirements, system choices and debugging steps.








