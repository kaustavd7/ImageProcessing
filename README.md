# ImageProcessing
Three Problem Statements

## 1) The lava: antaragni
Sincere students are usually defamed as emotionless or rocks by their over-exuberant friends, probably because they can’t see studious students’ antaragni yet. Who says the rocks can’t float? Let the rock-n-roll play, and you will see rocks rocking with spectacles in the air. The lava is hot molten rock erupted from a volcano and the magma is hot fluid material below or within Earth’s crust. An enormous amount of lava erupted, it flowed like a river.

Gradually top portion of the lava first gets cooled due to air contact, creating floating rocks in the river. These rocks need to be accounted for in estimating the overall lava flow. After volcanic eruption, estimation of accurate lava flow is essential for emergency response planning, public safety, property protection, land use planning, and environmental impact assessment. You can imagine, that there is no method other than capturing a variety of images (via drones) and processing them for this assessment task.

The final lava-detected region is shown as a white color mask with the non-lava region as black. My task is to generate only the final output mask image for the given input image.
   
## 2) Pro-night with or without camera flash?: pro light

You might have seen photographers carrying a variety of strobe lights (flash) during professional, cultural, or festival events occurring at night (pro-night). They produce a brief burst of light at a color temperature of about 5500 Kelvin to help illuminate a scene. Pro-nights are filled with glittery ornaments, flashy clothes, a truckload of makeup, and toasting glasses, where everything including people are showpieces. Flash causes specular reflections, unwanted glow, prolonged dark shadows, and other glittery artifacts. Moreover, it also changes the scene ambiance away from the night mood. Without a flash, the images will be dark with a noisy speckle effect and celebrities will look suntanned. Looks illuminating? Indeed for us, but for photographers, it’s a dilemma about, a night with or without a flash? 

When we faced a similar dilemma during denoising with or without preserving edges, the bilateral filter came to our rescue. You will extend a similar idea to design a cross bilateral filter for fusing flash and no-flash images to produce the final prolight image.

Write the Python program, which takes input from both flash and no-flash images of the same scene, fuses them appropriately, and produces a final good quality (prolight) image. The main criterion of evaluation is processing speed provided your program produces sufficient good quality pro light images with removing flashy artifacts. The higher the speed, the greater the score. If it can’t produce better quality than no-flash and flash, then the score will be 0.
