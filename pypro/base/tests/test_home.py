import pytest as pytest
from django.urls import reverse
from pypro.django_assertions import assert_contains


@pytest.fixture
def resp(client, db):
    return client.get(reverse('base:home'))


def test_status_code(resp):
    assert resp.status_code == 200


def test_title(resp):
    assert_contains(resp, '<title>Python Pro - Home</title>')


def test_home_link(resp):
    assert_contains(resp, f'href="{reverse("base:home")}">PythonPro</a>')


def test_email_link(resp):
    assert_contains(resp, 'href="mailto:ramalho@pythonpro.com.br"')
