import nibabel as nib
import numpy as np
from pathlib import Path

def load_mri_image(file_path):
    img = nib.load(file_path)
    data = img.get_fdata()
    return img, data

def normalize_image(data):
    norm_data = (data - np.min(data)) / (np.max(data) - np.min(data))
    return norm_data

def save_processed_image(img, new_data, output_path):
    new_img = nib.Nifti1Image(new_data, affine=img.affine)
    nib.save(new_img, output_path)
    print(f"Processed image saved at {output_path}")

if __name__ == "__main__":
    input_dir = Path("data")
    output_dir = Path("processed")
    output_dir.mkdir(exist_ok=True)

    for file_path in input_dir.glob("*.nii"):
        img, data = load_mri_image(file_path)
        norm_data = normalize_image(data)
        output_file = output_dir / file_path.name
        save_processed_image(img, norm_data, output_file)
