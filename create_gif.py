import imageio.v3 as iio


filenames=["team-pic1.png", "team-pic2.png"]
images=[]

for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite("output1.gif", images, duration=500, loop=0)