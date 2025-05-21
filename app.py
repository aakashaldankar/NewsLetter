from crew import NewsletterGenCrew
import os
import gradio as gr
from datetime import datetime

def load_html_template(): 
    with open('config/newsletter_template.html', 'r') as file:
        html_template = file.read()
    return html_template

def generate_newsletter(topic: str, personal_message: str):
    yield "🛠️ Generating newsletter... please wait.", None

    inputs = {
        'topic': topic,
        'personal_message': personal_message,
        'html_template': load_html_template()
    }

    crew_instance = NewsletterGenCrew()
    crew = crew_instance.crew()
    crew.kickoff(inputs=inputs)

    newsletter_task = crew_instance.newsletter_task()
    output_html = newsletter_task.output.raw

    yield "✅ Newsletter ready!", output_html
    
with gr.Blocks() as demo:
    gr.Markdown("## ✨ AI-Powered Newsletter Generator")
    gr.Markdown("Enter your topic and personal message below, then click **Submit** to generate your newsletter.")

    with gr.Row():
        topic_input = gr.Textbox(label="📰 Newsletter Topic", placeholder="e.g., AI in Healthcare")
        message_input = gr.Textbox(label="✉️ Personal Message", placeholder="e.g., Here's a weekly digest...", lines=2)

    submit_btn = gr.Button("🚀 Submit")
    html_output = gr.HTML(label="🧾 Your Newsletter")
    status_box = gr.Textbox(label="🧠 Status", interactive=False)

    submit_btn.click(
        fn=generate_newsletter,
        inputs=[topic_input, message_input],
        outputs=[status_box, html_output]
    )

demo.launch()


 






