import gradio as gr

def greet(name):
    return name + "님!, 반갑습니다. \nGradio의 세계로 오신것을 환영해요! :)"

demo = gr.Interface(
    fn=greet, 
    inputs="text", 
    outputs="text"
)
demo.launch(share=True) 