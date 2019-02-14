#!/usr/bin/env python3.5
import cv2
import matplotlib.pyplot as plt

def cam():
	cap = cv2.VideoCapture(1)

	while(True):
# Capture frame-by-frame
		ret, frame = cap.read()


# Display the resulting frame
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		canny = cv2.Canny(frame, 100, 200)

		# LIVE IMAGES
		cv2.imshow('gray',gray)
		cv2.imshow('canny', canny)
		cv2.imshow('frame', frame)

		# NICELY in matlab plot style but NOT LIVE!!
			# also watch the coler patterns -> MATPLOTLIB has BGR
#		plt.subplot(2,1,1)
#		plt.imshow(frame)
#		plt.title("my two subplots")
#		
#		plt.subplot(2,1,2)
#		plt.imshow(gray)
#		plt.show()

		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

# When everything done, release the capture
	cap.release()
	cv2.destroyAllWindows()


if __name__ == '__main__' :
	cam()
