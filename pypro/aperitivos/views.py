from django.shortcuts import render


def video(request, slug):
    videos = {
        'apresentacao': {'titulo': 'Vídeo Aperitivo: Motivação', 'vimeo_id': '705098707',
                         'page_title': 'Python Pro - Aperitivo'},
        'feynman': {'titulo': 'Aula 01 - Técnica Feynman', 'vimeo_id': '708273691',
                    'page_title': 'Python Pro - Feynman'},
    }
    video = videos[slug]

    return render(request, 'aperitivos/video.html', context={'video': video})
