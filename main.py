import os
import openai

from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

# Load OpenAI API key from .env file
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file
openai.api_key = os.environ['OPENAI_API_KEY']

# 質問テンプレートの定義
template_asking_shisha_flavor_mixes = """
シーシャのフレーバーミックスを3個教えてください。\
3種類のフレーバーをミックスした組み合わせで、ピーチを必ず含んでください。\
各フレーバーミックスの特徴も教えてください。
"""

if __name__ == '__main__':
    # チャットモデルの作成
    chat = ChatOpenAI(model='gpt-3.5-turbo')

    # テンプレートの作成
    message = chat.predict_messages([HumanMessage(content=template_asking_shisha_flavor_mixes)])

    print(message.content)
    # >> AIMessage(content="J'aime programmer.", additional_kwargs={})