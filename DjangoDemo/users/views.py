import collections
import time
from django.views.decorators.http import require_http_methods
from .forms import LoginForm
from django.contrib import auth
from django.http import HttpResponse, JsonResponse
from rest_framework_jwt.serializers import RefreshJSONWebTokenSerializer
from rest_framework_jwt.authentication import jwt_decode_handler
from rest_framework_jwt.utils import jwt_decode_handler
from rest_framework_jwt.views import RefreshJSONWebToken
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

import json
# Create your views here.

@require_http_methods(['POST'])
def login(request):
    form = LoginForm(request.POST)
    print(request.POST)
    if form.is_valid():
        print("valid request")
    username = form.cleaned_data['username']
    print('the username is : ', username)
    # password = form.cleaned_data['password']
    # content = json.loads(request.body.decode('utf-8'))
    # username = content['username']
    # password = content['password']
    user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
    if user is not None and user.is_active:
        auth.login(request, user)
        token = generate_token(user)
        time.sleep(1)
        attr_token = collections.OrderedDict({'token': token})
        refresh_token_class = RefreshJSONWebTokenSerializer().validate(attr_token)
        refresh_token = refresh_token_class['token']
        print(token, 'and', refresh_token_class['token'])
        return HttpResponse(JsonResponse({'message': 'success', 'token': token, 'refresh_token': refresh_token}))
    else:
        return HttpResponse(JsonResponse({'message': 'fail'}))
def generate_token(user):
    from rest_framework_jwt.settings import api_settings
    jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
    payload = jwt_payload_handler(user)
    return jwt_encode_handler(payload)

@require_http_methods(['GET'])
def logout(request):
    auth.logout(request)
    return HttpResponse("退出登录成功")
