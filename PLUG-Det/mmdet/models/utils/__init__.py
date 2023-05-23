# Copyright (c) OpenMMLab. All rights reserved.
from .brick_wrappers import AdaptiveAvgPool2d, adaptive_avg_pool2d
from .builder import build_linear_layer, build_transformer
from .ckpt_convert import pvt_convert
from .conv_upsample import ConvUpsample
from .csp_layer import CSPLayer
from .gaussian_target import gaussian_radius, gen_gaussian_target
from .inverted_residual import InvertedResidual
from .make_divisible import make_divisible
from .misc import interpolate_as, sigmoid_geometric_mean
from .normed_predictor import NormedConv2d, NormedLinear
from .panoptic_gt_processing import preprocess_panoptic_gt
from .positional_encoding import (LearnedPositionalEncoding,
                                  SinePositionalEncoding)
from .res_layer import ResLayer, SimplifiedBasicBlock
from .se_layer import DyReLU, SELayer
from .transformer import (DetrTransformerDecoder, DetrTransformerDecoderLayer,ClassDetrAttnLayer,
                          DynamicConv, PatchEmbed, Transformer, nchw_to_nlc,
                          nlc_to_nchw)
from .mmcv_transformer import (MultiheadAttention,MultiScaleDeformableAttention,BaseTransformerLayer)
from .class_transformer import (ClassDetrTransformerDecoderLayer,ClassDetrTransformerEncoder, ClassDetrTransformerDecoder, ClassTransformer, )
from .huicv.vis.visualize import  draw_a_bbox
from .huicv.plot_paper.plt_paper_config import set_plt
from .transformer import CLSTransformer
__all__ = [
    'ResLayer', 'gaussian_radius', 'gen_gaussian_target',
    'DetrTransformerDecoderLayer', 'DetrTransformerDecoder', 'Transformer','ClassDetrAttnLayer',
    'build_transformer', 'build_linear_layer', 'SinePositionalEncoding',
    'LearnedPositionalEncoding', 'DynamicConv', 'SimplifiedBasicBlock',
    'NormedLinear', 'NormedConv2d', 'make_divisible', 'InvertedResidual',
    'SELayer', 'interpolate_as', 'ConvUpsample', 'CSPLayer',
    'adaptive_avg_pool2d', 'AdaptiveAvgPool2d', 'PatchEmbed', 'nchw_to_nlc',
    'nlc_to_nchw', 'pvt_convert', 'sigmoid_geometric_mean',
    'preprocess_panoptic_gt', 'DyReLU','ClassDetrTransformerDecoderLayer','ClassDetrTransformerEncoder',
    'ClassDetrTransformerDecoder', 'ClassTransformer',
    'MultiheadAttention','MultiScaleDeformableAttention','BaseTransformerLayer',
    'get_hsv_colors', 'draw_a_bbox','set_plt','CLSTransformer'
]