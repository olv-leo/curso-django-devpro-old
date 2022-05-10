from django.shortcuts import render

videos = [
    {'slug': 'motivacao', 'titulo': 'Vídeo Aperitivo: Motivação', 'vimeo_id': '705098707',
     'page_title': 'Python Pro - Aperitivo'},
    {'slug': 'feynman', 'titulo': 'Aula 01 - Técnica Feynman', 'vimeo_id': '708273691',
     'page_title': 'Python Pro - Feynman'},
]

videos_dct = {dct['slug']: dct for dct in videos}


def indice(request):
    return render(request, 'aperitivos/indice.html', context={'videos': videos})


def video(request, slug):
    video = videos_dct[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
