Scale and Position the Filter Image
====================================

In this activity, you will learn to scale the filter and position it properly on face.

<img src= "https://s3-whjr-curriculum-uploads.whjr.online/fd53ad2b-9538-4b04-ac7e-ab2eeeb5449f.gif" width = "480" height = "320">


Follow the given steps to complete this activity:

1. Scale and position the filter.

* Open the main.py file.

* Create  variables `scale`, `dx` and `dy` to store the scaling factor and differential locations.

    `scale = 0`

    `dx = 0`

    `dy = 0`

* Define the `scale`, `dx`, `dy` values for filter image inside the if condition.

    `if(menuChoice == 0):`

    `scale = 90`

    `dx = 5`

    `dy = 40`

* Calculate the `xLoc` and `yLoc` based on `resizeFactor` and `dx, dy`.

    ` xLoc = int(xLoc - (resizefactor * dx))`

    `yLoc = int(yLoc - (resizefactor * dy))`

* Save and run the code to check the output.






