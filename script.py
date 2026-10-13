
import streamlit as st

st.set_page_config(
    page_title="Мой калькулятор",
    page_icon=":material/calculate:",
    layout="centered"
)

st.markdown("""
<style>
    html, body {
        width: 100%;
        max-width: 100%;
        overflow-x: hidden !important;
    }
    
    .block-container {
        width: 100%;
        max-width: 440px;
        box-sizing: border-box;
        padding: 1.5rem 16px 2rem 16px;
    }
    
    input,
    input[type="number"] {
        font-size: 16px !important;
    }
    
    [data-testid="stNumberInput"] {
        width: 100%;
        min-width: 0;
    }

    h1 {
        text-align: center;
        font-size: 32px;
        margin-bottom: 25px;
    }

    div.stButton > button {
        border-radius: 12px;
        height: 52px;
        font-size: 18px;
        font-weight: 600;
    }

    .result-box {
        text-align: center;
        background: #eaf3ff;
        color: #172b4d;
        border-radius: 14px;
        padding: 22px;
        margin-top: 20px;
    }

    .result-value {
        font-size: 36px;
        font-weight: 700;
    }
</style>
""", unsafe_allow_html=True)

st.title("Мой калькулятор")

a = st.number_input(
    "Первое число",
    value=0.0
)

operation = st.selectbox(
    "Операция",
    ["+", "-", "×", "÷"]
)

b = st.number_input(
    "Второе число",
    value=0.0
)

if st.button("Вычислить", type="primary", use_container_width=True):

    if operation == "+":
        result = a + b

    elif operation == "-":
        result = a - b

    elif operation == "×":
        result = a * b

    elif operation == "÷":
        if b == 0:
            st.error("На ноль делить нельзя!")
            st.stop()
        result = a / b

    st.markdown(
        f"""
        <div class="result-box">
            <div>Результат</div>
            <div class="result-value">{result:g}</div>
        </div>
        """,
        unsafe_allow_html=True
    )
