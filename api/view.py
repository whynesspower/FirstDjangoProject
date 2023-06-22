from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def getData():
	person={'name':'John', 'age':40}
	return Response(person)
