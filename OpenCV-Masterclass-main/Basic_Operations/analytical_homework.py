import cv2
import numpy as np
# Load the image
img = cv2.imread("assignment-001-given.jpg")
# Define the region of interest (ROI) for the license plate
x, y, w, h = 260, 180, 780, 750  # Adjust these values for the ROI
# Draw a rectangle around the ROI with a thicker green border
border_thickness = 5  # Increase border thickness
cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), border_thickness)
# Define the label position and size
label_text = "RAH972U"
font_scale = 1.2
font_thickness = 3
font_face = cv2.FONT_HERSHEY_SIMPLEX
text_size = cv2.getTextSize(label_text, font_face, font_scale, font_thickness)[0]
# Calculate label position at the top-right corner of the rectangle
label_x = x + w - text_size[0]  # Align text width to rectangle's top-right
label_y = y - 10  # Slightly above the rectangle's top edge
label_width = text_size[0] + 20
label_height = text_size[1] + 10
# Create a black background with opacity for the label
overlay = img.copy()
cv2.rectangle(
    overlay,
    (label_x - 10, label_y - text_size[1] - 10),  # Top-left corner
    (label_x + label_width - 10, label_y + 10),  # Bottom-right corner
    (0, 0, 0),  # Black color
    -1,  # Filled rectangle
)
alpha = 0.5  # Opacity level for the black background
cv2.addWeighted(overlay, alpha, img, 1 - alpha, 0, img)
# Add the label text on top of the black background
cv2.putText(
    img,
    label_text,
    (label_x, label_y),
    font_face,
    font_scale,
    (0, 255, 0),  # Green font color
    font_thickness,
)
# Save and display the resulting image
output_path = "labeled_output.jpg"
cv2.imwrite(output_path, img)
print(f"Annotated image saved as '{output_path}'")
# Optionally display the image
cv2.imshow("Image with Rectangle and Label", img)
cv2.waitKey(0)
cv2.destroyAllWindows()