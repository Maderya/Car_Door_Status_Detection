
    
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