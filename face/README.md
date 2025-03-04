Dependency:
	deepface(TensorFlow),
	
instruction:
create a file name data "./face/data/"
	store the image in /data/ file as
		Name_0.jpg
		Name_1.jpg
		NameX_0.jpg

can put multiple images of same person as same name and incremental no Name_1 2 3..... for bater accuracy.
there must me a image with index "_0" that will be the display image.

run the nuralModa.py to train the neural model
then detact.py to detect the face and register in info.json

the register process has 10s delay that can be adjusted from register.py as needed 
