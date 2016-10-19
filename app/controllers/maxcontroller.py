from system.core.controller import *

class maxcontroller(Controller):
	def __init__(self, action):
		super(maxcontroller, self).__init__(action)
		self.load_model('WelcomeModel')
		self.db = self._app.db
		
	def get_fav(self):
		print "ace 1"
		return self.load_view('myindex.html')
	
	def index(self):
		return self.load_view('myindex.html')	
	
	def get_query(self):
		#query = "select users.first_name, trips.name, trips.start_date, trips.end_date, trips.trip_miles, trips.rating from users  right join favorites on users.id = favorites.user_id right join trips on favorites.trip_id = trips.id where users.first_name like 'norman';"
		query = "select trips.name, trips.start_date, trips.end_date, trips.rating, trips.trip_miles, participants.user_id from users right join favorites on users.id = favorites.user_id right join trips on favorites.trip_id = trips.id right join participants on participants.trip_id = trips.id where users.id = 1;"
		x = self.db.query_db(query)
		print x
		return self.load_view('myindex.html',miles = x)	
		
	def maps(self):
		return self.load_view('map.html')
		
	def detailed_trip_routing(self, name):
		return redirect('/detailed_trip')
		
	def detailed_trip(self,name):
		query="select trips.name, trips.start_date, trips.end_date, trips.rating, trips.trip_miles,trips.start_location,trips.end_location,users.picture from users right join favorites on users.id = favorites.user_id right join trips on favorites.trip_id = trips.id where users.id = 1 and name = :name;"
		data = {'name': name}
		#query = "select trips.name, trips.start_date, trips.end_date, trips.rating, trips.trip_miles from users right join favorites on users.id = favorites.user_id right join trips on favorites.trip_id = trips.id where users.id = 1;"
		y = self.db.query_db(query,data)
		return self.load_view('test.html',miles = y)
		
	def get_place(self): 
		city = request.form['user_input'].replace('  ', ' ')
		url = "https://maps.googleapis.com/maps/api/place/textsearch/json?query=" + city +"&key=AIzaSyB9HQHDiGKOMKe3gk18jmE-7soMZzy8a7M"
		response = requests.get(url).content
		x =  response
			
		return (response)