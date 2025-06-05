# Dummy MRI Data Preprocessing Project

This project demonstrates a basic neuroimaging data preprocessing pipeline using synthetic MRI data.  
It is designed as a portfolio project to showcase Python skills relevant to neuroimaging research without using any real patient data.

## Project Structure

- `generate_dummy_data.py`: Generates synthetic 3D MRI volumes saved as NIfTI files in the `data/` folder.
- `preprocess.py`: Loads the synthetic MRI data, normalizes the intensities, and saves the processed images in the `processed/` folder.
- `data/`: Folder containing synthetic MRI files.
- `processed/`: Folder where preprocessed images are saved.

## How to Run

1. Install dependencies:
    ```bash
    pip install nibabel numpy
    ```

2. Generate synthetic MRI data:
    ```bash
    python generate_dummy_data.py
    ```

3. Preprocess the synthetic data:
    ```bash
    python preprocess.py
    ```

## Notes

- All MRI data in this project are fully synthetic and generated randomly.
- This pipeline is a simplified demonstration and can be expanded with real preprocessing steps (e.g., smoothing, motion correction) for real neuroimaging workflows.

---

Feel free to explore and extend this pipeline!
