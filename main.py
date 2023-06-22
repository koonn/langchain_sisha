import os
import openai

import streamlit as st

from langchain.prompts import PromptTemplate

from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
from langchain.chains import LLMChain

# .envファイルから、OpenAI API keyを読み込む
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())
openai.api_key = os.environ['OPENAI_API_KEY']

# プロンプトテンプレートの定義
template_asking_shisha_flavor_mixes = """
シーシャのフレーバーミックスを3個教えてください。\
3種類のフレーバーをミックスした組み合わせで、{flavors}を必ず含んでください。\
各フレーバーミックスの特徴も教えてください。
"""

def main(flavors: str):
    # プロンプトテンプレートの作成
    prompt = PromptTemplate(
        input_variables=['flavors'],
        template=template_asking_shisha_flavor_mixes
    )

    # チャットモデルの作成
    llm = ChatOpenAI(model='gpt-3.5-turbo')

    # LLMチェーンを作成
    chain = LLMChain(llm=llm, prompt=prompt)

    # チャットモデルの実行
    prediction = chain.run(flavors=flavors)

    # print(prediction.strip())
    st.write(prediction.strip())


if __name__ == '__main__':
    # タイトル
    st.title('おすすめのフレーバーミックスを提案します!')

    with st.form(key='my_form'):
        flavors_text = st.text_input(label='ミックスに含めたいフレーバーを入力してください')
        submitted = st.form_submit_button(label='送信')
        if submitted:
            main(flavors=flavors_text)