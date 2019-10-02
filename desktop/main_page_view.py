from django.shortcuts import render

def main_page(request):
    context = dict()
    if request.user.is_authenticated:
        context["username"] = request.user.username
        context["user_is_authenticated"] = True
    else:
        context["user_is_authenticated"] = False

    # return render(request, 'desktop/main_page.html', context)
    return render(request, 'desktop/main_page.html', context)