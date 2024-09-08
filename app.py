from flask import Flask, request, jsonify
from PIL import Image
from flask_cors import CORS
import io

app = Flask(__name__)
CORS(app)

@app.route('/api/testing-instructions', methods=['POST'])
def generate_testing_instructions():
    context = request.form.get('context', '')
    screenshots = request.files.getlist('screenshots')

    if not screenshots:
        return jsonify({'error': 'No screenshots uploaded'}), 400

    # Simulate screenshot processing
    screenshot_images = []
    for screenshot in screenshots:
        image = Image.open(screenshot)
        image_byte_array = io.BytesIO()
        image.save(image_byte_array, format='PNG')
        image_base64 = image_byte_array.getvalue()  # Simulating image processing
        screenshot_images.append(image_base64)

    # Call the simulated function to generate testing instructions
    instructions = call_simulated_llm(context, len(screenshots))

    return jsonify({"instructions": instructions}), 200

def call_simulated_llm(context, screenshot_count):
    """
    Simulates a response from a multimodal LLM that generates testing instructions
    based on screenshots and optional context.
    """
    # Simulated test case response for demonstration
    return {
        "description": f"Test case generated based on {screenshot_count} screenshot(s). The test focuses on validating the core functionality shown in the images.",
        "pre_conditions": [
            "Ensure that the system is in a stable state.",
            "The user is logged into the application.",
            f"{context}" if context else "No additional context provided."
        ],
        "testing_steps": [
            "Step 1: Open the application and navigate to the screen shown in the first screenshot.",
            "Step 2: Perform the action shown, such as clicking a button or entering text.",
            "Step 3: Verify the response or output matches the expected behavior described.",
            "Step 4: Capture any discrepancies or issues observed during the testing."
        ],
        "expected_result": "The feature should function as intended, displaying correct responses and error-free interactions."
    }

if __name__ == '__main__':
    app.run(debug=True)
