import json

from django.views.generic import View
from django.http import HttpResponse

from .models import Company


class CompanyList(View):

    def _serialize(self, company):
        return {
            "name": company.name,
            "address": company.address,
            "registration_number": company.registration_number
        }

    def get(self, request):
        companies = []
        for company in Company.objects.all():
            companies.append(self._serialize(company))

        return HttpResponse(json.dumps(companies), content_type='application/json')
