# 注意这里加了个 .core
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.utilities import WikipediaAPIWrapper

def generate_script(subject, video_length, creativity, api_key):
    # 1. 初始化 DeepSeek 模型
    llm = ChatOpenAI(
        model="deepseek-chat",          # ✅ DeepSeek 主模型
        temperature=creativity,
        openai_api_key=api_key,
        openai_api_base="https://api.deepseek.com/v1"
    )

    # 2. 检索维基百科（保持不变）
    wiki = WikipediaAPIWrapper()
    search_result = wiki.run(subject)

    # 3. 构造 Prompt
    prompt = ChatPromptTemplate.from_messages([
        ("system", "你是一位专业的短视频脚本策划师。"),
        ("human",
         f"""
请根据以下信息生成一段视频脚本：

主题：{subject}
时长：{video_length} 分钟
参考资料：{search_result}

要求：
- 语言生动、适合短视频口播
- 包含开场、正文、结尾
- 适当加入镜头提示（近景 / 远景 / 特写）
""")
    ])

    # 4. 调用模型
    chain = prompt | llm
    response = chain.invoke({})

    return response.content