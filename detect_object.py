import tensorflow as tf
import numpy as np
import Xlib
import Xlib.display
from Xlib import X
import cv2
from PIL import Image


class DetectObject:
    def __init__(self, MODEL_PATH, WINDOW_NAME):
        # load model
        self.model = tf.keras.models.load_model(MODEL_PATH)
        self.window_name = WINDOW_NAME

    def get_screenshot(self, top_cut=0, width=None, height=None):
        try:
            display = Xlib.display.Display()
            root = display.screen().root
            windowIDs = root.get_full_property(
                display.intern_atom('_NET_CLIENT_LIST'), X.AnyPropertyType
            ).value

            for windowId in windowIDs:
                window = display.create_resource_object('window', windowId)
                window_title_property = window.get_full_property(
                    display.intern_atom('_NET_WM_NAME'), 0
                )
                if not window_title_property:
                    continue

                window_title = window_title_property.value.decode(
                    'utf-8', errors='ignore').strip()
                if self.window_name.lower() not in window_title.lower():
                    continue

                # Get window geometry directly
                geometry = window.get_geometry()
                window_width, window_height = geometry.width, geometry.height
                print(f"📊 Window size: {window_width}x{window_height}")

                # Set capture region
                y_start = top_cut
                capture_height = height or (window_height - top_cut)

                capture_width = width or window_width

                if capture_width > window_width:
                    print(
                        f"[ERROR] Capture width ({capture_width}) > window width ({window_width})")
                    return None

                if y_start + capture_height > window_height:
                    print(
                        f"[ERROR] Region too tall: y_start({y_start}) + height({capture_height}) > window_height({window_height})")
                    return None

                pixmap = window.get_image(
                    x=0,
                    y=y_start,
                    width=capture_width,
                    height=capture_height,
                    format=Xlib.X.ZPixmap,
                    plane_mask=0xFFFFFFFF
                )

                raw_data = pixmap.data
                final_image = np.frombuffer(raw_data, dtype=np.uint8).reshape(
                    (capture_height, capture_width, 4))
                rgb_image = final_image[:, :, :3]  # Remove alpha

                # Save Result
                # test = Image.fromarray(rgb_image, mode="RGB")
                # test.save("screenshot_cut_top.png")
                # print(
                #     f"Screenshot captured: {capture_width}x{capture_height} starting at (0, {y_start})")

                display.close()
                return rgb_image

        except Exception as e:
            print(f"[ERROR] Failed to capture screenshot: {e}")
            return None

    def detect_object(self, image_input):
        # Pre-process image
        adjusted_image = tf.image.adjust_hue(image=image_input, delta=-0.5)
        adjusted_image = tf.image.adjust_saturation(
            image=image_input, saturation_factor=0.1)

        image = np.expand_dims(adjusted_image, axis=0)
        processed_image = image.astype(np.float32) / 255.0
        resized_image = tf.image.resize(
            images=processed_image, size=(224, 224), preserve_aspect_ratio=False)

        # Make a prediction
        predictions = self.model.predict(resized_image)

        # Apply thresholding to get binary predictions
        SIGMOID_THRESHOLD = 0.5
        binary_predictions = (predictions > SIGMOID_THRESHOLD).astype(int)
        binary_label = []

        # convert b
        # return binary_labelinary '1' or '0' to 'open and 'close'
        for i in binary_predictions.reshape(-1):
            if i == 0:
                binary_label.append('Closed')
            else:
                binary_label.append('Open')
        return binary_label
