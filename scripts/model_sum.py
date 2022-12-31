import torch
from torchsummary import summary
# from models.with_mb_quant import PoseEstimationWithMobileNet
from models.with_mobilenet import PoseEstimationWithMobileNet
from modules.load_state import load_state

net = PoseEstimationWithMobileNet()
# checkpoint = torch.load("../models/model_quant.pth", map_location='cpu')
checkpoint = torch.load("../models/checkpoint_iter_370000.pth", map_location='cpu')
load_state(net, checkpoint)
summary(net, input_size=(3, 256, 256), batch_size=-1)
