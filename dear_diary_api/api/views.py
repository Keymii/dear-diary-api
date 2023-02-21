from rest_framework.response import Response
from rest_framework.decorators import api_view
from projectApp.models import MasterTable

@api_view(['GET'])
def home(request, user):
    table=MasterTable.objects.all()
    user=table.filter(user=user)
    '''for sec in user:
        s=user.filter(section=sec)
        for page in s.page.all():
            data={**data, s.section: page}
    return Response(data)'''
    sections=[]
    pages=[]
    for i in user:
        sections.append(i.section)
    sections=[*set(sections)]
    for section in sections:
        page=user.filter(section=section)
        section_page=[]
        for j in page:
            section_page.append(j.page)
        pages.append(section_page)
    data=dict(zip(sections, pages))
    return Response(data)
