import argparse
import torch
import util.misc as utils

def get_args_parser():
    parser = argparse.ArgumentParser('Lightning project from scratch', add_help=False)
    parser.add_argument('--device', default='cuda',
                        help='device to use for training / testing')
    return parser

def main(args):
    utils.init_distributed_mode(args)

if __name__ == '__main__':
    parser = argparse.ArgumentParser('Lightning project from scratch', parents=[get_args_parser()])
    args = parser.parse_args()
    main(args)
