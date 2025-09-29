from detect_object import DetectObject
import matplotlib.pyplot as plt


MODEL_PATH = "/home/maderya/skill_test_m2m/models3/checkpoint/best_model.keras"
WINDOW_NAME = 'Car Control Simulation'

classifier = DetectObject(MODEL_PATH, WINDOW_NAME)
image = classifier.get_screenshot(top_cut=250)
prediction_result = classifier.detect_object(image)

print(prediction_result)

# plt.imshow(prediction_result)
# plt.title('images')
# plt.axis('off')
# plt.show()
# print(prediction_result)
