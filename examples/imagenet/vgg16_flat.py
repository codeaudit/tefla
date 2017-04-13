from __future__ import division, print_function, absolute_import

from tefla.core.layer_arg_ops import common_layer_args, make_args, end_points
from tefla.core.layers import dropout, relu
from tefla.core.layers import input, conv2d, fully_connected, max_pool, softmax

# sizes - (width, height)
image_size = (256, 256)
crop_size = (224, 224)


def model(is_training, reuse):
    common_args = common_layer_args(is_training, reuse)
    conv_args = make_args(activation=relu, **common_args)
    pool_args = make_args(filter_size=(2, 2), **common_args)
    fc_args = make_args(activation=relu, **common_args)
    logit_args = make_args(activation=None, **common_args)

    x = input((None, crop_size[1], crop_size[0], 3), **common_args)

    x = conv2d(x, 64, name='conv1_1', **conv_args)
    x = conv2d(x, 64, name='conv1_2', **conv_args)
    x = max_pool(x, name='maxpool1', **pool_args)

    x = conv2d(x, 128, name='conv2_1', **conv_args)
    x = conv2d(x, 128, name='conv2_2', **conv_args)
    x = max_pool(x, name='maxpool2', **pool_args)

    x = conv2d(x, 256, name='conv3_1', **conv_args)
    x = conv2d(x, 256, name='conv3_2', **conv_args)
    x = conv2d(x, 256, name='conv3_3', **conv_args)
    x = max_pool(x, name='maxpool3', **pool_args)

    x = conv2d(x, 512, name='conv4_1', **conv_args)
    x = conv2d(x, 512, name='conv4_2', **conv_args)
    x = conv2d(x, 512, name='conv4_3', **conv_args)
    x = max_pool(x, name='maxpool4', **pool_args)

    x = conv2d(x, 512, name='conv5_1', **conv_args)
    x = conv2d(x, 512, name='conv5_2', **conv_args)
    x = conv2d(x, 512, name='conv5_3', **conv_args)
    x = max_pool(x, name='maxpool5', **pool_args)

    x = fully_connected(x, n_output=4096, name='fc6', **fc_args)
    x = dropout(x, drop_p=0.5, name='dropout1', **common_args)

    x = fully_connected(x, n_output=4096, name='fc7', **fc_args)
    x = dropout(x, drop_p=0.5, name='dropout2', **common_args)

    logits = fully_connected(x, n_output=1000, name="logits", **logit_args)
    predictions = softmax(logits, name='predictions', **common_args)

    return end_points(is_training)


# model_for_loading = model(False, None)
# from tefla.utils import util
#
# util.show_vars()
