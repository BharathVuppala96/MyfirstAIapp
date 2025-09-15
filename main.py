from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain



import os
os.environ['GOOGLE_API_KEY']="AIzaSyB283UvDtA-pxbnq9hl5EXDHX9rxJ8J10k"



tweet_template="Give me {number} tweets on {topic}"
tweet_prompt=PromptTemplate(input_variables=["number","topic"],template=tweet_template)

gemini_model=ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest")


tweet_chain=tweet_prompt | gemini_model
response = tweet_chain.invoke({"number": 3, "topic":"India"})

import streamlit as st

st.header(" Bharath Tweet Generator")

st.subheader("Generate tweets using GEnAI ")

topic = st.text_input("Topic")

number=st.number_input("Number of tweets", min_value=1, max_value=10, value=1, step=1)

if st.button("generate"):
    tweets=tweet_chain.invoke({"number": number, "topic":topic})
    st.write(tweets.content)

