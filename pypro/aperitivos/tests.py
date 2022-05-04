import pytest
from django.urls import reverse


@pytest.fixture
def resp(client):
    return client.get(reverse('aperitivos:video', args=('motivacao',)))

#Testando se o acesso a página está acontecendo com sucesso.
def test_status_code(resp):
    assert resp.status_code == 200
