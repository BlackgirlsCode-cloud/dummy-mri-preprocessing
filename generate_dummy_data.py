import numpy as np
import nibabel as nib
from pathlib import Path

def generate_dummy_mri(file_path, shape=(64, 64, 64)):
    """
    Generate a synthetic MRI volume and save as a NIfTI file.
    """
    dummy_data = np.random.rand(*shape)
    dummy_img = nib.Nifti1Image(dummy_data, affine=np.eye(4))
    nib.save(dummy_img, file_path)
    print(f"Dummy MRI image saved at {file_path}")

if __name__ == "__main__":
    output_dir = Path("data")
    output_dir.mkdir(exist_ok=True)
    
    # Generate multiple dummy subjects
    for i in range(1, 4):
        file_name = output_dir / f"subject{i:02d}.nii"
        generate_dummy_mri(file_name)
