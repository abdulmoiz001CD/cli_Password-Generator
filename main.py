import streamlit as st 
import random
import string

def pass_generator(lenght,use_digit,use_special):
    characters = string.ascii_letters

    if use_digit:
         characters += string.digits

    if use_special:
         characters += string.punctuation


    return "".join(random.choice(characters) for _  in range(lenght))


st.title("Password Generator")

lenght = st.slider("Select Password Lenght" , min_value = 6 , max_value= 18 , value= 8)
use_digit = st.checkbox(f"Include Digit")
use_special = st.checkbox("Include Special Character")


if st.button("Generate Password"):
     password = pass_generator(lenght,use_digit,use_special)
     st.write(f"Generated Password: `{password}`")

st.write("______________________________")
st.write("Build with By Abdul Moiz")
     
