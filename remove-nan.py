import nibabel as nib
import numpy as np

# Load the NIfTI file
file_path = "./prova/rawdata/sub-verse008/no_CT_sub-verse008_ct.nii.gz"
img = nib.load(file_path)

# Get the data array
data = img.get_fdata()

# Check if there are NaN values
has_nan = np.isnan(data).any()
has_inf = np.isinf(data).any()

if has_nan:
    print("The NIfTI file contains NaN values.")
else:
    print("The NIfTI file does not contain NaN values.")

if has_inf:
    print("The NIfTI file contains inf values.")
else:
    print("The NIfTI file does not contain inf values.")
