# PandasAgent
Chat with dataset(excel,csv) present in our device. usually retrieving data from excel sheets requires different form of questioning.but withthis we can ask questions in natural language.

# Project_setup

## Step 1 -- environment setup:
1. open vscode

```   
python -m venv myenv
```
2. myenv can be any name you want to give to your virtual environment

3. myenv in above code is virtual environment name we give
   
## Step 2 -- Activating virtual environment setup:

```
.\myenv\scripts\activate
```

4. To activate vitual environment created

## Step 3 -- Installing required libraries: 

5. Now we have to install required library packages

```
pip install langchain
pip install openai
pip install streamlit
pip install tabulate
```

## step 4 -- upload csv file as dataset into the directory of the project

6. For testing the code download any excel dataset an d save it as csv file or use csv files on the device on which you want to ask questions.

## Step 5 -- Streamlit file for Chatbot on csv file dataset

7. Run pandas_agent.py file to build chatbot interface .

```
streamlit run pandas.py
```

# Reference:

https://python.langchain.com/docs/modules/agents/toolkits/pandas


# Collab Notebook:

csv_agent.ipynb

It is the model code for question answering with csv files

# Improvements:

1. Can be made this as a tool for manipulating the data in the csv file as well .
2. Can also make in plotting graphical representation in responses .



   

