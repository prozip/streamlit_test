import streamlit as st


import torch
from diffusers import StableDiffusionPipeline

# make sure you're logged in with `huggingface-cli login`
pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4", 
        revision="fp16", torch_dtype=torch.float16, use_auth_token="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")  


st.title("AI Art Tool")
st.write("Text to Image generator")
st.write(torch.version)

promp = st.text_input("Input promp:")
st.write(promp)



