Resize the Filter Image
========================

In this activity, you will learn to resize the filter image to fit on the face.

<img src= "https://s3-whjr-curriculum-uploads.whjr.online/ea3c4d39-fa3e-4043-af64-17d30ccf7589.gif" width = "480" height = "320">


Follow the given steps to complete this activity:

1. Resize the filter image.

* Open the main.py file.

* Calculate the width of the face by finding the distance between the landmark points `21, 251`.

    `dist = math.dist(face[21], face[251])`

* Find the resize factor by dividing `dist` by `scale` and store it in `resizefactor` variable.

    `resizefactor = dist/scale`

* Resize the filter image using cv2.resize() method.

    `filterImg = cv2.resize(menuImages[menuChoice], (0, 0), fx = resizefactor, fy = resizefactor)`

* Save and run the code to check the output.






