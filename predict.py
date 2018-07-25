import sys
sys.path.append('.')

import argparse
import dlib
import env
import numpy as np
import os

from common.files import is_file, get_file_extension
from lipnext.helpers.video import get_video_data_from_file, reshape_and_normalize_video_data
from lipnext.model.v2 import create_model, compile_model
from preprocessing.extractor.extract_roi import extract_video_data


# set PYTHONPATH=%PYTHONPATH%;./
# python predict.py -w data\results\2018-07-24-16-15-18\weights0029.hdf5 -v D:\GRID\s1\bbaf2n.mpg
def predict(weights_file_path: str, video_file_path: str, predictor_path: str, frame_count: int, image_width: int, image_height: int, image_channels: int, max_string: int):
	print("\nPREDICTION\n")

	print('Predicting for video at: {}'.format(video_file_path))
	print('Using predictor at:      {}'.format(predictor_path))

	video_file_extension = get_file_extension(video_file_path)
	video_data = None

	if video_file_extension == '.npy':
		video_data = get_video_data_from_file(video_file_path)
	else:
		detector  = dlib.get_frontal_face_detector()
		predictor = dlib.shape_predictor(predictor_path)

		video_data = extract_video_data(video_file_path, detector, predictor)
		video_data = reshape_and_normalize_video_data(video_data)

	model = create_model(frame_count, image_channels, image_height, image_width, max_string)
	compile_model(model)
	model.load_weights(weights_file_path)

	x_data = np.array([video_data])
	y_pred = model.predict(x_data)

	print(y_pred.shape)
	print(y_pred)


def main():
	print(r'''
   __         __     ______   __   __     ______     __  __     ______  
  /\ \       /\ \   /\  == \ /\ "-.\ \   /\  ___\   /\_\_\_\   /\__  _\ 
  \ \ \____  \ \ \  \ \  _-/ \ \ \-.  \  \ \  __\   \/_/\_\/_  \/_/\ \/ 
   \ \_____\  \ \_\  \ \_\    \ \_\\"\_\  \ \_____\   /\_\/\_\    \ \_\ 
    \/_____/   \/_/   \/_/     \/_/ \/_/   \/_____/   \/_/\/_/     \/_/ 
	''')

	ap = argparse.ArgumentParser()

	ap.add_argument('-v', '--video-path', required=True,
		help='Path to video file to analize')

	ap.add_argument('-w', '--weights-path', required=True,
		help='Path to .hdf5 trained weights file')

	DEFAULT_PREDICTOR = os.path.join(__file__, '..', 'data', 'predictors', 'shape_predictor_68_face_landmarks.dat')

	ap.add_argument("-pp", "--predictor-path", required=False,
		help="(Optional) Path to the predictor .dat file", default=DEFAULT_PREDICTOR)

	args = vars(ap.parse_args())

	weights        = os.path.realpath(args['weights_path'])
	video          = os.path.realpath(args['video_path'])
	predictor_path = os.path.realpath(args["predictor_path"])

	if not is_file(weights) or get_file_extension(weights) != '.hdf5':
		print('Invalid path to trained weights file')
		return

	if not is_file(video):
		print('Invalid path to video file')
		return
	
	predict(weights, video, predictor_path, env.FRAME_COUNT, env.IMAGE_WIDTH, env.IMAGE_HEIGHT, env.IMAGE_CHANNELS, env.MAX_STRING)


if __name__ == '__main__':
	main()
