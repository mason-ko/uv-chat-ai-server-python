from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from .llm import llm

def translate_text(message: str, target_language: str) -> str:
    prompt = ChatPromptTemplate.from_template(
        "Translate '{message}' to {target_language} in a simple, concise way without any pronunciation or additional explanations."
    )
    chain = prompt | llm | StrOutputParser()
    result = chain.invoke({"message": message, "target_language": target_language})
    return result
