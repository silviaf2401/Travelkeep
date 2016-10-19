
"""
    Sample Model File

    A Model should be in charge of communicating with the Database.
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model
import re
from datetime import datetime

class WelcomeModel(Model):
    def __init__(self):
        super(WelcomeModel, self).__init__()

    def login_user(self, user_info):
        errors=[]
        EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')

        if not user_info['email']:
            errors.append('Email cannot be blank')
        elif not EMAIL_REGEX.match(user_info['email']):
            errors.append('Email format must be valid!')
        if not user_info['password']:
            errors.append('Password cannot be blank')

        if errors:
            return {"status": False, "errors": errors}

        user_query = "SELECT * FROM users WHERE email = :email LIMIT 1"
        user_data = {'email': user_info['email']}
        user = self.db.query_db(user_query, user_data)
        if user:
           # check_password_hash() compares encrypted password in DB to one provided by user logging in
            if self.bcrypt.check_password_hash(user[0]['password'], user_info['password']):
                return {"status": True, "user": user[0]}
        errors.append('User was not found in database. Please try a different user name/password combination or click on register below')
        # Whether we did not find the email, or if the password did not match, either way return False
        return {"status": False, "errors": errors}

    def create_user(self, info):
        # We write our validations in model functions.
        # They will look similar to those we wrote in Flask
        EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
        errors = []
        # Some basic validation
        if not info['first_name']:
            errors.append('First name cannot be blank')
        if not info['last_name']:
            errors.append('Last name cannot be blank')
        if not info['email']:
            errors.append('Email cannot be blank')
        elif not EMAIL_REGEX.match(info['email']):
            errors.append('Email format must be valid!')
        if not info['password']:
            errors.append('Password cannot be blank')
        elif info['password'] != info['pw_confirmation']:
            errors.append('Password and confirmation must match!')
        # If we hit errors, return them, else return True.
        if errors:
            return {"status": False, "errors": errors}
        else:
            password = info['password']
        # bcrypt is now an attribute of our model
        # we will call the bcrypt functions similarly to how we did before
        # here we use generate_password_hash() to generate an encrypted password
            email = info['email']
            user_query = "SELECT * FROM users WHERE email = :email LIMIT 1"
            query_data = { 'email': email }
            user = self.db.query_db(user_query, query_data)
            if user != []:
                errors.append("An account is already associated with that e-mail address, please login instead")
                return {"status": False, "errors": errors}
            else:
                user_query ="SELECT * FROM users LIMIT 1"
                user = self.db.query_db(user_query)
                if user !=[]:
                    hashed_pw = self.bcrypt.generate_password_hash(password)
                    create_query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at, share_w_friends, picture) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW(), :share_w_friends, :picture)"
                    create_data = {'first_name': info['first_name'], 'last_name': info['last_name'], 'email': info['email'], 'password': hashed_pw, 'share_w_friends': 0, 'picture': "/static/img/default.png"}
                    self.db.query_db(create_query, create_data)# Code to insert user goes here...
            # Then retrieve the last inserted user.
                    get_user_query = "SELECT * FROM users ORDER BY id DESC LIMIT 1"
                    users = self.db.query_db(get_user_query)
                    return { "status": True, "user": users[0] }
                else:
                    hashed_pw = self.bcrypt.generate_password_hash(password)
                    create_query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at, share_w_friends, picture) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW(), :share_w_friends, :picture)"
                    create_data = {'first_name': info['first_name'], 'last_name': info['last_name'], 'email': info['email'], 'password': hashed_pw, 'share_w_friends': 0, 'picture': "/static/img/default.png"}
                    self.db.query_db(create_query, create_data)# Code to insert user goes here...
            # Then retrieve the last inserted user.
                    get_user_query = "SELECT * FROM users ORDER BY id DESC LIMIT 1"
                    users = self.db.query_db(get_user_query)
                    return { "status": True, "user": users[0] }

    def fb_login(self, fb_user_info):

        # hash token so that it is encripted on client
        hashed_token = self.bcrypt.generate_password_hash(fb_user_info['FBtoken'])

        exists_user_query = "SELECT * FROM users WHERE email = :email LIMIT 1"
        exists_user_data = { 'email': fb_user_info['FBemail'] }
        exists_user = self.db.query_db(exists_user_query, exists_user_data)

        # login the fb user ASK if this is safe
        if exists_user:

            return { "status": True, "user": exists_user[0], "token": hashed_token }

        # Register the fb user
        else:

            EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
            errors = []
            # Some basic validation
            if not fb_user_info['FBtoken']:
                errors.append('Token cannot be blank')
            if not fb_user_info['FBfirst_name']:
                errors.append('First name cannot be blank')
            if not fb_user_info['FBlast_name']:
                errors.append('Last name cannot be blank')
            if not fb_user_info['FBemail']:
                errors.append('Email cannot be blank')
            elif not EMAIL_REGEX.match(fb_user_info['FBemail']):
                errors.append('Email format must be valid!')
            if not fb_user_info['FBid']:
                errors.append('id cannot be blank')
            # If we hit errors, return them, else return True.
            if errors:
                return {"status": False, "errors": errors}
            else:
                fb_create_query = "INSERT INTO users (first_name, last_name, email, share_w_friends, created_at, updated_at, picture) VALUES (:first_name, :last_name, :email, :share_w_friends, NOW(), NOW(), :picture)"
                fb_create_data = {'first_name': fb_user_info['FBfirst_name'], 'last_name': fb_user_info['FBlast_name'], 'email': fb_user_info['FBemail'], 'share_w_friends': 0, 'picture': fb_user_info['FBpicture']}
                new_user = self.db.query_db(fb_create_query, fb_create_data)# Code to insert user goes here...
                # Then retrieve the last inserted user.
                get_user_query = "SELECT * FROM users WHERE id = :id LIMIT 1"
                get_user_data = {'id': new_user}
                user = self.db.query_db(get_user_query,get_user_data)
                return { "status": True, "user": user[0], "token": hashed_token }



    def milestraveled(self, trip_info):
        sum =0;
        milesforeachmonth=[];
        i=1
        while i<13:
            milesforeachmonth.append(0);
            i= i+1
        #SELECT * from trips join favorites on trips.id = favorites.trip_id join users on users.id=favorites.user_id where users.id =1#
        #totmilestraveled_query ="SELECT * from trips join favorites on trips.id = favorites.trip_id join users on users.id=favorites.user_id where users.id =:user_id and trips.start_date BETWEEN :startdate and :enddate AND trips.rating =:triprating"
        totmilestraveled_query ="SELECT * from trips join participants on participants.trip_id =trips.id join users on participants.user_id=users.id WHERE users.id =:user_id and trips.start_date BETWEEN :startdate and :enddate AND trips.rating =:triprating"
        totmilestraveled_data = {'startdate': trip_info['start_date'], 'enddate': trip_info['end_date'], 'triprating': trip_info['rating'], 'user_id': trip_info['user_id']}
        totmilestraveled = self.db.query_db(totmilestraveled_query, totmilestraveled_data)
        print "this is totmilestraveled", totmilestraveled
        for element in totmilestraveled:
            for i in range(0,12):
                if element['end_date'].month == i+1:
                    milesforeachmonth[i]= milesforeachmonth[i]+ int(element['trip_miles'])
        print "This is the milesforeachmonth array ", milesforeachmonth
        for element in totmilestraveled:
            sum = sum + element['trip_miles']
        return milesforeachmonth

    def placesvisited(self, trip_info):
        #SELECT * from trips join favorites on trips.id = favorites.trip_id join users on users.id=favorites.user_id where users.id =1#
        #placesvisited_query ="SELECT end_location from trips join favorites on trips.id = favorites.trip_id join users on users.id=favorites.user_id where users.id =:user_id and trips.start_date BETWEEN :startdate and :enddate AND trips.rating =:triprating"
        placesvisited_query="SELECT end_location from trips join participants on participants.trip_id=trips.id join users on participants.user_id=users.id WHERE users.id =:user_id and trips.start_date BETWEEN :startdate and :enddate AND trips.rating =:triprating"
        placesvisited_data = {'startdate': trip_info['start_date'], 'enddate': trip_info['end_date'], 'triprating': trip_info['rating'], 'user_id': trip_info['user_id']}
        placesvisited = self.db.query_db(placesvisited_query, placesvisited_data)
        return placesvisited


    def get_user_by_id(self, user_id):
        # pass data to the query like so
      query = "SELECT id, first_name, last_name, email FROM users WHERE id = :user_id"
      data = { 'user_id': user_id}
      return self.db.query_db(query, data)


    def getallfriends(self, user_id):
        query = "SELECT * from users LEFT join friends on users.id=friends.user_id LEFT join users as users2 on users2.id= friends.friend_id WHERE users.id =:user_id"
        data = { 'user_id': user_id}
        list_friends= self.db.query_db(query, data)
        if list_friends[0]['first_name'] == None:
            num_friends=0
        else:
            num_friends=len(list_friends)
        list_friends[0]['num_friends']=num_friends        
        print "this is list_friends", list_friends 
        return list_friends

    def getallusersexceptselfandfriends(self, user_id):
        query= "SELECT * from users where users.id <>:user_id"
        data = {'user_id': user_id}
        usersbutself =self.db.query_db(query, data)
        print "this is usersbutself", usersbutself
        query2 = "SELECT * from users LEFT join friends on users.id=friends.user_id LEFT join users as users2 on users2.id= friends.friend_id WHERE users.id =:user_id"
        data2 = { 'user_id': user_id}
        allfriends = self.db.query_db(query2, data2)
        listallfriends =[]
        for element in allfriends:
            listallfriends.append(element['id'])
        prunedusers =[]
        for element in usersbutself:
            if element['id'] not in listallfriends:
                prunedusers.append(element)
        return prunedusers

    def delete(self, data):
        removefromdb_query="DELETE from friends WHERE user_id=:user_id and friend_id=:friend_id"
        return self.db.query_db(removefromdb_query, data)

    def add(self, data):
        print "this is data", data
        addtofriends_query="INSERT INTO friends (user_id, friend_id, created_at) VALUES (:user_id, :friend_id, NOW())"
        query_data={ 'user_id': data['user_id'],
                    'friend_id': data['friend_id']}
        test = self.db.query_db(addtofriends_query, query_data)
        return test

    def viewfriendstrips(self, data):
        print "data", data
        #query_friends = "SELECT users2.id from users LEFT join friends on users.id=friends.user_id LEFT join users as users2 on users2.id= friends.friend_id WHERE users.id =:user_id"
        query_friends = "Select U.first_name, U.last_name, T.trip_miles, T.end_location, T.name, T.start_date, T.end_date, T.rating from friends F join participants P on P.user_id = F.friend_id join Trips T on T.id = P.trip_id join users U on U.id = F.friend_id where F.user_id =:user_id ORDER BY F.friend_id DESC"
        data = {'user_id': data['user_id']}
        query_friends=self.db.query_db(query_friends, data)
        print "this is query_friends", query_friends
        #print query_friends[0], "this is query_friends['id']"
        #query_trips = "SELECT * from trips join participants on participants.trip_id=trips.id WHERE participants.user_id =:friend_id"

        #data_trips ={ 'friend_id': query_friends[0]['id']}

        #friends_trips=self.db.query_db(query_trips, data_trips)
        #print friends_trips, "this is friends_trips"
        return query_friends

    def getAllTrips(self):
        query = "SELECT * FROM trips ORDER BY start_date DESC"
        return self.db.query_db(query)


    def getAllParticipants(self):
        query = "SELECT p.*, u.first_name, u.last_name FROM participants p JOIN users u ON p.user_id = u.id"
        return self.db.query_db(query)

    def ongoing_m(self, sess_id):
        # print "SESSION ID", sess_id
        # get trip start and end location
        query1 = "SELECT t.start_location, t.end_location, t.id, u.first_name, u.last_name, t.trip_miles FROM trips t LEFT JOIN participants p ON t.id = p.trip_id \
        LEFT JOIN users u ON u.id = p.user_id WHERE u.id = :sess_id ORDER BY t.id DESC LIMIT 1;"
        data1 = {'sess_id': sess_id}

        trip_1 = self.db.query_db(query1, data1)

        # get list of participants
        query2 = "SELECT * FROM users LEFT JOIN participants \
        ON users.id=participants.user_id \
        LEFT JOIN trips on participants.trip_id=trips.id \
        WHERE trips.id=:spec_trip_id"
        data2 = {'spec_trip_id': trip_1[0]['id']}

        participants = self.db.query_db(query2, data2)

        arrData = []
        arrData.append(trip_1)
        arrData.append(participants)

        return arrData

    def getAllUsers(self):
        query = "SELECT * FROM users"
        return self.db.query_db(query)

    def up_photo_m(self, up_photo):
        add_query = "INSERT INTO photos_vids (photo, trip_id, user_id, created_at, updated_at) \
        VALUES (:spec_photo, :spec_trip_id, :spec_user_id, NOW(), NOW())"
        add_data = {
        'spec_photo': up_photo,
        'spec_trip_id': 1,
        'spec_user_id': 1
        }
        self.db.query_db(add_query, add_data)
        return

    def up_video_m(self, up_video):
            add_query = "INSERT INTO photos_vids (videos, trip_id, user_id, created_at, updated_at) \
            VALUES (:spec_photo, :spec_trip_id, :spec_user_id, NOW(), NOW())"
            add_data = {
            'spec_photo': up_video,
            'spec_trip_id': 1,
            'spec_user_id': 1
            }
            self.db.query_db(add_query, add_data)
            return

    def add_trip_m(self, trip_details, trip_api_info):

        miles = trip_api_info['rows'][0]['elements'][0]['distance']['text']
        milesStr = miles.replace(' mi','')
        milesInt = re.sub(r'\.\d+$','',milesStr)
        # create trip
        ins_trip_query = "INSERT INTO trips (name, start_date, end_date, start_location, \
        end_location, trip_miles) \
        VALUES (:spec_name, :spec_start_date, :spec_end_date, :spec_start_location, \
        :spec_end_location, :spec_trip_miles)"
        ins_trip_data = {
        'spec_name': trip_details['trip_name'],
        'spec_start_date': trip_details['start_date'],
        'spec_end_date': trip_details['end_date'],
        'spec_start_location': trip_details['start_loc'],
        'spec_end_location': trip_details['end_loc'],
        'spec_trip_miles': milesInt
        }

        # newly created trip
        tripid = self.db.query_db(ins_trip_query, ins_trip_data)

        # automatically add to favorites
        ins_trip_query2 = "INSERT INTO favorites (user_id, trip_id, \
        created_at, updated_at) \
        VALUES (:spec_user_id, :spec_trip_id, NOW(),NOW())"
        ins_trip_data2 = {
        'spec_user_id': 1,
        'spec_trip_id': tripid
        }

        self.db.query_db(ins_trip_query2, ins_trip_data2)

        # add participants of new trip
        pStr = trip_details['participant']
        pArr = pStr.split(',')

        add_participant_query = "INSERT INTO participants (user_id, trip_id, created_at, updated_at) VALUES (:user_id, :trip_id, NOW(), NOW())"

        for pId in pArr:
            add_participant_data = {'user_id': pId, 'trip_id': tripid }
            self.db.query_db(add_participant_query,add_participant_data)


        return

        def complete_trip_m(self, trip_details, trip_api_info):
            pass
