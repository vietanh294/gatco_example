from application.extensions import apimanager
from application.models.model import User, QuocGia, TinhThanh
from application.extensions import auth
from gatco.exceptions import ServerError
from gatco_restapi import  ProcessingException

def auth_func(request=None, **kw):
    #uid = auth.current_user(request)
    #if uid is None:
    #    raise ServerError("abc")
    
    pass

apimanager.create_api(User,
    methods=['GET', 'POST', 'DELETE', 'PUT'],
    url_prefix='/api/v1',
    preprocess=dict(GET_SINGLE=[auth_func], GET_MANY=[auth_func], POST=[auth_func], PUT_SINGLE=[auth_func]),
    collection_name='user',
    include_columns=['id', 'birthday', 'email','is_active'])

apimanager.create_api(collection_name='quocgia', Model=QuocGia,
    methods=['GET', 'POST', 'DELETE', 'PUT'],
    url_prefix='/api/v1',
    preprocess=dict(GET_SINGLE=[auth_func], GET_MANY=[auth_func], POST=[auth_func], PUT_SINGLE=[auth_func]),
    )

apimanager.create_api(collection_name='tinhthanh', Model=TinhThanh,
    methods=['GET', 'POST', 'DELETE', 'PUT'],
    url_prefix='/api/v1',
    preprocess=dict(GET_SINGLE=[auth_func], GET_MANY=[auth_func], POST=[auth_func], PUT_SINGLE=[auth_func]),
    )