import pathlib

import streamlit as st
import streamlit.components.v1 as components

# ---------------------------------------------------------------------------
# StabilityLog - 화장품 안정성 시험 트래커
# 기존에 만들어둔 index.html(순수 HTML/CSS/JS, localStorage 기반)을
# 그대로 Streamlit 앱 안에 임베드해서 보여주는 방식입니다.
# ---------------------------------------------------------------------------

st.set_page_config(
    page_title="StabilityLog - 화장품 안정성 시험 트래커",
    page_icon="🧪",
    layout="wide",
)

# Streamlit 기본 여백/헤더를 최대한 줄여서 index.html이 화면 전체를 쓰도록 함
st.markdown(
    """
    <style>
        .block-container { padding: 0 !important; max-width: 100% !important; }
        header[data-testid="stHeader"] { height: 0; visibility: hidden; }
        #MainMenu { visibility: hidden; }
        footer { visibility: hidden; }
    </style>
    """,
    unsafe_allow_html=True,
)

HTML_PATH = pathlib.Path(__file__).parent / "index.html"
html_content = HTML_PATH.read_text(encoding="utf-8")

# index.html은 자체적으로 <html><head><body>를 포함한 완전한 문서이므로
# iframe(srcdoc) 안에 그대로 렌더링합니다.
# height는 필요에 따라 조절하세요. scrolling=True로 내부 스크롤을 허용합니다.
components.html(html_content, height=1400, scrolling=True)
