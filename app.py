from flask import Flask, render_template, request, send_file, url_for
import os
from utils.processing import process_file
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = "/tmp/uploads"
PROCESSED_FOLDER = "/tmp/processed"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["file"]

        if file:
            filename = secure_filename(file.filename)

            upload_path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(upload_path)

            df, summary = process_file(upload_path)

            processed_filename = "cleaned_" + filename
            processed_path = os.path.join(PROCESSED_FOLDER, processed_filename)

            df.to_csv(processed_path, index=False)

            return render_template(
                "dashboard.html",
                summary=summary,
                filename=processed_filename
            )

    return render_template("index.html")


# ✅ DOWNLOAD ROUTE (IMPORTANT)
@app.route("/download/<filename>")
def download_file(filename):
    file_path = os.path.join(PROCESSED_FOLDER, filename)

    # Debug print (check terminal)
    print("Downloading:", file_path)

    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    else:
        return "File not found", 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)