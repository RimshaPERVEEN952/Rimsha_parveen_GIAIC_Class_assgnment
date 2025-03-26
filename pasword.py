import streamlit as st
import random
import string

# define functon
def password_generator(length , use_digit, use_special_char):
    charctors = string.ascii_letters

    if (use_digit):
            charctors += string.digits

    if(use_special_char):
            charctors +=string.punctuation

# underscore is a specifc syntax    
    return ''.join(random.choice(charctors) for _ in range(length))

st.title("Password Generator" )
st.write('<h2 style="color:#691fb2">With Rimsha Parveen</h2>', unsafe_allow_html=True)

length = st.slider("select password length to generate your password " , min_value=6 , max_value=14  , value=12)
use_digit = st.checkbox("add digit")
use_special_char = st.checkbox("add special character")

if st.button("Generate strong Password"):
       password = password_generator(length , use_digit , use_special_char )
       st.success(f"\t #####  Your password has generated! :  {password}")
       st.write('<b style="color:#136c68">_________________________________ Congratulation_________________________________</b>' ,  unsafe_allow_html=True)

st.write('<h3 style="color:#691fb2">by Rimsha Parveen ❤️💌</h3>' ,  unsafe_allow_html=True)