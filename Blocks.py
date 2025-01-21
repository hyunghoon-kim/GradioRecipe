import gradio as gr
from transformers import pipeline

classifier = pipeline(
    "image-classification", 
    model="google/vit-base-patch16-224"
)

def classify_image(image, top_k=3):
    results = classifier(image)
    sorted_results = sorted(results, 
                            key=lambda x: x["score"], 
                            reverse=True)
    output_dict = {result["label"]: result["score"] 
                   for result in sorted_results[:top_k]}
    return output_dict

with gr.Blocks() as demo:
    with gr.Row(): 
        gr.HTML("<h1 style='text-align: center;'>ViT 기반 이미지 분류 데모</h1>")
    with gr.Row():
        with gr.Column():
            image = gr.Image(type="pil", label="이미지 업로드")
        with gr.Column():
            with gr.Row():
                top_k = gr.Slider(minimum=1, maximum=10, 
                                  value=3, step=1, label="상위 K개 결과")
            with gr.Row():
                classify = gr.Button('분류!') 
    with gr.Row():
        output = gr.Label(label="분류 결과")

    classify.click(
        fn=classify_image,
        inputs=[image, top_k],
        outputs=output
    )

demo.launch()