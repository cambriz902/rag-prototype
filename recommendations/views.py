from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

from django.shortcuts import render

from recommendations.constants import CHROMA_PATH

@api_view(['POST'])
def recommend_papers(request):
    try:
        query = request.data.get("query", "").strip()
        
        if not query:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={"error": "Query parameter is required."}
            )
        
        embedding_func = OpenAIEmbeddings()
        db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_func)
        results = db.similarity_search_with_relevance_scores(query, k=1)

        return Response(
                status=status.HTTP_200_OK,
                data={'papers': [
                    {
                        'meta_data': results[0][0].metadata,
                        'contents': results[0][0].page_content,
                        'score': results[0][1]
                    }
                ]}
            )
    except Exception as e:
        print(f"Error: {e}")
        return Response(
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            data={'error': str(e)}
        )
