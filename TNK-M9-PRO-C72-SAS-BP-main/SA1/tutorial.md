Place Filter on Face
========================

In this activity, you will learn to drag the filters and place them on the face.

<img src= "https://s3-whjr-curriculum-uploads.whjr.online/e6fb661a-401b-43f5-a8ef-e79b218096db.gif" width = "480" height = "320">


Follow the given steps to complete this activity:

1. Place filter on the face.

* Open the main.py file.

* Import the `FaceMeshDetector` library.

    `from cvzone.FaceMeshModule import FaceMeshDetector`

* Detect 2 faces using `FeshMeshDetector()` function.

    `faceDetector = FaceMeshDetector(maxFaces=2)`

* Store the faces with the face mesh landmark.

    `cameraFeedImg, faces = faceDetector.findFaceMesh(cameraFeedImg, draw= False)`

* Use a for loop on `faces` and store the `x` and `y` coordinates for the landmark point where filter is to be placed.

    `for face in faces:`

        `xLoc= face[21][0]`

        `yLoc= face[21][1]`

* Overlay filter image on the face.

    `cameraFeedImg= cvzone.overlayPNG(cameraFeedImg, menuImages[menuChoice], [xLoc, yLoc])`
`
* Save and run the code to check the output.






