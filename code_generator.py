from flask import Flask, render_template, url_for, redirect, request
import openai
from dotenv import load_dotenv
import os
app = Flask(__name__)
posts = [ ]

def configure():
    load_dotenv()
# @app.route("/")
# def hello():
#     return render_template('home.html', posts=posts)


# @app.route("/about")
# def localhost():
#     return render_template("about.html", title = 'about')
@app.route("/")
def homepage():
    return render_template("homepage.html", title = 'home')
@app.route("/python", methods=['POST', 'GET'])
def python():
     if request.method=='POST':
            
        header=request.form['header']
        type_choice = request.form['dropdown']
        hero=request.form['hero']
        body=request.form['body']
        footer=request.form['footer']
        prompt = "Please Generate a basic code python only for GUI in " + type_choice + "follow the following instruction" + \
            '\n' + "in the header " + header + '\n' + "in the hero " + hero + '\n' + "in the body " + body + '\n'\
              + "in the footer " + footer
        generated_code = get_completion(prompt)
        

        return render_template('code_display.html', generated_code=generated_code, title = "python")
     else:
        return render_template('python_gen.html', title="python")


@app.route("/ruby", methods=['POST', 'GET'])
def ruby():
    if request.method=='POST':
            
        header=request.form['header']
        type_choice = request.form['dropdown']
        hero=request.form['hero']
        body=request.form['body']
        footer=request.form['footer']
        prompt = "Please Generate code only just generate an ruby GUI code only.in " + type_choice + " follow the following instruction" + \
            '\n' + "in the header " + header + '\n' + "in the hero " + hero + '\n' + "in the body " + body + '\n'\
              + "and in the footer " + footer
        generated_code = get_completion(prompt)
        

        return render_template('code_display.html', generated_code=generated_code, title= 'ruby')
    else:
        return render_template('ruby.html')
@app.route("/html", methods=['POST', 'GET'])
def html():
     if request.method=='POST':
            
        header=request.form['header']
        hero=request.form['hero']
        body=request.form['body']
        footer=request.form['footer']
        prompt = "Please Generate a basic template only just generate an HTML code only for my website's home page. follow the following instruction" + \
            '\n' + "in the header " + header + '\n' + "in the hero " + hero + '\n' + "in the body " + body + '\n'\
              + "and in the footer " + footer
        generated_code = get_completion(prompt)
        

        return render_template('code_display.html', generated_code=generated_code, title='html')
     else:
        return render_template('code_generator.html') 

@app.route("/help", methods=['POST', 'GET'])
def help():
    if request.method=='POST':
            
        type_choice = request.form['dropdown']
        prompt = "please give me a step by step brief help for" + type_choice + "and also how many separate code file is needed in order to run " + type_choice + "smoothly and how can i organize the files"
        generated_code = get_completion(prompt)
        

        return render_template('code_display.html', generated_code=generated_code, title = 'html')
    else:
        return render_template('help.html')

def get_completion(prompt, model="gpt-3.5-turbo"):
    openai.api_key = os.getenv('api_key')
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]


if __name__=="__main__":
    configure()
    app.run(debug=True)