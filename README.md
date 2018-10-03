# lipnext

> A Keras (Tensorflow) implementation of LipNet lipreading

One to two paragraph statement about your product and what it does.

## Setup

### Prerequisites

...

### Installation

OS X & Linux:

```
...
```

Windows:

```
...
```

## Usage

...

### Preprocessing

...

### Training

Use the `train.py` script to start training a model after preprocesing your dataset. You'll also need to provide a directory containing individual align files with the expected sentence:

```
usage: python train.py [-h] -d DATASET_PATH -a ALIGNS_PATH [-e EPOCHS] [-ic]

optional arguments:
  -h, --help            show this help message and exit
  -d DATASET_PATH, --dataset-path DATASET_PATH
                        Path to the dataset root directory
  -a ALIGNS_PATH, --aligns-path ALIGNS_PATH
                        Path to the directory containing all align files
  -e EPOCHS, --epochs EPOCHS
                        (Optional) Number of epochs to run
  -ic, --ignore-cache   (Optional) Force the generator to ignore the cache
                        file
```

i.e:

```
python train.py -d data/dataset -a data/aligns -e 70
```

The training is configured to use multiprocessing with 2 workers by default.

### Evaluating

Use the `predict.py` script to analyze a video or a directory of videos with a trained model:

```
usage: python predict.py [-h] -v VIDEO_PATH -w WEIGHTS_PATH [-pp PREDICTOR_PATH]

optional arguments:
  -h, --help            show this help message and exit
  -v VIDEO_PATH, --video-path VIDEO_PATH
                        Path to video file or batch directory to analize
  -w WEIGHTS_PATH, --weights-path WEIGHTS_PATH
                        Path to .hdf5 trained weights file
  -pp PREDICTOR_PATH, --predictor-path PREDICTOR_PATH
                        (Optional) Path to the predictor .dat file
```

i.e:

```
python predict.py -w data/res/2018-09-26-02-30/lipnext_065_1.96.hdf5 -v data/dataset_eval
```

## To-do List

- [x] RGB standardization: Apply per-batch zero mean standardization
- [x] Augmentation: Make generators also output the horizontal flip of each video
- [x] Statistics: Record per-epoch statistics and other useful data visualizations.
- [ ] Documentation: Proper usage and code documentation
- [ ] Testing: Develop unit testing

## Built With

* [Python](https://www.python.org/) - The programming language
* [Keras](https://keras.io/) - The high-level neural network API

## Author

* **Omar Salinas** - [omarsalinas16](https://github.com/omarsalinas16)

See also the list of [contributors](https://github.com/omarsalinas16/lipnext/contributors) who participated in this project.

## License

This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details
