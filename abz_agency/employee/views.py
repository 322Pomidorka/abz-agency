from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView

from .models import Employees


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def show_employees(request):
    # if request.is_ajax():
    #     request.GET['children_id']
    #
    #     node = Employees.objects.get(id=)
    #
    # else:
    employees_list = Employees.objects.filter(level__in=[0, 1])

    return render(request, 'index.html', {'employees_list': employees_list})


def full_info_employees(request):
    template_name = 'employees.html'
    if is_ajax(request):
        sort_by = request.GET.get('sort_by')
        search_text = request.GET.get('q_search')
        employees = Employees.objects.order_by(sort_by).filter(Q(first_name__icontains=search_text)
                                                               | Q(last_name__icontains=search_text)
                                                               | Q(employment_position__icontains=search_text)
                                                               | Q(salary__icontains=search_text)
                                                               | Q(employment_start_date__icontains=search_text))

        template_name = 'employees_all_sort.html'
    else:
        employees = Employees.objects.order_by('date_added')

    context = {}
    current_page = Paginator(list(employees), 20)
    page = request.GET.get('page')
    try:
        context['employees'] = current_page.page(page)
    except PageNotAnInteger:
        context['employees'] = current_page.page(1)
    except EmptyPage:
        context['employees'] = current_page.page(current_page.num_pages)
    return render(request, template_name, context)


# class QSearchEmployees(ListView)
#     template_name = 'employees_all_sort.html'