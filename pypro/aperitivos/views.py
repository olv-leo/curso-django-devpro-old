from django.shortcuts import render


class Video:
    def __init__(self, slug, titulo, vimeo_id, page_title):
        self.slug = slug
        self.titulo = titulo
        self.page_title = page_title
        self.vimeo_id = vimeo_id

videos = [
    Video('motivacao', 'Vídeo Aperitivo: Motivação', '705098707', 'Python Pro - Aperitivo'),
    Video('feynman', 'Aula 01 - Técnica Feynman','708273691', 'Python Pro - Feynman'),
]

videos_dct = {v.slug: v for v in videos}


def indice(request):
    return render(request, 'aperitivos/indice.html', context={'videos': videos})


def video(request, slug):
    video = videos_dct[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
