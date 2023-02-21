from rest_framework.response import Response
from rest_framework.decorators import api_view
from projectApp.models import MasterTable

@api_view(['GET'])
def home(request, id):
    table=MasterTable.objects.all()
    user=table.filter(userdataid=id)
    data={}
    for sec in user.section.all():
        s=user.filter(section=sec)
        for page in s.page.all():
            data={**data, s.section: page}
    return Response(data)