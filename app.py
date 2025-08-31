from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

# Load the AI model
generator = pipeline('text-generation', model='gpt2')

@app.route('/', methods=['GET', 'POST'])
def home():
    result_text = ""
    if request.method == 'POST':
        user_prompt = request.form['prompt']
        ai_result = generator(user_prompt, max_length=50, num_return_sequences=1)
        result_text = ai_result[0]['generated_text']
    
    return render_template('index.html', result=result_text)

if __name__ == '__main__':
    app.run(debug=True)