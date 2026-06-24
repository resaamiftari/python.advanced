import streamlit as st

def kalkuloje(number1,number2,operator):
    if operator == "mbledhe":
        rez= number1 + number2
    elif operator == "zbrite":
        rez= number1 - number2
    elif operator == "shumezim":
        rez =number1 * number2
    elif operator == "pjesto":
        rez =number1 / number2
        try:
            rez= number1 / number2
        except ZeroDivisionError:
            rez= "smundesh me pjestu me 0"
    return rez

def main():
    st.title("Kalkulatori")

    num1=st.number_input("Sheno numrin e pare")
    num2=st.number_input("Sheno numrin e dyte")

    operatori=st.radio("Selekto operatorin",["mbledhe","zbrite","shumezim","pjesto"])

    rezultati=kalkuloje(num1,num2,operatori)
    st.write(rezultati)

if __name__=="__main__":
    main()
