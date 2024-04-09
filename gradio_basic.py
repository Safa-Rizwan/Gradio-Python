import gradio as gr
import random
# Sample 01
# # greet function
# def greet(name):
#     return 'Hello '+ name +'!'

# ui = gr.Interface(greet, 'text','text')
# ui.launch(share=True)

# Sample 02
# With Atrributes
# greet function
# def greet(name):
#     return 'Hello '+ name +'!'

# ui = gr.Interface(fn=greet, inputs=gr.components.Textbox(lines = 2,placeholder = 'Name here...'), outputs='text')
# ui.launch(share=True)

# Sample 03 
# greet function
# def greet(name):
#     return 'Hello '+ name +'!'

# with gr.Blocks() as demo:
#     name = gr.Textbox(label='Name:')
#     otpt = gr.Textbox(label='Output:')
#     greet_btn = gr.Button('Greet!')
#     greet_btn.click(fn = greet, inputs=name, outputs=otpt, api_name='greet')
# demo.launch()


# Sample 04
# greet function
# def greet(name, is_morning, temp):
#     msg = 'Good Morning!' if is_morning else 'Good Evening!'
#     greeting = f'{msg}, Hello {name}! Today temperature is {temp} degrees.'
#     cels = (temp - 32) * 5/9
#     return greeting, round(cels,2)
# ui = gr.Interface(fn=greet, inputs=['text', 'checkbox', gr.components.Slider(0,100)], outputs=['text', 'number'])
# ui.launch(share=True)

# Sample 05
# # Chatbot Interface
# def random_response(message,history):
#     return random.choice(['Yes', 'No'])
# demo = gr.ChatInterface(random_response)
# demo.launch()

# double tabs
title = 'Multiple interfaces'
# greet function
def greet(name):
    return 'Hello '+ name +'!'

def user_help(do):
    return 'Good, you are learning Gradio for ' + do

# interface 1
tab1 = gr.Interface(greet, 'text', 'text')

# interface 2
tab2 = gr.Interface(user_help, 'text', 'text')

demo = gr.TabbedInterface([tab1, tab2], ['app1', 'app2'])
demo.launch()
