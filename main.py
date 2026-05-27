import streamlit as st
from utils import generate_script

st.title("🎬 视频脚本生成器")

with st.sidebar:
    deepseek_api_key = st.text_input("请输入 DeepSeek API 密钥：", type="password")
    st.markdown("[获取 DeepSeek API 密钥](https://platform.deepseek.com/)")

subject = st.text_input("💡 请输入视频的主题")
video_length = st.number_input(
    "⏱️ 请输入视频的大致时长（单位：分钟）",
    min_value=0.1,
    step=0.1
)
creativity = st.slider(
    "✨ 请输入视频脚本的创造力（数字小说明更严谨，数字大说明更多样）",
    min_value=0.0,
    max_value=1.0,
    value=0.2,
    step=0.1
)

submit = st.button("生成脚本")

if submit:
    if not deepseek_api_key:
        st.warning("请先填写 DeepSeek API Key")
    elif not subject:
        st.warning("请填写视频主题")
    else:
        with st.spinner("正在生成脚本，请稍候..."):
            script = generate_script(
                subject=subject,
                video_length=video_length,
                creativity=creativity,
                api_key=deepseek_api_key
            )
            st.success("脚本生成完成！")
            st.write(script)
