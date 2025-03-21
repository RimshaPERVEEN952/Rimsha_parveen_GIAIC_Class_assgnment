import streamlit as st

# title
# st.write("## Unit Conersition")
st.markdown('<h2><b style="color:darkred"> Unit Convertor Assignment</b></h2>' , unsafe_allow_html=True)
st.markdown('<h1 style="color:green">Rimsha Parveen</h1>' , unsafe_allow_html=True)
# user enter
my_val = st.number_input("Enter value to convert" , min_value=0.0 ,format="%0.3f" )

# from
value = st.selectbox(label="Conversion from"
                      , options=["meter","kilometer", "cm","mm", "gram"])
# to
to= st.selectbox(label="to convert" ,
              options=["meter","kilometer","cm","mm", "kilogram"])
st.markdown(f"you  convert from: \t{my_val} {value} to \t {to}")

btn = st.button("Convert")
def Convertor(my_val):
    if btn:
        if ((value == "meter") and (to == "kilometer")):
            # st.write(my_val)
            return my_val*100
        
        elif((value == "kilometer") and(to == "meter")):
            return my_val * 0.001

        elif((value == "cm") and (to == "mm")):
            return my_val *10

        elif((value == "mm") and (to == "cm")):
            return my_val *0.1

        elif((value == "gram") and(to == "kilogram")):
            return my_val *1000
        
        elif((value == "kilogram") and(to == "gram")):
            return my_val *0.001
        elif (value == to):
            return my_val

conv = Convertor(my_val)    
result = (f" {conv}")
if btn:
    st.success(f"Finala result :{result}")
    # st.write(Convertor_m_km(my_val))

# st.write(btn)