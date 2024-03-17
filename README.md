# GeoAI Challenge Location Mention Recognition (LMR) from Social Media

## Introduction
Welcome to the repository containing the 1st place solution for the GeoAI Challenge Location Mention Recognition (LMR) from Social Media, organized by the International Telecommunication Union (ITU). This competition focused on automating the recognition of location mentions in microblogging posts during emergencies, aiming to aid disaster response authorities in their efforts.
<p align="center">
  <img width="400" alt="LMR example" src="https://github.com/moadel2002/Location-Mention-Recognition/assets/110140891/323c0dfa-4321-4109-b00f-71a65f0a1241">
</p>
  

## Methodology
## Data

Our solution for the GeoAI Challenge Location Mention Recognition (LMR) leverages two primary datasets for training:

1. **IDRISI Dataset**:
   - **Description**: The IDRISI dataset, named after the geographer Muhammad Al-Idrisi, is a significant resource for Location Mention Prediction (LMP) from Twitter data.
   - **Link**: [IDRISI Dataset](https://github.com/rsuwaileh/IDRISI/tree/main/LMR)

2. **WNUT16 Dataset**:
   - **Description**: The WNUT16 dataset is utilized in a study on Named Entity Recognition (NER) in Twitter data. It offers annotated tweets and focuses on recognizing named entities in noisy, user-generated text on social media.
   - **Link**: [WNUT16 Dataset](https://github.com/aritter/twitter_nlp/blob/master/data/annotated/ner.txt)

## Data Preprocessing

Data preprocessing is a pivotal step in our methodology, ensuring that the text data is well-structured and ready for analysis. Notably, I've introduced specific changes in the tagging scheme to harmonize the datasets.

In the WNUT16 dataset, I transitioned from the BIO (Begin-Inside-Outside) tagging scheme to the BIOES (Begin-Inside-Outside-End-Single) tagging scheme. This tagging scheme provides a more nuanced representation of named entities (NE) within the text. It is denoted as follows:
- **B (Begin)**: The first token of a chunk phrase or NE.
- **I (Inside)**: Tokens inside chunk phrases or NEs.
- **O (Outside)**: Tokens that are not part of any chunk phrase or NE.
- **E (End)**: The last token of a chunk phrase or NE.
- **S (Single)**: Represents unit or single-length chunk phrases or NEs.

Similarly, I applied this adjustment to the IDRISI dataset, transitioning from the BILOU (Begin-Inside-Last-Outside-Unit) tagging scheme to BIOES. Additionally, I replaced certain words like STAT, CITY, CTRY, and geo-loc with LOC for consistency. This harmonization in tagging schemes across both datasets helped to improve the performance, ensured consistency and facilitated a unified approach in our Location Mention Recognition (LMR) model development.

<p align="center">
  <img width="400" alt="LMR example" src="https://github.com/moadel2002/Location-Mention-Recognition/assets/110140891/0a3311fd-4f18-4c58-88cf-a6c98e310a22">
</p>

<p align="center">
IDRISI Sample Preprocessing Output
</p>
<p align="center">
  <img width="400" alt="LMR example" src="https://github.com/moadel2002/Location-Mention-Recognition/assets/110140891/44491ab6-5a5a-48eb-a8b6-a8724bef0f7c">
</p>

<p align="center">
WNUT16 Sample Preprocessing Output
</p>

## Model Architecture

For our Location Mention Recognition (LMR) solution, I harnessed the power of Flair, a versatile natural language processing (NLP) library. Flair offers a robust set of tools for NLP tasks, including named entity recognition (NER), sentiment analysis, part-of-speech tagging (PoS), biomedical data support, sense disambiguation, and classification, with growing language support.

Flair's architecture encompasses three main components:

1. **Text Embedding Library**: Flair provides simple interfaces to utilize various word and document embeddings. This includes Flair's proprietary embeddings and transformers, allowing for flexibility in embedding choice.

2. **PyTorch NLP Framework**: Built on PyTorch, Flair provides a solid foundation for training custom NLP models and experimenting with novel approaches. It makes use of Flair embeddings and classes, simplifying the development of complex NLP models.

For our LMR model, I harnessed Flair's NLP capabilities, using it as a robust foundation for building our sequence labeling model.

## Training

To train our LMR model, I utilized the Flair library's functionalities along with specific configurations tailored to our task. Below are the essential steps involved in the training process:

1. **Data Preparation**: I prepared the training data using the Flair library, specifying the tag type as 'ner'. This ensured that the model would be trained to recognize named entities, which aligns with the LMR task.

2. **Label Dictionary**: I constructed a tag dictionary based on the training data to define the named entity labels that the model would identify. This label dictionary forms a critical component in training the sequence labeling model.

3. **Embeddings**: Flair provides access to powerful transformer-based word embeddings. I chose the 'tner/deberta-v3-large-ontonotes5' model and customized its parameters. This embedding was employed as the foundation for our model's understanding of the text data.

4. **Sequence Tagger**: Using Flair, I created a SequenceTagger model configured for our LMR task. The model architecture included essential parameters like hidden size, embeddings, tag dictionary, tag type, and other settings. Importantly, I specified 'use_crf' and 'use_rnn' as 'False' to adapt the model for our specific requirements.

5. **Training Configuration**: I employed Flair's ModelTrainer to initiate the training process. This step involved specifying crucial training parameters, such as learning rate, mini-batch size, and the number of training epochs. Additionally, I used the AdamW optimizer and a learning rate scheduler (OneCycleLR) to optimize training. I specified the model's storage mode as 'none' and set weight decay to 0 to control model regularization.

## Evaluation and Results

The competition required submissions to follow a specific format, with each submission file containing two columns: 'ID' and 'Target.' The 'Target' column is crucial, representing the predicted start and end indices for each location mention within a tweet.

The primary evaluation metric for the GeoAI Challenge Location Mention Recognition (LMR) was the Root Mean Squared Error (RMSE). RMSE serves as a quantitative measure of the accuracy of our model's predictions in identifying the start and end indices for location mentions within microblogging posts.


Our model's remarkable performance, outperforms the baseline model which is Bert based.

| Metric         | Baseline model    |  Our model        |
| -------------- |:-----------------:|:-----------------:|
| RMSE           | 13.99             | 12.7              |


The second private phase evaluation was based on F1 score and our model achieved the highest F1 score among all solutions.

## How to Use
To utilize our solution, follow these steps:
1. Clone this repository to your local machine.
2. Download the trained model weights from the following link: [Model Weights](https://drive.google.com/file/d/1-2yQPU3JEJoTD7TUQ1emSzJH93mmbH-o/view?usp=drive_link).
3. Execute the `predict.py` script to infer the model on test data.
