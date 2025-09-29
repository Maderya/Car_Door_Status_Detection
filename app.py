from flask import Flask, render_template, jsonify, request
from detect_object import DetectObject
import time

app = Flask(__name__, template_folder='webpage')

# Init Data
status = {
    "front_right": "Closed",
    "front_left": "Closed",
    "rear_right": "Closed",
    "rear_left": "Closed",
    "hood": "Closed"
}

# Route for the main page


@app.route('/')
def index():
    return render_template('index.html', status=status)


@app.route('/update', methods=['POST'])
def update_status():
    MODEL_PATH = "/home/maderya/skill_test_m2m/models3/checkpoint/best_model.keras"
    WINDOW_NAME = 'Car Control Simulation'
    
    start_time = time.time()
    classifier = DetectObject(MODEL_PATH, WINDOW_NAME)
    image = classifier.get_screenshot(250)
    prediction_result = classifier.detect_object(image)
    print("--- %s seconds ---" % (time.time() - start_time))
    
    # Simulate a function that returns a new status
    new_status = {
        "front_right": prediction_result[0],
        "front_left": prediction_result[1],
        "rear_right": prediction_result[2],
        "rear_left": prediction_result[3],
        "hood": prediction_result[4]
    }

    return jsonify(new_status)


if __name__ == '__main__':
    app.run(debug=True)
