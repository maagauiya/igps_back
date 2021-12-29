import bcrypt



app = Flask(__name__)
app.config['MONGO_URI']='mongodb://localhost:27017/sttechdb'
app.config['SECRET_KEY']='Th1s1ss3cr3t'


mongo = PyMongo(app)
bcrypt = Bcrypt(app)

# blocked
# user_name = "4346522"
# password = "blocked20210913"

user_name = "4338462"
password = "87757727433"

hash_pass = bcrypt.generate_password_hash(password).decode('utf-8')

mongo.db.new_users.update({"username":user_name},{"$set":{"password":hash_pass}})

