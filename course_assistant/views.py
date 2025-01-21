from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain_chroma import Chroma
from langchain.prompts import ChatPromptTemplate
from AI.OpenAIClient import OpenAIClient

from django.shortcuts import render

from backend.constants import CHROMA_PATH
from course_assistant.constants import PROMPT_TEMPLATE

@api_view(['POST'])
def ask_question(request):
    try:
        query = request.data.get("query", "").strip()

        # check parameter is available in requst
        if not query:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={"error": "Query parameter is required."}
            )
        
        # Find relevant text in vector database
        embedding_func = OpenAIEmbeddings()
        db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_func)
        results = db.similarity_search_with_relevance_scores(query, k=1)

        # Accumulate doc context 
        context_text = "\n\n--\n\n".join([doc.page_content for doc, _score in results])

        # make request to OpenAI
        client = OpenAIClient()
        response = client.send_message_ask_question(query, context_text)

        return Response(
                status=status.HTTP_200_OK,
                data={
                    'curriculum': [
                        {
                            'meta_data': results[0][0].metadata,
                            'contents': results[0][0].page_content,
                            'score': results[0][1]
                        }
                    ],
                    'open_ai_response': response.dict()
                }
            )
    except Exception as e:
        print(f"Error: {e}")
        return Response(
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            data={'error': str(e)}
        )
