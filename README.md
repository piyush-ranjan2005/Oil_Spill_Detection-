# Dataset files for AI-Driven System for Oil Spill

This repository branch `Ritwik-Oil_Spill_Detection-` contains dataset archives tracked with Git LFS.

Files included
- `dataset.zip` — 1,055,456,121 bytes (~1.06 GB)
  - SHA256: `E6ED4EDCF2C4DF41DC9FD0DE13091E71B480BD44762A7BA48D393C3F0BB0A5EE`
- `preprocess.zip` — 1,232,595,370 bytes (~1.23 GB)
  - SHA256: `0E5C8741266199421BDC51C4F553D5D1654015744A7ADA9FD033EF8F9DD5F57A`

Notes
- These zip files are tracked using Git LFS. To fetch them when cloning the repo, run:

  ```powershell
  git lfs install
  git clone --branch Ritwik-Oil_Spill_Detection- https://github.com/springboardmentor112r-Agri/Oil_Spill_Detection-.git
  git lfs pull
  ```

- To verify checksums locally (PowerShell):

  ```powershell
  Get-FileHash -Path .\dataset.zip -Algorithm SHA256
  Get-FileHash -Path .\preprocess.zip -Algorithm SHA256
  ```

- If you prefer the raw dataset (unpacked) available in the repo, consider tracking the original `.npy` files with Git LFS instead. Note that GitHub LFS storage/bandwidth quotas may apply.

Contact / Usage
- If you move these files to external storage (S3/Drive), update this `README.md` with the public download link and preferred verification checksum.
