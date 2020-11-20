from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.views.generic import FormView
from .models import *
from .forms import *


class MyRegisterFormView(FormView):
    form_class = UserCreationForm

    success_url = "/accounts/login/"
    template_name = "signup.html"

    def form_valid(self, form):
        form.save()
        return super(MyRegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(MyRegisterFormView, self).form_invalid(form)


def logout(request):
    return render(request, "logout.html")


def products(request):
    context = {"data_p": Product.objects.all()}
    return render(request, "products.html", context)


def auctions(request):
    context = {"data_a": Auction.objects.all()}
    return render(request, "auctions.html", context)


def farms(request):
    context = {"data_f": Farm.objects.all()}
    return render(request, "farms.html", context)


def product_delete(request, product_id):
    try:
        c = Product.objects.get(id=product_id)
        c.delete()
        context = {"data_p": Product.objects.all()}
        return render(request, 'products.html', context)
    except Product.DoesNotExist:
        return HttpResponseNotFound("<h2>Task not found</h2>")


def product_edit(request, product_id):
    try:
        data_p = Product.objects.get(id=product_id)
        data_f = Farm.objects.all()
        if request.method == "POST":
            data_p.name = request.POST.get("name")
            data_p.count = request.POST.get("count")
            data_p.cost = request.POST.get("cost")
            data_p.farm = request.POST.get("farm")
            data_p.save()
            return render(request, 'products.html', {"data_p": Product.objects.all()})
        else:
            return render(request, "product_edit.html", {"data_p": data_p, "data_f": data_f})
    except Product.DoesNotExist:
        return HttpResponseNotFound("<h2>Task not found</h2>")


def auction_add(request):
    form = Auction_form(request.POST or None)
    if form.is_valid():
        form.save()
        temp = Auction.objects.get(product=form.cleaned_data['product'],
                                   username=form.cleaned_data['username'],
                                   count=form.cleaned_data['count'],
                                   cost=form.cleaned_data['cost'],
                                   date=form.cleaned_data['date']
                                   )
        temp_p = Product.objects.get(name=temp.product)
        print(temp_p.count)
        print(temp.count)
        temp_p.count = temp_p.count - temp.count
        temp_p.save()
        context = {"data_a": Auction.objects.all()}
        return render(request, "auctions.html", context)
    context = {'form': form, 'data_u': User.objects.all(), 'data_p': Product.objects.all()}
    return render(request, "auction_add.html", context)


def farm_add(request):
    form = Farm_form(request.POST or None)
    if form.is_valid():
        form.save()
        context = {"data_f": Farm.objects.all()}
        return render(request, "farms.html", context)
    context = {'form': form}
    return render(request, "farm_add.html", context)


def product_add(request):
    form = Product_form(request.POST or None)
    if form.is_valid():
        form.save()
        context = {"data_p": Product.objects.all()}
        return render(request, "products.html", context)
    context = {'form': form, 'data_f': Farm.objects.all()}
    return render(request, "product_add.html", context)


def account(request, user_id):
    context = {"user": User.objects.get(id=user_id), "data_a":Auction.objects.all()}
    return render(request, "account.html", context)
