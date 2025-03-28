import streamlit as st
import re

st.title("💪YOUR PASSWORDS STRENGTH ")
st.write("A strong password should be at least:")
st.write('<h4 style="color:green">✅ Be at least 8 characters long</h4>' ,unsafe_allow_html=True  )
st.write('<h4 style="color:green">✅ Contain uppercase & lowercase letters</h4>' ,unsafe_allow_html=True )
st.write('<h4 style="color:green">✅ Include at least one digit (0-9)</h4>' ,unsafe_allow_html=True )
st.write('<h4 style="color:green">✅ Have one special character (!@#$%^&*)</h4>' ,unsafe_allow_html=True )

user_password =st.text_input("Enter strong password")
# score = st.slider("select password length to generate your password" , max_value = 4)

def check_password_stength(user_password):
    score = 0    
    if len(user_password) >= 8:
        score += 1
        # score =1
    else:
        st.write("❌ Password should be at least 8 characters long.")
    
    if (re.search(r"[A-Z]", user_password) and re.search(r"[a-z]" , user_password)):
        score +=1
        # score =2
    else:
        st.write("❌ Include both uppercase and lowercase letters.")
    if (re.search(r"\d" , user_password)):
        score +=1
        # score =3
    else:
        st.write("❌ Add at least one number (0-9).")
    if (re.search(r"[!@#$%^&*]", user_password)):
        score+=1
        # score =4
    else:
        st.write("❌ Include at least one special character (!@#$%^&*).")
  
    if score == 4:
        st.write("✅ Strong Password!")
    elif score == 3:
        st.write("⚠️ Moderate Password - Consider adding more security features.")
    else:
        st.write("❌ Weak Password - Improve it using the suggestions above.")
# # Get user input
if st.button("Password strength"):
    if user_password:
        check_password_stength(user_password)

