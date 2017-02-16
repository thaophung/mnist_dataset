#!/usr/bin/env sh
# Compute the mean image in lmdb dataset
OUTPUT=./data/mnist    #folder for the lmdb datasets and output for mean image
TOOLS=./build/tools

$TOOLS/compute_image_mean $OUTPUT/mnist_first_digit_train_lmdb $OUTPUT/mnist_first_digit_train_mean.binaryproto
$TOOLS/compute_image_mean $OUTPUT/mnist_first_digit_test_lmdb $OUTPUT/mnist_first_digit_test_mean.binaryproto

echo "DONE."
