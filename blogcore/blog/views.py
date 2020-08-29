from django.shortcuts import render

def post_list(request):
    param_for_recive_list=['Петя','Вася','Оля','Катя']
    return render(request,'blog/index.html',context={"var_for_html_templ": param_for_recive_list})