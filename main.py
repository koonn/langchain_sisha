import os
import openai

from langchain.prompts import PromptTemplate

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

# プロンプトテンプレートの定義
template_asking_shisha_flavor_mixes = """
シーシャのフレーバーミックスを3個教えてください。\
3種類のフレーバーをミックスした組み合わせで、{flavors}を必ず含んでください。\
各フレーバーミックスの特徴も教えてください。
"""

if __name__ == '__main__':
    # プロンプトテンプレートの作成
    prompt = PromptTemplate(
        input_variables=['flavors'],
        template=template_asking_shisha_flavor_mixes
    )

    # テンプレートからプロンプトを生成
    prompt = prompt.format(flavors='アップル')
    # print(prompt)

    # チャットモデルの作成
    llm = ChatOpenAI(model='gpt-3.5-turbo')

    # チャットモデルの実行
    message = llm.predict_messages([HumanMessage(content=prompt)])

    print(message.content)
    # >> AIMessage(content="J'aime programmer.", additional_kwargs={})