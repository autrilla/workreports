import functools

from pyramid.httpexceptions import HTTPFound, HTTPForbidden
from pyramid.response import Response
from pyramid.security import remember, forget
from pyramid.view import view_config, forbidden_view_config

from ..models import User


@view_config(route_name='login')
def login(request):
    username = request.json_body.get('username', '')
    password = request.json_body.get('password', '')
    query = request.dbsession.query(User)
    user = query.filter(User.username == username).first()

    if user and user.verify_password(password):
        headers = remember(request, username)
        return HTTPFound(location=request.route_url('home'), headers=headers)
    else:
        return Response("Invalid username or password")


@view_config(route_name='logout')
def logout(request):
    headers = forget(request)
    return HTTPFound(location=request.route_url('home'), headers=headers)


def login_required(func):
    @functools.wraps(func)
    def f(request, *args, **kwargs):
        if not request.authenticated_userid:
            return HTTPForbidden()
        func()
    return f


@view_config(route_name='home')
@login_required
def home(request):
    return Response('Hello, {}'.format(request.authenticated_userid))


@forbidden_view_config()
def forbidden(request):
    if request.authenticated_userid:
        return HTTPForbidden()
    return HTTPFound(location=request.route_url('home'))
