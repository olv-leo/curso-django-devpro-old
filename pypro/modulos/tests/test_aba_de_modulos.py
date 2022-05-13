import pytest as pytest
from django.test import Client
from django.urls import reverse
from model_mommy import mommy
from pypro.django_assertions import assert_contains

@pytest.fixture
def modulos(db):
    return mommy.make(Modulo, 2)


@pytest.fixture
def resp(client, modulos):
    return client.get(reverse('base:home'))

def test_titulos_dos_modulos(resp, modulos):
    for modulo in modulos:
        assert_contains(resp, modulo.titulo)

