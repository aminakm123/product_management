import datetime
import json

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.db.models import Q
from django.http.response import HttpResponse

from main.functions import generate_form_errors
from product.forms import CategoryForm
from product.forms import ProductForm
from product.models import Category, Product




# category crud starts here
def create_category(request):
    
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            if not Category.objects.filter(name=name,is_deleted=False).exists():
                Category(                    
                    name = name
                ).save()
                response_data = {
                    "status": "true",
                    "title": "Successfully Created",
                    "message": "Category created successfully.",
                    "redirect": "true",
                    "redirect_url": reverse('product:categories')
                }
            else:    
                response_data = {
                    "status": "false",
                    "stable": "true",
                    "title": "This category already exists",
                    "message": "Category already exists",                        
                }
        else:
            message = generate_form_errors(form, formset=False)
            
            response_data = {
                "stable": "true",
                "status": "form_error",
                "title": "Form validation error",
                "message": str(message),               
            }
        return HttpResponse(json.dumps(response_data), content_type='application/json')
    else:
        form = CategoryForm()
        context = {
            "title": "Create Category",
            "form": form,
            "redirect": "true",
            "create":True
        }
        return render(request, 'category/create_category.html', context)

def categories(request):
    instances = Category.objects.filter(is_deleted=False)
    paginator = Paginator(instances,1000000000000)
    page_number = request.GET.get('page')
    instances = paginator.get_page(page_number)
    context = {
        'instances': instances,
        "title": 'Categories',
    }
    return render(request, "category/categories.html", context)


def edit_category(request, pk):
    instance = get_object_or_404(Category.objects.filter(pk=pk, is_deleted=False))
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=instance)

        if form.is_valid():
            data = form.save(commit=False)
            data.updator = request.user
            data.date_updated = datetime.datetime.now()
            data.save()

            response_data = {
                "status": "true",
                "redirect" : "true",
                "title": "Successfully Updated",
                "message": "Category updated successfully.",                
                "redirect_url": reverse('product:categories')
            }

        else:
            message = generate_form_errors(form, formset=False)
            response_data = {
                "stable": "true",
                "status": "form_error",
                "message": str(message),
                "title": "Form validation error"  
            }
        return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    else:
        form = CategoryForm(instance=instance)
        context = {
            "form": form,
            "instance": instance,
            "title": "Edit Category :" + instance.name,
            "redirect": "true",
            "url": reverse('product:edit_category', kwargs={'pk': instance.pk})
        }
        return render(request, 'category/create_category.html', context)
    

def category(request, pk):
    instance = get_object_or_404(Category.objects.filter(pk=pk,is_deleted=False))
    context = {
        'instance': instance,
        'title': 'Category'
    }
    return render(request, "category/category.html", context)


def delete_category(request,pk):
    instance = get_object_or_404(Category.objects.filter(pk=pk,is_deleted=False))
    Category.objects.filter(pk=pk).update(is_deleted=True,name=instance.name)
    response_data = {
        "status" : "true",        
        "title" : "Successfully Deleted",
        "message" : "Category Successfully Deleted.", 
        "redirect" : "true",       
        "redirect_url" : reverse('product:categories')
    }
    return HttpResponse(json.dumps(response_data), content_type='application/javascript')
