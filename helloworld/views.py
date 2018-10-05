from django.shortcuts import render,redirect   # 加入 redirect 套件
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.template import loader
from guestbook.models import TextMessage
from guestbook.models import PictureMessage
import random

def index(request):
	template = loader.get_template('guestbookver1.html')
	pictures = [
	'https://images.unsplash.com/photo-1536228767230-783ad0b61dd9?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=c89d5a12f9cfc95dcda865d1e971d3a8&auto=format&fit=crop&w=1950&q=80',
	'https://images.unsplash.com/photo-1536210133278-5e870d9d569b?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=17e5893343edd74e303a4189eca5d406&auto=format&fit=crop&w=1050&q=80',
	'https://images.unsplash.com/photo-1536308304182-5a2e0e04bb08?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=f086e0c56cf55e117c1dcc58aa83d6ab&auto=format&fit=crop&w=967&q=80',
	'https://images.unsplash.com/photo-1536300947881-070c913b69b9?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=156e2cf55899c41cbbdd2237f2093fb2&auto=format&fit=crop&w=634&q=80',
	'https://images.unsplash.com/photo-1536559692556-79e8be88e8ab?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=97d54d56f7e8c363cda42b6651896f68&auto=format&fit=crop&w=634&q=80',
	'https://images.unsplash.com/photo-1537528201119-94ad9830acc6?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=08bb8f14ad9f4afe8723d48fabf38fe0&auto=format&fit=crop&w=600&q=60',
	'https://images.unsplash.com/photo-1537526421896-c86df03a8452?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=8c06b95a1746d91ad19cda1edb05ecd7&auto=format&fit=crop&w=600&q=60',
	'https://images.unsplash.com/photo-1537525993299-045a6b04759a?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=caa406977a1697806de2d65dfbe6aa16&auto=format&fit=crop&w=600&q=60',
	'https://images.unsplash.com/photo-1537517812565-2d44597c3eff?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=38a5865008eb0da603a833b507781973&auto=format&fit=crop&w=600&q=60',
	'https://images.unsplash.com/photo-1537517025403-65ef82973508?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=47c10b42f7111e37066a456e5658da9e&auto=format&fit=crop&w=600&q=60',
	'https://images.unsplash.com/photo-1537504271830-efdadab508e7?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=6eae56a67fad1a58846b08413b9fa244&auto=format&fit=crop&w=600&q=60',
	'https://images.unsplash.com/photo-1537488265546-ccea6b0276aa?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=e3b4a3a26ee1977ab52ba64c8d3e3257&auto=format&fit=crop&w=600&q=60',
	'https://images.unsplash.com/photo-1537518588317-e5cc1e331f88?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=f242bda8133dad4100b8841254830690&auto=format&fit=crop&w=600&q=60',
	'https://images.unsplash.com/photo-1537512786933-dda1dd51f47c?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=bf2cc3a7dc81936ab2eb92c57bbce5f6&auto=format&fit=crop&w=600&q=60',
	'https://images.unsplash.com/photo-1537479664518-1f74e0830ce9?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=dbe6fef0488e61d26a4a0150f1be2345&auto=format&fit=crop&w=600&q=60',
	'https://images.unsplash.com/photo-1537481614698-f0e2f82e2c62?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=71f3a6828cce182adcf737197329d725&auto=format&fit=crop&w=600&q=60',
	'https://images.unsplash.com/photo-1537474988800-bd56a8c361a6?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=0927eea1286e1198567a41206846a5e3&auto=format&fit=crop&w=600&q=60',
	'https://images.unsplash.com/photo-1537471382899-3ad916b3b745?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=8edb2a3256b4b994fa2134d86981ccd9&auto=format&fit=crop&w=600&q=60',
	'https://images.unsplash.com/photo-1537459035957-f3165448c7ea?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=cbeda0984a754a283355e8c1a4686ad3&auto=format&fit=crop&w=600&q=60',
	'https://images.unsplash.com/photo-1537420268456-f92a8382fc5d?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=e9a24bb72c13d710f3ed64a2c59c1968&auto=format&fit=crop&w=600&q=60',
	'https://images.unsplash.com/photo-1537396057802-87d0127d5271?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=6f473b4da5d289d0765c1f77a15c0fa0&auto=format&fit=crop&w=600&q=60',
	'https://images.unsplash.com/photo-1537420371683-0017ae637893?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=7ce424ad3da7637e1bfbbe32a182bd8b&auto=format&fit=crop&w=600&q=60',
	'https://images.unsplash.com/photo-1537415984076-6ed31437b3c9?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=c19c92eb9e4aa991089c3e0c3a9dd826&auto=format&fit=crop&w=600&q=60',
	'https://images.unsplash.com/photo-1537392719903-ecaf9b486e31?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=c4a6a56294f208a1f5dc2c865d1611b5&auto=format&fit=crop&w=600&q=60',
	'https://images.unsplash.com/photo-1537431422278-32a079615207?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=a561bb5dd6afa596e8e8967eceedcd05&auto=format&fit=crop&w=600&q=60',
	'https://images.unsplash.com/photo-1537410056906-d336ddf64024?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=44d277a3d8e1ca12d213ace48f58040a&auto=format&fit=crop&w=600&q=60',
	'https://images.unsplash.com/photo-1537416064394-6369beecee65?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=8eccd4b106fb08ddb4072171b5c695b0&auto=format&fit=crop&w=600&q=60',
	'https://images.unsplash.com/photo-1537351963512-438ef58ed8c1?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=36c055f841e96e0ef9d9b789bce4eae0&auto=format&fit=crop&w=600&q=60',
	'https://images.unsplash.com/photo-1537352867670-2c0fed42e909?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=72ae4ef87d6c37894e0e3ce315d516ee&auto=format&fit=crop&w=600&q=60',
	'https://images.unsplash.com/photo-1537246239611-d0661025f2de?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=9bb284a583e599c06a42d7d87d1dee9c&auto=format&fit=crop&w=600&q=60',
	]
	r = random.sample(pictures, 20)
	context = {"pictures" : pictures, "random" : r}

	t1 = TextMessage.objects.create(talker = 'Micheal', message = 'Hello Professor!')
	t2 = TextMessage.objects.create(talker = 'Ken', message = 'Hello Professor!')
	t3 = TextMessage.objects.create(talker = 'Clinton', message = 'Hello Professor!')
	
	msgs = TextMessage.objects.all()


	for i in range(20):
		PictureMessage.objects.create(link = r[i])

	pic = PictureMessage.objects.all()
	#return HttpResponse(template.render(context, request))
	return render(request, 'guestbookver1.html', locals())
