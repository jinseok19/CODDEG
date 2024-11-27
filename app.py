from flask import Flask, render_template, request, redirect, url_for
import os
from erp_combination import erp_combination

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/step1')
def step1():
    return render_template('step1.html')

@app.route('/report')
def report():
    return render_template('report.html')

@app.route('/run_erp_combination', methods=['POST'])
def run_erp_combination_TOP():
    # Call the erp_combination function with appropriate arguments
    erp_combination(
        screen_width=1920,
        screen_height=1080,
        fs=256,
        channels=['EEG_Fp1', 'EEG_Fp2'],
        isi=1000,
        top_image_path='./images/backgrounds/B0.jpg',
        clothes_type='bottoms',
        image_folder='./images/bottoms',
        num_trials=1,
        num_images=30,
        event_save_path='./event',
        result_dir='./plot/bottoms/0',
        lowcut=1.0,
        highcut=30.0,
        tmin=-0.2,
        tmax=1.0,
        mode='all'
    )
    return redirect(url_for('step1'))

@app.route('/run_erp_combination_bt', methods=['POST'])
def run_erp_combination_BOTTOM():
    # Call the erp_combination function with appropriate arguments
    erp_combination(
        screen_width=1920,
        screen_height=1080,
        fs=256,
        channels=['EEG_Fp1', 'EEG_Fp2'],
        isi=1000,
        top_image_path='./images/backgrounds/B0.jpg',
        clothes_type='bottoms',
        image_folder='./images/tops',
        num_trials=1,
        num_images=30,
        event_save_path='./event',
        result_dir='./plot/tops/0',
        lowcut=1.0,
        highcut=30.0,
        tmin=-0.2,
        tmax=1.0,
        mode='all'
    )
    return redirect(url_for('step1'))
if __name__ == '__main__':
    app.run(debug=True)