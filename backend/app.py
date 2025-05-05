from flask import Flask, request, send_file, jsonify
from PIL import Image
import io
from strategies.blur import BlurStrategy
from strategies.sharpen import SharpenStrategy
from strategies.edge_detection import EdgeDetectionStrategy
from strategies.strategy import ImageProcessingStrategy

app = Flask(__name__)

# Strategy Map
strategy_map = {
    "blur": BlurStrategy(),
    "sharpen": SharpenStrategy(),
    "edge": EdgeDetectionStrategy()
}

@app.route('/process', methods=['POST'])
def process_image():
    filter_type = request.form.get("filter")
    file = request.files.get("image")

    if not file or not filter_type:
        return jsonify({"error": "Missing image or filter type"}), 400

    if filter_type not in strategy_map:
        return jsonify({"error": "Invalid filter type"}), 400

    try:
        # Open image and apply strategy
        image = Image.open(file.stream).convert("RGB")
        strategy: ImageProcessingStrategy = strategy_map[filter_type]
        result_image = strategy.apply(image)

        # Save to byte stream
        img_io = io.BytesIO()
        result_image.save(img_io, format='PNG')
        img_io.seek(0)

        return send_file(
            img_io,
            mimetype='image/png',
            as_attachment=False,
            download_name='processed.png'
        )
    except Exception as e:
        print("Processing error:", e)
        return jsonify({"error": "Failed to process image"}), 500

@app.route('/ping', methods=['GET'])
def ping():
    return "Backend is live!"

if __name__ == '__main__':
    app.run(debug=True)
