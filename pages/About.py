import streamlit as st

st.title("About Kwon")
st.header("To be a good English teacher")

# 이미지 추가
st.subheader("Meet our mascot!")

# 이미지 파일 업로드
uploaded_file = st.file_uploader("Upload your mascot image (png or jpg)", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Your friendly mascot!", width=300)
else:
    st.write("Please upload a mascot image to display.")

st.write("This cute character is here to cheer you on as you learn and grow! 🌟")


