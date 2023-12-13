Add Multiple Filters
========================

In this activity, you will learn to apply multiple filters at a time on the face.

<img src= "https://media.slid.es/uploads/1525749/images/10515188/AA2.gif" width = "480" height = "320">


Follow the given steps to complete this activity:

1. .

* Open the main.py file.

* Set the initial `scale` to `0`.

    `scale = 90`

* Create `dx, dy` variables to position each filter.

    `dx = 0`

    `dy = 0`

* Check if menuchoice is 0,1,2,3,4 and set the variables scale, dx, dy.

    `if(menuChoice == 0):`

        `scale = 90`

        `dx = 5`

        `dy = 40`

    `if(menuChoice == 1):`

        `scale = 85`

        `dx = 5`

        `dy = 80`

    `if(menuChoice == 2):`

        `scale = 55`

        `dx = 20`

        `dy = 60`

    `if(menuChoice == 3):`

        `scale = 70`

        `dx = 15`

        `dy = 30`

    `if(menuChoice == 4):`

        `scale = 80`

        `dx = 10`

        `dy = 30`

* Set the `resizefactor` to `dist/scale`.

    `resizefactor = dist/scale`

* Calculate the `xLoc` and `Yloc` based on `resizeFactor` and `dx,dy`.

    `xLoc = int(xLoc - (resizefactor*dx))`

    `yLoc = int(yLoc - (resizefactor * dy))`

* Save and run the code to check the output.






