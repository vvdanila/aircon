import json

from django.views.generic import View
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Client


class ClientList(View):

    def _serialize(self, client):
        return {
            "name": client.name,
            "address": client.address,
            "client_id": client.client_id
        }

    def get(self, request):
        clients = []
        for client in Client.objects.all():
            clients.append(self._serialize(client))

        return HttpResponse(json.dumps(clients), content_type='application/json')

    def post(self, request):

        print("post:", request.POST)

        data = {
            "name": request.POST.get("name"),
            "address": request.POST.get("address"),
            "client_id": request.POST.get("client_id"),
        }
        print("data:", data)
        new_client = Client(**data)
        new_client.save()

        return HttpResponse(status=201)
