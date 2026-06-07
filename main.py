# from flask import Flask,render_template,request
# import uuid
# from werkzeug.utils import secure_filename
# import os

# UPLOAD_FOLDER = 'user_uploads'
# ALLOWED_EXTENSIONS = { 'png', 'jpg', 'jpeg'}

# app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# # app=Flask(__name__)
# # app = Flask(__name__, template_folder='../templates')
# # xapp = Flask(__name__)
# @app.route("/")
# def home():
#     return render_template("index.html")

# @app.route("/create",methods=["GET","POST"])
# def create():
#     myid=uuid.uuid1()
#     if request.method=="POST":
#        print(request.files.keys())
#        rec_id=(request.form.get("uuid"))
#        desc=(request.form.get("text"))
#        for key , value in request.files.items():
#           print(key,value)
#           #upload file
#           file=request.files[key]
#           if file:
#                 filename = secure_filename(file.filename)
#                 if(not(os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], rec_id)))):
#                     os.mkdir(os.path.join(app.config['UPLOAD_FOLDER'], rec_id))
#                 file.save(os.path.join(app.config['UPLOAD_FOLDER'], rec_id,  filename))
#                 # input_files.append(file.filename)
#                 # print(file.filename)
#           with open(os.path.join(app.config['UPLOAD_FOLDER'], rec_id,  "desc.txt"),"w") as f: 
#               f.write(desc)
                  
          
#     return render_template("create.html",myid=myid)

# @app.route("/gallery")
# def gallery():
#     return render_template("gallery.html")
# if __name__=="__main__":
# app.run(debug=True)





# from flask import Flask, render_template, request
# import uuid
# from werkzeug.utils import secure_filename
# import os

# # Config
# UPLOAD_FOLDER = 'user_upload'
# ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# # Ensure upload folder exists
# os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# @app.route("/")
# def home():
#     return render_template("index.html")

# @app.route("/create", methods=["GET", "POST"])
# def create():
#     myid = uuid.uuid1()
#     if request.method == "POST":
#         rec_id = request.form.get("uuid")
#         desc = request.form.get("text")

#         # Create subfolder for this UUID if it doesn't exist
#         folder_path = os.path.join(app.config['UPLOAD_FOLDER'], rec_id)
#         os.makedirs(folder_path, exist_ok=True)

#         # Save uploaded files
#         for key, file in request.files.items():
#             if file and file.filename != '':
#                 filename = secure_filename(file.filename)
#                 file.save(os.path.join(folder_path, filename))
#                 print(f"Saved file: {filename}")

#     return render_template("create.html", myid=myid)

# @app.route("/gallery")
# def gallery():
#     return render_template("gallery.html")

# if __name__ == "__main__":
#     app.run(debug=True)
from flask import Flask, render_template, request
import uuid
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = 'user_uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
 

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/create", methods=["GET", "POST"])
def create():
    myid = uuid.uuid1()
    if request.method == "POST":
        print(request.files.keys())
        rec_id = request.form.get("uuid")
        desc = request.form.get("text")
        input_files = []
        for key, value in request.files.items():
            print(key, value)
            # Upload the file
            file = request.files[key]
            if file:
                filename = secure_filename(file.filename)
                if(not(os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], rec_id)))):
                    os.mkdir(os.path.join(app.config['UPLOAD_FOLDER'], rec_id))
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], rec_id,  filename))
                input_files.append(file.filename)
                print(file.filename)
            # Capture the description and save it to a file
            with open(os.path.join(app.config['UPLOAD_FOLDER'], rec_id, "desc.txt"), "w") as f:
                f.write(desc)
        for fl in input_files:
            with open(os.path.join(app.config['UPLOAD_FOLDER'], rec_id,  "input.txt"), "a") as f:
                f.write(f"file '{fl}'\nduration 1\n")


    return render_template("create.html", myid=myid)

@app.route("/gallery")
def gallery():
    reels = os.listdir("static/reels")
    print(reels)
    return render_template("gallery.html", reels=reels)

app.run(debug=True)
