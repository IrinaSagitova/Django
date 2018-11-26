import datetime
from .settings import FILES_PATH
import os
from django.shortcuts import render
from django.views.generic import TemplateView


class FileList(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, date=None):
        # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
        f_list = []
        for f in os.listdir(FILES_PATH):
            path_f = os.stat(os.path.join(FILES_PATH, f))
            data_f = datetime.fromtimestamp(int(path_f.st_ctime)).date()
            if date == None or data_f <= date:
                f_list.append(
                    {'name': f,
                     'ctime': datetime.fromtimestamp(int(path_f.st_ctime)).date(),
                     'mtime': datetime.fromtimestamp(int(path_f.st_mtime)).date()
                     })
        return {'files': f_list}


def file_content(request, name):
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    with open(os.path.join(FILES_PATH, name), encoding='utf-8') as file:
        content = file.read()
    return render(
        request,
        'file_content.html',
        context={'file_name': name, 'file_content': content}
    )