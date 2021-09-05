from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django import forms
from core.models import UrlKey
from django.db.models import F
from django.contrib.auth.decorators import login_required


class UrlForm(forms.ModelForm):
	class Meta:
		model = UrlKey
		fields = ('url',)

@login_required
def index(request):
	ctx = {}
	form = UrlForm(request.POST or None)
	if form.is_bound and form.is_valid():
		obj = form.save()
		ctx['key'] = obj.key
		form = UrlForm()
	ctx['form'] = form
	return render(request, 'short_url.html', ctx)


def redireсt_url(request, key):
	try:
		model = UrlKey.objects.get(key=key)
	except Model.DoesNotExists:
		return redirect('start')
	url = model.url
	model.redirect_count = F('redirect_count') + 1
	model.save()
	return redirect(to=url)


def create_user(request):
	form = UserCreationForm(request.POST or None)
	if form.is_bound and form.is_valid():
		form.save()
		return redirect('start')
	return render(request, 'create_user.html', {'form': form})