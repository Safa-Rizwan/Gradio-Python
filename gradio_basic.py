import gradio as gr

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
def greet(name):
    return 'Hello '+ name +'!'

with gr.Blocks() as demo:
    name = gr.Textbox(label='Name:')
    otpt = gr.Textbox(label='Output:')
    greet_btn = gr.Button('Greet!')
    greet_btn.click(fn = greet, inputs=name, outputs=otpt, api_name='greet')
demo.launch()
