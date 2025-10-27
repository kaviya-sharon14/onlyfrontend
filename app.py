import subprocess
import sys

# ✅ Auto-install Flask if missing
try:
    from flask import Flask, request, jsonify, render_template
except ImportError:
    print("Flask not found! Installing Flask automatically...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "flask"])
    from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# In-memory task list (temporary store)
tasks = []
next_id = 1


@app.route('/')
def home():
    return render_template('index.html', title='To-Do List')


@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)


@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    for t in tasks:
        if t["id"] == task_id:
            return jsonify(t)
    return jsonify({"error": "Task not found"}), 404


@app.route('/tasks', methods=['POST'])
def create_task():
    global next_id
    data = request.get_json()
    title = data.get("title")
    if not title:
        return jsonify({"error": "Title is required"}), 400
    new_task = {"id": next_id, "title": title, "done": False}
    tasks.append(new_task)
    next_id += 1
    return jsonify(new_task), 201


@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    for t in tasks:
        if t["id"] == task_id:
            t["title"] = data.get("title", t["title"])
            t["done"] = data.get("done", t["done"])
            return jsonify(t)
    return jsonify({"error": "Task not found"}), 404


@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t["id"] != task_id]
    return jsonify({"message": "Task deleted"})


if __name__ == '__main__':
    print("Starting Flask To-Do App...")
    app.run(debug=True)   #

