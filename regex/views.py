import re

from django.shortcuts import render


def display_matching_patterns(request):
    """It deals with finding all occurrences of a regular expression in a text string and displays the matching
    patterns.

    :param request: a POST request in which the regex and text_string data are sent
    :return: all occurrences found rendered in the html template
    """
    data = request.POST
    text_string = data.get('text_string')
    regex = data.get('regex')
    strings_found = re.findall(regex, text_string)
    context = {'strings_found': strings_found}
    return render(request, 'regex.html', context)
