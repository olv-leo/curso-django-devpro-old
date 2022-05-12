import pytest
from django.urls import reverse
from pypro.aperitivos.models import Video
from pypro.django_assertions import assert_contains
from model_mommy import mommy


@pytest.fixture
def video(db):
    return mommy.make(Video)

@pytest.fixture
def resp(client, video):
    return client.get(reverse('aperitivos:video', args=(video.slug,)))


@pytest.fixture
def resp_video_nao_encontrado(client, video):
    return client.get(reverse('aperitivos:video', args=(video.slug+'video_nao_encontrado',)))


# Testando se o acesso a página está acontecendo com sucesso.
def test_status_code(resp):
    assert resp.status_code == 200


def test_status_code_video_nao_encontrado(resp_video_nao_encontrado):
    assert resp_video_nao_encontrado.status_code == 404


def test_title_video(resp, video):
    assert_contains(resp, f'<h1 class="mt-4 mb-3">{video.titulo}</h1>')


def test_conteudo_video(resp, video):
    assert_contains(resp, f'<iframe src="https://player.vimeo.com/video/{video.vimeo_id}"')
