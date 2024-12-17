import streamlit as st

st.title("About Kwon")
st.header("To be a good English teacher")

# 이미지 추가
st.subheader("Meet our mascot!")
image_url = "https://example.com/cute-character.png"  # 여기에 캐릭터 이미지 URL 또는 로컬 경로 입력
st.image(image_url, caption="Your friendly mascot!", width=300)

st.write("This cute character is here to cheer you on as you learn and grow! 🌟")

uploaded_file = st.file_uploader("Upload a cute character image", type=["png", "jpg", "jpeg"])
if uploaded_file is not None:
    st.image(uploaded_file, caption="Your friendly mascot!", width=300)

