from flask import *
import extractor
from os import listdir, remove
from os.path import isfile, getmtime
from pathlib import Path
from werkzeug.utils import secure_filename
import re
from random import randint
from typing import List
import time


PATH_TO_INPUT_FILES: str = "./input_files/"
PATH_TO_OUTPUT_FILES: str = "./output_files/"


def sanitize(filename: str) -> str:
    index = secure_filename(filename)
    index = Path(filename).stem
    index = re.sub(r"[^a-zA-Z0-9_]", "", index)
    if len(index) > 0:
        index = index[:10]
        index += "_"
    index += str(randint(1000, 10000))
    return index


def get_file_code(filename: str) -> str:
    return filename.split(".")[0][-4:]

def hours_to_seconds(hours: float) -> float:
    return hours * 60 * 60


def delete_old_files() -> None:
    file_codes_to_delete: List[str] = []
    current_time = time.time()
    for filename in listdir(PATH_TO_INPUT_FILES):
        if Path(filename).suffix != ".txt":
            filepath: str = PATH_TO_INPUT_FILES + filename
            file_mtime = getmtime(filepath)
            file_age = current_time - file_mtime
            if file_age > hours_to_seconds(2):
                file_codes_to_delete.append(get_file_code(filename))
                remove(filepath)
    for filename in listdir(PATH_TO_OUTPUT_FILES):
        filepath: str = PATH_TO_OUTPUT_FILES + filename
        if get_file_code(filename) in file_codes_to_delete:
            remove(filepath)


app = Flask(__name__)


@app.route("/")
def upload():
    return render_template("file_upload.html")


@app.route("/extract", methods=["POST"])
def extract():
    file = request.files["file"]
    if file is not None and file.filename is not None:
        delete_old_files()

        index = sanitize(file.filename)
        new_filename: str = index + ".ifc"
        file.save(PATH_TO_INPUT_FILES + new_filename)
        extractor.extract_bep_data_from_ifc_file(
            new_filename, PATH_TO_INPUT_FILES, PATH_TO_OUTPUT_FILES
        )
        return jsonify({"message": index})
    return ("Record not found", 400)


@app.route("/download/<index>", methods=["GET"])
def download(index):
    output_filename: str = index + ".xlsx"
    if isfile(PATH_TO_OUTPUT_FILES + output_filename):
        return send_file(PATH_TO_OUTPUT_FILES + output_filename, as_attachment=True)
    return ("Record not found", 400)


if __name__ == "__main__":
    app.run(debug=True)
