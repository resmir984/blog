#1).

#from blog.models import users,posts

# authenticate
# authentication(username,email)
#[ctrl+enter==>for two pages view in same page],
# [ctrl+backspace==>for word by word delete]
#
# def authenticate(username,email):
#     user_data=[user for user in users if user["username"]==username and user["email"]==email]
#
#     print(user_data)
#
# authenticate("django","django@gmail.com")
#
# def authenticate(username,email):
#     user_data=[user for user in users if user["username"]==username and user["email"]==email]
#
#     if user_data:
#         return user_data
#     else:
#         return None
#
# print(authenticate("django","django@gmail.com"))

# def authenticate(username,email):
#     user_data=[user for user in users if user["username"]==username and user["email"]==email]
#     return user_data
# user=authenticate("django","django@gmail.com")
# if user:
#     print("login successful")
# else:
#     print("invalid credentials")

#2).

#
# def authenticate(**kwargs):
#     username=kwargs.get("username")
#     email=kwargs.get("email")
#     user_data=[user for user in users if user ["username"]==username and user["email"]==email]
#     return user_data
#
# user=authenticate(username="django",email="django@gmail.com")
#
# if user:
#     print("login successful")
# else:
#     print("invalid credentials")

#3).
#
# from blog.models import users,posts
#
# def authenticate(**kwargs):  #kwargs={"username":"django","email":"django@gmail.com"}
#     username=kwargs["username"]
#     email=kwargs["email"]
#     user_data=[user for user in users if user["username"]==username and user["email"]==email]
#     return user_data
#
# user=authenticate(username="abcd",email="abcd@gmail.com")
#
# if user:
#     print("login success")
# else:
#     print("invalid credentials")



#4).
#
# from blog.models import users,posts
# def authenticate(**kwargs):  # kwargs={"username":"django","email":"django@gmail.com"}
#     username=kwargs.get("username")
#     email=kwargs.get("email")          #none
#     user_data=[user for user in users if user["username"]==username and user["email"]==email]
#     return user_data
#
#
# user=authenticate(username="django", email="django@gmail.com")
#
# if user:
#     print("login success")
# else:
#     print("invalid credentials")

#5).

# class SignInView:
#     def post(self,**kwargs):
#         print("values in",kwargs)
# sv=SignInView()
# sv.post(username="django",email="django@gmail.com")

#6.0).

# from blog.models import users,posts
# def authenticate(**kwargs):  # kwargs={"username":"django","email":"django@gmail.com"}
#     username=kwargs.get("username")
#     email=kwargs.get("email")          #none
#     user_data=[user for user in users if user["username"]==username and user["email"]==email]
#     return user_data


#6.1).

# class SignInView:
#
#     def post(self,*args,**kwargs):
#         username=kwargs.get("username")
#         email=kwargs.get("email")
#         user=authenticate(username=username,email=email)
#         if user:
#             print("success")
#         else:
#             print("invalid credentials")
#
# sign=SignInView()
#
# sign.post(username="django1",email="django@gmail.com")

#7.0)

# from blog.models import users,posts
# def authenticate(**kwargs):  # kwargs={"username":"django","email":"django@gmail.com"}
#     username=kwargs.get("username")
#     email=kwargs.get("email")          #none
#     user_data=[user for user in users if user["username"]==username and user["email"]==email]
#     return user_data
#
#
# session={}             #"user:"django"
#
#
# class SignInView:
#
#     def post(self,*args,**kwargs):
#         username=kwargs.get("username")
#         email=kwargs.get("email")
#         user=authenticate(username=username,email=email)
#         if user:
#             print("success")
#             session["user"]=username
#         else:
#             print("invalid credentials")
#
# sign=SignInView()
#
# sign.post(username="django1",email="django@gmail.com")
# print(session)

#8.0).

#
# from blog.models import users,posts
# def authenticate(**kwargs):  # kwargs={"username":"django","email":"django@gmail.com"}
#     username=kwargs.get("username")
#     email=kwargs.get("email")          #none
#     user_data=[user for user in users if user["username"]==username and user["email"]==email]
#     return user_data
#
#
# session={}             #"user:"django"
#
#
# class SignInView:
#
#     def post(self,*args,**kwargs):
#         username=kwargs.get("username")
#         email=kwargs.get("email")
#         user=authenticate(username=username,email=email)
#         if user:
#             print("success")
#             session["user"]=username
#         else:
#             print("invalid credentials")
#
# def logout():
#     if "user" in session:
#         session.pop("user")
#         print("user logged out")
#     else:
#         print("u must login")
#
# sign=SignInView()
#
# sign.post(username="django",email="django@gmail.com")
# print(session)
# logout()
# print(session)


#
# print(dir(dict))   #methods in objects
# print(dir(list))   #methods in list
# print("remove" in dir(dict))  #remove is present or not in dict
# print("pop" in dir(dict))


#9.0).
#
#
# from blog.models import users,posts
# def authenticate(**kwargs):  # kwargs={"username":"django","email":"django@gmail.com"}
#     username=kwargs.get("username")
#     email=kwargs.get("email")          #none
#     user_data=[user for user in users if user["username"]==username and user["email"]==email]
#     return user_data
#
#
# session={}             #"user:"django"
#
#
# class SignInView:
#
#     def post(self,*args,**kwargs):
#         username=kwargs.get("username")
#         email=kwargs.get("email")
#         user=authenticate(username=username,email=email)
#         if user:
#             print("success")
#             session["user"]=username
#         else:
#             print("invalid credentials")
#
# def logout():
#     if "user" in session:
#         session.pop("user")
#         print("user logged out")
#     else:
#         print("u must login")
#
# class PostListView:
#
#     def get(self,*args,**kwargs):
#         return posts
#
# sign=SignInView()
#
# sign.post(username="django",email="django@gmail.com")
# print(session)
#
# pl=PostListView()                                      # for all posts viewing
# all_posts=pl.get()
# for p in all_posts:
#     print(p)


#10)

#
#
# from blog.models import users,posts
#
#
#
#
# def authenticate(**kwargs):  # kwargs={"username":"django","email":"django@gmail.com"}
#     username=kwargs.get("username")
#     email=kwargs.get("email")          #none
#     user_data=[user for user in users if user["username"]==username and user["email"]==email]
#     return user_data
#
#
# session={}             #"user:"django"
#
# def login_required(fn):
#     def wrapper(*args,**kwargs):
#         if "user" in session:
#             return fn(*args,**kwargs)
#         else:
#             raise Exception("u must login")
#     return wrapper
#
# class SignInView:
#
#     def post(self,*args,**kwargs):
#         username=kwargs.get("username")
#         email=kwargs.get("email")
#         user=authenticate(username=username,email=email)
#         if user:
#             print("success")
#             session["user"]=username
#         else:
#             print("invalid credentials")
#
# @login_required
# def logout(*args,**kwargs):
#     session.pop("user")
#
# class PostListView:
#
#     @login_required
#     def get(self,*args,**kwargs):
#         return posts
#
# pl=PostListView()
# try:
#     all_post=pl.get()
# except Exception as e:
#     print(e)

#11)


#
# from blog.models import users,posts
#
#
#
#
# def authenticate(**kwargs):  # kwargs={"username":"django","email":"django@gmail.com"}
#     username=kwargs.get("username")
#     email=kwargs.get("email")          #none
#     user_data=[user for user in users if user["username"]==username and user["email"]==email]
#     return user_data
#
#
# session={}             #"user:"django"
#
# def login_required(fn):
#     def wrapper(*args,**kwargs):
#         if "user" in session:
#             return fn(*args,**kwargs)
#         else:
#             raise Exception("u must login")
#     return wrapper
#
# class SignInView:
#
#     def post(self,*args,**kwargs):
#         username=kwargs.get("username")
#         email=kwargs.get("email")
#         user=authenticate(username=username,email=email)
#         if user:
#             print("success")
#             session["user"]=username
#         else:
#             print("invalid credentials")
#
# @login_required
# def logout(*args,**kwargs):
#     session.pop("user")
#
# class PostListView:
#
#     @login_required
#     def get(self,*args,**kwargs):
#         return posts
#
# #logined user's post only list
#
# class MyPostsView:
#     @login_required
#     def get(self,*args,**kwargs):
#         username=session.get("user")  #normalization==>for avoid data redundancy.data split based on data.relation is there
#         userId=[user["id"] for user in users if user["name"]==username][0]
#         print(userId)
#
# lg=SignInView()
# lg.post(username="django",email="django@gmail.com")
#
# post=MyPostsView()
# post.get()


#12)



# from blog.models import users,posts
#
#
#
# def authenticate(**kwargs):  # kwargs={"username":"django","email":"django@gmail.com"}
#     username=kwargs.get("username")
#     email=kwargs.get("email")          #none
#     user_data=[user for user in users if user["username"]==username and user["email"]==email]
#     return user_data
#
#
# session={}             #"user:"django"
#
# def login_required(fn):
#     def wrapper(*args,**kwargs):
#         if "user" in session:
#             return fn(*args,**kwargs)
#         else:
#             raise Exception("u must login")
#     return wrapper
#
# @login_required
# def logged_user():
#     username = session.get("user")
#     user_id = [user["id"] for user in users if user["name"] == username][0]
#     return  user_id
#
# class SignInView:
#
#     def post(self,*args,**kwargs):
#         username=kwargs.get("username")
#         email=kwargs.get("email")
#         user=authenticate(username=username,email=email)
#         if user:
#             print("success")
#             session["user"]=username
#         else:
#             print("invalid credentials")
#
# @login_required
# def logout(*args,**kwargs):
#     session.pop("user")
#
# class PostListView:
#
#     @login_required
#     def get(self,*args,**kwargs):
#         return posts
#
# #logined user's post only list
#
# class MyPostsView:
#     @login_required
#     def get(self,*args,**kwargs):
#         username=session.get("user")
#         user_id=[user["id"] for user in users if user["username"]==username][0]
#         qs=[post for post in posts if post["userId"]==user_id]
#         return qs
#
#
# user=SignInView()
# user.post(username="django",email="django@gmail.com")
#
# po=MyPostsView()
# print(po.get())
#
#
# class PostCreateView():
#     def post (self,*args,**kwargs):
#         userId=logged_user()
#         title=kwargs.get("title")
#         body=kwargs.get("body")
#         data={
#             "userId":userId,
#             "title":title,
#             "body":body
#         }
#         posts.append(data)
#         print("post created successfully")
#
# usr=SignInView()
# usr.post(username="django",email="django@gamil.com")
# pst=PostCreateView()
# pst.post(title="mypost",body="this is my new post")
#
#
#
# mp=MyPostsView()
# print(mp.get())
#


#13)



from blog.models import users,posts




def authenticate(**kwargs):  # kwargs={"username":"django","email":"django@gmail.com"}
    username=kwargs.get("username")
    email=kwargs.get("email")          #none
    user_data=[user for user in users if user["username"]==username and user["email"]==email]
    return user_data


session={}             #"user:"django"

def login_required(fn):
    def wrapper(*args,**kwargs):
        if "user" in session:
            return fn(*args,**kwargs)
        else:
            print("u must login")
    return wrapper

@login_required
def logged_user():
    username = session.get("user")
    user_id = [user["id"] for user in users if user["username"] == username][0]
    return  user_id

class SignInView:

    def post(self,*args,**kwargs):
        username=kwargs.get("username")
        email=kwargs.get("email")
        user=authenticate(username=username,email=email)
        if user:
            print("success")
            session["user"]=username
        else:
            print("invalid credentials")

@login_required
def logout(*args,**kwargs):
    session.pop("user")

class PostListView:

    @login_required
    def get(self,*args,**kwargs):
        return posts

#logined user's post only list

class MyPostsView:
    @login_required
    def get(self,*args,**kwargs):
        users_id=logged_user()
        qs=[post for post in posts if post("userId")==user_id]
        return qs


class PostCreateView():
    @login_required
    def post (self,*args,**kwargs):
        userId=logged_user()
        title=kwargs.get("title")
        body=kwargs.get("body")
        data={
            "userId":userId,
            "title":title,
            "body":body
        }
        posts.append(data)
        print("post created successfully")


class PostDetailsView():
    @login_required
    def get(self,*args,**kwargs):
        post_id=kwargs.get("post_id")
        qs=[p for p in posts if p.get("id")==post_id]
        return qs
    def put(self,id=None,*args,**kwargs):
        #print(id)
        post=[p for p in posts if p.get("id")==id][0]
        #print(post)
        title=kwargs.get("title")
        body=kwargs.get("body")
        post["title"]=title
        post["body"]=body
        print(post)


usr=SignInView()
usr.post(username="django",email="django@gamil.com")
pst=PostCreateView()
pst.post(title="mypost",body="this is my new post")

mp=MyPostsView()
print(mp.get())

detail=PostDetailsView()
#detail.put(id=5)
print(detail.get(post_id=10))
detail.put(id=10,title="my new post",body="this is my post")


#[print(detail.put(id=5))

###print(detail.get(post_id=5))


#user and card==h/w]

