import imageio

filenames = ["BEAN.jpeg"]

images = []
for filename in filenames: images.append(imageio.imread(filename))

imageio.mimsave('RS.gif', images, 'GIF', duration = 2)