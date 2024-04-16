# juniorIS

### Overview
This project focuses on evaluating the performance of the gemma-2b-it model on the MMLU dataset in terms of number of shots. The MMLU dataset consists of multiple-choice questions from various subject areas, categorized into Humanities, Social Science, STEM, and others.

### Experiment Setup
- **Dataset**: The MMLU dataset comprises 15908 questions, with 5 questions per subject for the few-shot development set, 1540 questions for the validation set, and 14079 questions for the test set. Additional shots were obtained by using 5 questions from the validation set.
- **Model**: The gemma-2b-it model, a 2 billion parameter instruct model based on the Gemma architecture, was utilized. The model employs a transformer decoder architecture and underwent pre-training on 2T tokens of primarily English data, followed by fine-tuning using a mix of text-only, English-only synthetic, and human-generated prompt response pairs.

### Execution Environment
- **Platform**: The experiment was conducted using Google Colab, a popular platform for running Python code and machine learning experiments. Google Colab provides access to powerful GPU resources, facilitating efficient training of large models like gemma-2b-it.

### Prompt Format
- **Prompt Structure**: The experiment utilized the same prompt format as the original MMLU dataset paper. Each prompt started with the statement "The following are multiple-choice questions (with answers) about [subject]." Up to 10 demonstration examples with answers were added to the prompt before appending the question. All prompts ended with "Answer: ".

### Files
- **gemma.ipynb**: Code to run gemma-2b-it on MMLU dataset. Expected to be run using Google Colab.
- **dataAnalysis.ipynb**: Code to analyze the result from gemma.ipynb.
- **extractField.py**: Code to create json file that has subjects as keys and field names as values

### Getting started
1. upload gemma.ipynb to Google Colab and also upload data.json to google drive path: /content/drive/MyDrive/Colab Notebooks/CS 200/data.json
2. execute each cell from the top in Google Colab
3. download updated data.json from Google Drive
4. run extractField.py and dataAnalysis.ipynb in the same folder as data.json