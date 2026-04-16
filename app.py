from flask import Flask, request, jsonify, render_template
import json
import os

app = Flask(__name__)

# Load notes
def load_notes():
    import os

def load_notes():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "notes.json")

    with open(file_path, "r") as f:
        return json.load(f)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_question = request.json.get("question")
    print("QUESTION:", user_question)

    notes = load_notes()

    # SIMPLE SEARCH (we'll improve later)
    relevant_texts = []
    for note in notes:
        if user_question.lower() in note["text"].lower():
            relevant_texts.append(note["text"])

    if not relevant_texts:
        relevant_texts.append("No exact match found. Try rephrasing.")

    # Combine context
    context = "\n".join(relevant_texts)

    # TEMP RESPONSE (AI comes later)
    response = f"Context found:\n{context}"

    return jsonify({"answer": response})


if __name__ == "__main__":
    app.run(debug=True)