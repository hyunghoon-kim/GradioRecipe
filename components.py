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

demo = gr.Interface(
    fn=classify_image,
    inputs=[
        gr.Image(
            type="pil", 
            label="이미지 업로드"
        ),  
        gr.Slider(
            minimum=1,
            maximum=10, 
            value=3,  
            step=1,
            label="상위 K개 결과"
        ),  
    ],
    outputs=gr.Label(label="분류 결과"), 
)

demo.launch()