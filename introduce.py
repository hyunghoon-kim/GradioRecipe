import gradio as gr 

def do_introduce(name, age): 
    return f'안녕하세요. 저는 {name}입니다. 저의 나이는 {age}살 입니다.'

with gr.Blocks() as demo: 
    with gr.Row(): 
        with gr.Column(): 
            name = gr.Text(label='이름')
            age = gr.Text(label='나이')
        with gr.Column(): 
            intro = gr.Button('시작!') 
    with gr.Row():
        output = gr.Text(label='소개 문구') 

    intro.click(
        fn=do_introduce,
        inputs=[name, age],
        outputs=output
    )

demo.launch()