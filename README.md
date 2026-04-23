🧥 Invisible Cloak Effect
A Python + OpenCV project that simulates the Harry Potter-style invisible cloak effect in real time using your webcam. By replacing a specific colored cloth with the background, it creates the illusion that the wearer has turned invisible.

🎯 How It Works
The effect is achieved using a technique called color segmentation combined with background substitution. Here's the step-by-step breakdown:
1. Capture Background
When the program starts, it captures a few frames of the background without the person or cloak present. These frames are averaged to create a clean, stable background image that will be used for the substitution.
2. Detect the Cloak Color
Each subsequent frame from the webcam is converted from BGR to HSV (Hue, Saturation, Value) color space. HSV is preferred over RGB/BGR for color detection because it separates color information (hue) from lighting (value), making detection more robust under varying light conditions.
A predefined HSV color range is used to create a binary mask — white pixels where the cloak color is detected, black everywhere else.
3. Refine the Mask
The raw mask often contains noise and small imperfections. To clean it up:

Morphological operations (erosion and dilation) are applied to remove noise and fill holes in the detected region.

4. Apply the Cloak Effect
Using the refined mask:

The cloak region in the current frame is replaced with the corresponding pixels from the captured background.
The non-cloak region remains unchanged.
Both parts are combined using bitwise operations (cv2.bitwise_and, cv2.bitwise_or) to produce the final frame.

5. Display the Result
The final composited frame is displayed in real time, creating a seamless invisible cloak illusion.

🛠️ Tech Stack
ToolPurposePythonCore programming languageOpenCV (cv2)Video capture, image processing, maskingNumPyArray and matrix operations

📋 Requirements

Python 3.x
OpenCV
NumPy
A webcam
A solid-colored cloth (red/blue/green works best)

Install dependencies:
bashpip install opencv-python numpy

🚀 Usage

Clone the repository:

bash   git clone https://github.com/your-username/invisible-cloak.git
   cd invisible-cloak

Run the script:

bash   python invisible_cloak.py

Follow the on-screen instructions:

Stand away from the frame for the first few seconds so the background can be captured.
Put on / hold up your cloak and watch the magic! 🪄


Press q to quit the application.


🎨 Tips for Best Results

Use a bright, solid-colored cloth (red works great) in good lighting.
Make sure the background is static during background capture.
Avoid wearing clothes of the same color as the cloak.
Use in a well-lit environment for better color detection.

