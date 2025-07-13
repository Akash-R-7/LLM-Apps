## Model Details
* [phi-4-mini-instruct](https://huggingface.co/microsoft/Phi-4-mini-instruct) model instruction fine-tuned on LinkedIn posts.<br>
* Parameter Efficient Fine tuning with LoRA adapter.<br>

## Training Dataset
* Uses LinkedIn dataset from [kaggle](https://www.kaggle.com/datasets/shreyasajal/linkedin-influencers-data) for sourcing.<br>
* Instruction dataset is created from the post and hashtags from the dataset, using hashtags to create themes. For posts missing hashtags, [zephyr-7b-beta](https://huggingface.co/HuggingFaceH4/zephyr-7b-beta) is used to generate relevant theme. Final instruction is also generated using the same model.<br>
* After some refining and chunking final dataset is obtained in the following format:
  ```yaml
  {
  "instruction": "Create a LinkedIn post in the theme of marketing that features a conversation between two individuals discussing a unique and unexpected topic related to marketing. Make it engaging by using a convers",
   "output": "Was great to sit down with  Scott Trobaugh  +  Cliff Lewis  for this chat about Mr. Rogers and  #marketing . So random, I know, but trust me, they're on to something!"
  }
* The total dataset size obtained is approx. 30,000.

## Training Details
* phi-4-mini-instruct (a 3.8B parameter model) is used as the base model.
* LoRA (a parameter-efficient training approach) is utilized to fine-tune the base model on the obtained dataset.
* Due to hardware constraints (T4 google colab GPU), there are are lot of limitataions while training such a huge model, like continously facing out-of-memory error. After several trials, I was successfully able to train a very small subset.
* Final model after merging base model with adapter was uploaded at [Huggingface](https://huggingface.co/SkyR/linkedin-8bit-phi4). 
* Training details can be found out there.

## Inferencing and Running app
* Final app which uses the trained model can be run by installing packages from requriements.py and running app.py.
* The gradio interface is used to provide a simple front-end for the app.
* The final app can be run only on GPU due to bit configuaration used during training when the model was quantized.
* Running first time will take slightly longer time due to package installations and downloading model from the hub.
* In case of any error, please see the following video on how the app can simply be run on a colab notebook.

https://github.com/user-attachments/assets/8fc78d20-bf2b-4792-a41f-50ed158f24be

## Future scope
* Due to the large size of the model, even with optimizations like quantization, shorter sequence lengths, and using GPU, generation still takes around 20 sec after initial loading of the model.
* Faster inference can be achieved by using a techniques like flash attention and parallelism.
* These techniques demand better hardware which was a constraint on this project.
* In future, more data can be used for training, with these inferencing techniques to obtain even better and faster model.

 
  
