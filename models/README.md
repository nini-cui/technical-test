# File to be downloaded

Please download file glove.6B.100d.text file to run the code

# Relation Extraction

Installing all the packages from the **requirements.txt** file to the virtual environment:
```
pip install -r requirements.txt
```


# Usage 

The configurations can be adjusted in the **conf.yml** file. 
You can toggle whether to do k fold analysis or not, what is the batch size for the training of the model, the number of epochs and whether to save the forecasts in a file for uploading to Kaggle (https://www.kaggle.com/c/nlp-getting-started). 

The main script is the **test.py** script. 

```
python test.py
```
Replace test_sentence with any sentences that you want to predict

# Overview of the pipeline

The steps in the pipeline are as follows:

**Text preprocesing** -> **Creating the tensors from text** -> **Training the model** -> **Making predictions**