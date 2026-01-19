 Oil Spill Detection Using SAR Satellite Imagery
 
   An End-to-End Deep Learning System for Environmental Monitoring


             --📌 Abstract--

Oil spills are among the most severe environmental disasters, causing long-term damage to marine ecosystems, coastal regions, and human livelihoods. Traditional monitoring methods are time-consuming and limited in coverage.

This project presents an AI-driven Oil Spill Detection and Severity Assessment System using Synthetic Aperture Radar (SAR) satellite imagery and a U-Net deep learning architecture. The system performs pixel-level segmentation to accurately identify oil spill regions, assesses spill severity, and provides an interactive web-based user interface for real-time analysis.


         --🧭 Table of Contents--

1.Introduction

2.Problem Statement

3.Why SAR Images?

4.Dataset Description

5.Project Workflow

6.Exploratory Data Analysis (EDA)

7.Data Preprocessing

8.Model Architecture – U-Net

9.Model Training

10.Evaluation Metrics

11.Error Analysis & Improvements

12.Post-Processing

13.Severity Assessment Logic

14.Web Application (UI)

15.Deployment

16.Results & Sample Outputs

17.Limitations

18.Future Enhancements

19.Conclusion



            ---1️⃣ Introduction---

Marine oil spills are difficult to monitor due to their dynamic nature and large spatial extent. Satellite imagery provides a scalable solution, and SAR images are especially effective as they operate independently of weather and lighting conditions.

This project builds a complete AI pipeline, from raw satellite data to a deployed web application, enabling users to upload SAR images and instantly receive oil spill detection results


          ---2️⃣ Problem Statement---

The goal of this project is to:

--->Detect oil spills from SAR satellite images

--->Segment oil and non-oil regions at pixel level

--->Quantify the severity of the spill

--->Provide an easy-to-use interface for non-technical users

--->Deploy the solution as a publicly accessible application



         ---3️⃣ Why SAR Images?---

Unlike optical images, SAR images:

-->Work day and night

-->Penetrate clouds and fog

-->Highlight oil spills as bright (white) regions

-->Are widely used in real-world maritime surveillance

Important:

In this project:

-->White pixels → Oil Spill

-->Black pixels → Water


           ---4️⃣ Dataset Description---

Image Type: Grayscale SAR images

Labels: Binary segmentation masks

Mask Encoding:

White (1) → Oil

Black (0) → Water




           ---5️⃣ Project Workflow---

<img width="416" height="727" alt="Screenshot 2026-01-13 173909" src="https://github.com/user-attachments/assets/f3f0621d-a033-4c58-a3b3-3c374be119ac" />





                 ---6️⃣ Exploratory Data Analysis (EDA)---


EDA was performed to understand:

Pixel intensity distribution

Image dimensions

Mask uniqueness

Oil vs water pixel ratio


Key observations:

SAR images are single-channel (grayscale)

Oil regions appear brighter

Class imbalance exists (water dominates)



<img width="930" height="674" alt="Screenshot 2026-01-10 143712" src="https://github.com/user-attachments/assets/b679b37b-3aa8-4fa7-9c10-28db9957a837" />




                       ---7️⃣ Data Preprocessing---


Steps applied:

Grayscale normalization (0–1)

Resizing to 256×256

Binary thresholding for masks


Optional data augmentation:

Horizontal flip

Vertical flip

Rotation



                      ---8️⃣ Model Architecture – U-Net---

The U-Net architecture is chosen due to its effectiveness in segmentation tasks.

Architecture Highlights:

-->Encoder (contracting path) extracts contextual features

-->Decoder (expanding path) restores spatial resolution

-->Skip connections preserve fine-grained details

-->Final sigmoid layer outputs pixel-wise probabilities


👉Tech Stack:

Python

PyTorch

OpenCV

NumPy

Streamlit

SAR Satellite Imagery

Git & GitHub


                               ----9️⃣ Model Training---

Loss Function:

Binary Cross-Entropy + Dice Loss

Optimizer: Adam

Learning Rate: 0.001

Epochs: 15+

Batch Size: 8

Training was checkpointed to allow resume after interruption.


<img width="587" height="352" alt="Screenshot 2026-01-13 170427" src="https://github.com/user-attachments/assets/25fa658e-041d-4e45-b383-82ef995014cf" />


                   
                         ---🔁 Training Concepts Explained---

Forward Pass: Image → Encoder → Decoder → Mask

Loss Calculation: Measures segmentation error

Backpropagation: Updates weights

Epoch: One full pass through dataset

Batch: Subset of images per iteration

Validation: Measures generalization


                         ---🔍 10️⃣ Evaluation Metrics---

Accuracy is misleading for segmentation, so we used:
Dice Coefficient
Intersection over Union (IoU)
Precision & Recall
Pixel-level Confusion Matrix
<img width="1450" height="805" alt="Screenshot 2026-01-13 171134" src="https://github.com/user-attachments/assets/cbeff4ba-86da-4425-ad58-de30c867de64" />


<img width="819" height="691" alt="Screenshot 2026-01-13 171407" src="https://github.com/user-attachments/assets/d6dd278e-6bb9-45c5-8ea4-114c2b8a410e" />








                    ----11️⃣ Error Analysis & Improvements---

Observed issues:

Boundary inaccuracies

Small false positives


Applied improvements:

Lowered threshold for SAR contrast

Morphological post-processing

Data augmentation

Longer training


<img width="1186" height="868" alt="Screenshot 2026-01-13 171506" src="https://github.com/user-attachments/assets/6521d750-fa8f-4efc-bce5-cdee94547c0b" />





                                 ----12️⃣ Post-Processing-----

To reduce noise:

Morphological opening

Morphological closing

This removes isolated false detections and smooths boundaries.
<img width="1264" height="824" alt="Screenshot 2026-01-13 171643" src="https://github.com/user-attachments/assets/1fcde4c5-b532-452d-8809-99d417ed476d" />






                             -----13️⃣ Severity Assessment Logic---

Severity is calculated based on oil pixel percentage:

       Oil  Coverage	                        Severity	                               Risk
            0%	                                 None	                             threat
          < 5%	                                 Low	                             Minimal impact
          5–20%	                              Medium	                           Moderate risk
          > 20%	                               High	                              Severe threat



                                 
                                  
                                  -----14️⃣ Web Application (UI)----

A Streamlit-based web application was developed with:

SAR image upload

Run Analysis button

Probability map

Binary mask

Overlay visualization

Severity analysis

PDF report download

<img width="1903" height="771" alt="Screenshot 2026-01-13 171900" src="https://github.com/user-attachments/assets/0f174bbb-4d98-4410-adaa-d32e7fa0c549" />





                            ----15️⃣ Deployment----

The application is deployed using Streamlit Community Cloud.

-->Public access

-->CPU-based inference

-->GitHub-linked deployment

🔗 Live Application Demo

You can access the fully deployed and interactive version of this project here:


https://oil-spilldetection-2k25.streamlit.app/


                            ---16️⃣ Results & Sample Outputs---


Input SAR image

<img width="908" height="569" alt="image" src="https://github.com/user-attachments/assets/bb2b6017-6380-4cce-aa10-66aebc05ec73" />




Probability map


<img width="480" height="497" alt="Screenshot 2026-01-13 172622" src="https://github.com/user-attachments/assets/15f8af75-2467-4a4d-9384-ebf11bd965b1" />



Binary mask

<img width="956" height="595" alt="Screenshot 2026-01-13 172720" src="https://github.com/user-attachments/assets/06b8ca9e-44d6-4198-938c-6119873a8674" />



Overlay image

<img width="417" height="500" alt="Screenshot 2026-01-13 172812" src="https://github.com/user-attachments/assets/a9be5572-f4f1-4507-81bf-31ee4d36b5c6" />




Severity output

<img width="542" height="482" alt="Screenshot 2026-01-13 172841" src="https://github.com/user-attachments/assets/e8c5419e-23c6-4405-942d-f3eb10cf3c12" />



Overall UI and output of the model with the downloaded report

<img width="1864" height="794" alt="Screenshot 2026-01-13 173139" src="https://github.com/user-attachments/assets/96c86c05-1bfb-4046-a4d4-511e4e8219df" />

<img width="1798" height="773" alt="Screenshot 2026-01-13 173230" src="https://github.com/user-attachments/assets/8a9d6a05-67aa-482b-90fd-8a096584ab84" />

<img width="562" height="830" alt="Screenshot 2026-01-13 173404" src="https://github.com/user-attachments/assets/2ab12396-3fb0-426b-aa11-99c445232406" />

<img width="621" height="801" alt="Screenshot 2026-01-13 173454" src="https://github.com/user-attachments/assets/ce5aaf80-9c6a-4406-9f73-7adb744ec658" />







                             ----17️⃣ Limitations----

Works only on SAR images

Not trained on optical imagery

Performance depends on SAR quality




                                 ----18️⃣ Future Enhancements---

Multi-class spill categorization

Temporal spill tracking

Location-based alerts

Integration with GIS systems

Mobile-friendly UI

Real-time satellite feed



                                      ----19️⃣ Conclusion----

This project demonstrates a complete AI solution, from raw satellite data to a deployed application, capable of detecting and assessing oil spills with high precision. It highlights the practical use of deep learning in environmental monitoring and disaster management.


👩‍💻 Author

Name: Poojitha

Role: AI / ML Developer

Project Type: Academic / Research / Internship Project




---📜 Acknowledgements---

Mentor guidance

Open SAR datasets


