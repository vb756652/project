from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = 'YOUR_OPENAI_API_KEY'

# Define a route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Define a route to handle form submissions
@app.route('/generate', methods=['POST'])
def generate():
    prompt = request.form['prompt']
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=100
    )
    generated_text = response.choices[0].text.strip()
    return render_template('index.html', prompt=prompt, generated_text=generated_text)

if __name__ == '__main__':
    app.run(debug=True)
