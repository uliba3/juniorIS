# juniorIS
## Project Summary

### Overview
This project focuses on evaluating the performance of the gemma-2b-it model on the MMLU dataset in terms of number of shots. The MMLU dataset consists of multiple-choice questions from various subject areas, categorized into Humanities, Social Science, STEM, and others.

### Experiment Setup
- **Dataset**: The MMLU dataset comprises 15908 questions, with 5 questions per subject for the few-shot development set, 1540 questions for the validation set, and 14079 questions for the test set. Additional shots were obtained by using 5 questions from the validation set.
- **Model**: The gemma-2b-it model, a 2 billion parameter instruct model based on the Gemma architecture, was utilized. The model employs a transformer decoder architecture and underwent pre-training on 2T tokens of primarily English data, followed by fine-tuning using a mix of text-only, English-only synthetic, and human-generated prompt response pairs.

### Performance Evaluation
- **Accuracy**: The performance of the gemma-2b-it model was evaluated in terms of classification accuracy across all examples and tasks in the MMLU dataset. The model achieved a 42.3% accuracy on the MMLU dataset with 5-shot settings, comparable to GPT-3 175B (5-shot) model's performance of 43.9%. For more information, you can refer to the [Gemma Open Models](https://blog.google/technology/developers/gemma-open-models/) blog post.

### Execution Environment
- **Platform**: The experiment was conducted using Google Colab, a popular platform for running Python code and machine learning experiments. Google Colab provides access to powerful GPU resources, facilitating efficient training of large models like gemma-2b-it.

### Prompt Format
- **Prompt Structure**: The experiment utilized the same prompt format as the original MMLU dataset paper. Each prompt started with the statement "The following are multiple-choice questions (with answers) about [subject]." Up to 10 demonstration examples with answers were added to the prompt before appending the question. All prompts ended with "Answer: ".