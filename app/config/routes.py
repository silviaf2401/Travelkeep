"""
    Routes Configuration File

    Put Routing rules here
"""
from system.core.router import routes

"""
    This is where you define routes

    Start by defining the default controller
    Pylot will look for the index method in the default controller to handle the base route

    Pylot will also automatically generate routes that resemble: '/controller/method/parameters'
    For example if you had a products controller with an add method that took one parameter
    named id the automatically generated url would be '/products/add/<id>'
    The automatically generated routes respond to all of the http verbs (GET, POST, PUT, PATCH, DELETE)
"""
routes['default_controller'] = 'Welcome'
routes['POST']['/logincheck']='Welcome#logincheck'
routes['POST']['/regcheck']='Welcome#regcheck'
routes['GET']['/register']='Welcome#register'
routes['GET']['/login']='Welcome#login'
routes['GET']['/dashboard']='Welcome#dashboard'
routes['GET']['/logout']='Welcome#logout'
routes['GET']['/tripsbydate'] = 'Welcome#tripsbydate'
routes['POST']['/fbcheck'] = 'Welcome#fbcheck'
routes['GET']['/milestraveled']='Welcome#milestraveled'
routes['POST']['/calculatemilestraveled']='Welcome#calculatemilestraveled'
routes['GET']['/ongoingtrip'] = 'Welcome#ongoing'
routes['POST']['/submit_ongoing'] = 'Welcome#submit_ongoing'
routes['GET']['/favoritetrips'] = 'maxcontroller#get_fav'
routes["GET"]['/welcome/detailed_trip_routing/<name>'] = 'maxcontroller#detailed_trip'
routes['POST']['/Welcome/get_query'] = 'maxcontroller#get_query'
routes["GET"]['/map/page'] = 'maxcontroller#maps'
routes["GET"]['/welcome/test'] = 'maxcontroller#test'
routes["POST"]['/Welcome/get_place'] = 'maxcontroller#get_place'
routes['GET']['/addfriend']='Welcome#addfriend'
routes['POST']['/delete/<friend_id>']='Welcome#deletefriend'
routes['POST']['/addfriend/<friend_id>']='Welcome#add'
routes['GET']['/viewfriendstrips']='Welcome#viewfriendstrips'
routes['POST']['/createtrip'] = 'Welcome#createtrip'
routes['POST']['/upload/photo'] = 'Welcome#upload_photo'
routes['POST']['/upload/video'] = 'Welcome#upload_video'
routes['POST']['/addtrip'] = 'Welcome#add_trip'
routes['POST']['/completetrip'] = 'Welcome#complete_trip'

