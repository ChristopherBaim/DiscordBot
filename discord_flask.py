

# python discord_flask.py



from os.path import expanduser
home = expanduser("~")

# curl -d "heystuff" -X POST http://localhost:8111/submit_text

# TODO: Use smaller model
from transformers import GPT2LMHeadModel, GPT2Tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2", pad_token_id=tokenizer.eos_token_id) 



import torch
import numpy as np


from flask import Flask, render_template, url_for #, redirect
app = Flask(__name__)
app.config['SECRET_KEY'] = '123'

from flask_wtf import FlaskForm
from wtforms import TextAreaField
from wtforms.validators import DataRequired
# from flask import jsonify
from flask import request


class MyForm(FlaskForm):
    input_ = TextAreaField('INPUT', id ='contentcode') #, validators=[DataRequired()])




# @app.route('/', methods=('GET', 'POST'))
# @app.route('/home', methods=('GET', 'POST'))
# def home():
#     data = []
#     form = MyForm()
#     if request.method == 'GET':
#         return render_template('home.html', data=data, title='DV', form=form)
#     return render_template('home.html', data=data, title='DV', form=form)

# prompt1 = 'Eberron embraces swashbuckling action and pulp adventure while adding \
# a layer of noir intrigue. Daring heroes battle villains in high-stakes \
# instances of over-the-top action, dealing with narrow escapes and ominous \
# mysteries that threaten the world’s safety. But stories don’t always end \
# well, villains sometimes succeed, and there isn’t a perfect answer to every \
# problem. Magic is common, and weaved through everyday life. \
# \n Greybeard is a wise wizard that has a staff. I ask Greybeard'



# prompt1 = 'greybeard: Im an old wizard. I cast speels.\
# \nme: what is your staff made of? \
# \ngreybeard: its a wooden staff, lad \
# \nme: how old are you? \
# \ngreybeard: im as old as the trees, lad \
# \nme: where are we going? \
# \ngreybeard: to wonderland, lad \
# \nme:'
# prompt2 = "\ngreybeard:"





torn_fristo_1 = "User: Who are you? \
\nTorn Fristo: I...I don't remember\
\nUser: What are you doing here? \
\nTorn Fristo: Please...help me get out. I'm afraid \
\nUser: What is your name? \
\nTorn Fristo: I think...it was Turdy \
\nUser: How did you end up here?  \
\nTorn Fristo: I...remember a poopy hole \
\nUser: Where are we? \
\nTorn Fristo: In a Tarasque anus...I think \
\nUser: Will you help us? \
\nTorn Fristo: I'm scared...but I'll try \
\nUser: Are you okay? \
\nTorn Fristo: It smells...poopy in here \
\nUser: What was that? \
\nTorn Fristo: Poop worms...nasty creatures \
\nUser: Are you dead? \
\nTorn Fristo: I'm as dead as this poop...this poop \
\nUser: How can we help you? \
\nTorn Fristo: Free me...please...from this poopy prison \
\nUser:"
torn_firsto_2 = "\nTorn Fristo:"









@app.route('/submit_text', methods=('GET', 'POST'))
def submit_text():
    form = MyForm()
    # if request.method == 'GET':
    #     return render_template('home.html', title='DV')
    if request.method == 'POST':
        # print (request._cached_json[0])
        text = request._cached_json[0]['text']
        print (text)

        prompt = ''

        if text.startswith("To Torn:"):
            text = text.split('To Torn:')[1]
            prompt = torn_fristo_1 + text + torn_firsto_2

        elif text.startswith("To Karina:"):
            text = text.split('To Karina:')[1]
            prompt = karina_1 + text + karina_2

        elif text.startswith("To Kaspar:"):
            text = text.split('To Kaspar:')[1]
            prompt = kasper_1 + text + kasper_2

        # print (prompt)


        if len(prompt) > 0:

                # prompt = prompt1 + text + prompt2
            input_ids = tokenizer.encode(prompt) #, max_length=512)
            input_ids = np.array(input_ids)
            input_ids = np.reshape(input_ids, [1,-1])
            input_ids = torch.tensor(input_ids)

            # print (input_ids.shape)
            input_len = input_ids.shape[1]
            # print (len(input_ids))

            n_tokens_to_sample = 25

            # top_p set 0.75
            aa = model.generate(do_sample=True, top_p=.5, max_length=input_len+n_tokens_to_sample, input_ids=input_ids)
        
            aa = aa.numpy()
            aa = aa[0]
            # print ( tokenizer.decode(aa))
            # print ()
            aa = aa[input_len:]
            text = tokenizer.decode(aa)
            print ('output1:', text)

            if '\nUser:' in text:
                text = text.split('\nUser:')[0]

            if len(text.strip(' ') )== 0: 
                return {'hey': ''}, 200


            return {'hey': text}, 200

        else:
            return {'hey': ''}, 200








if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=8111)





