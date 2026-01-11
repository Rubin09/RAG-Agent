from ...config.ConversationalRAGconfig import get_hugginface_api
from langchain_huggingface import HuggingFaceEmbeddings, ChatHuggingFace,HuggingFaceEndpoint

   
def get_llm():

    """
    Generate a response from Hugging Face LLm

    Args:
        prompt (str): The input prompt to send to the model.

    Returns:
        str: The generated response text.
    """
    hf_token = get_hugginface_api()
    llm_base = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation",
    huggingfacehub_api_token=hf_token,
    temperature = 0.7,
    )

    
    return ChatHuggingFace(llm=llm_base)