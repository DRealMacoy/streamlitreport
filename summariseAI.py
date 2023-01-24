# import libraries

import openai       
import streamlit as st 

# set the GPT3 - api key
openai.api_key = st.secrets ["pass"]

st.header("Report summarizer app OpenAI + Streamlit")

article_text = st.text_area ("Enter the observation list to be summarized")
output_size = st.radio(label = "What kind of output do you want?", 
                    options= ["To-The-Point", "Concise", "Detailed"])

if output_size == "To-The-Point":
    out_token = 50,
if output_size == "Concise":
        out_token = 128,
else:
    out_token = 516,

if len(article_text) > 100:
        temp = st.slider("temperature", 0.0,1.0,0.5)
        if st.button("Generate short summary"):
     # Use GTP-3 to generate a summary of the article
            response = openai.Completion.create(
                engine = "text-davinci-003",
                prompt = "Please summarize this article to generate background" + article_text,
                max_tokens = out_token,
                temperature = 0.5)
     
     #Print the summary

        res = response["choices"] [0] ["text"]
        st.info(res)
        st.download_button("Download Result", res)

else:
   st.warning("The paragraph is not long enough")