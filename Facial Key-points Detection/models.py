# The convolutional neural network architecture

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.nn.init as I


class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()

        self.conv1 = nn.Conv2d(1, 32, 3)
        self.pool = nn.MaxPool2d(2,2)
        self.conv2 = nn.Conv2d(32, 64, 3)
        self.conv3 = nn.Conv2d(64, 128, 3)
        self.conv4 = nn.Conv2d(128, 256 ,3)
        self.conv5 = nn.Conv2d(256, 512 ,1)
        self.conv6 = nn.Conv2d(512, 1024, 1)
        

        self.fc1 = nn.Linear(9216, 1024)
        self.fc1_drop = nn.Dropout(p=0.4)
        self.fc2 = nn.Linear(1024 , 136)
        
        
    def forward(self, x):
        
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = self.pool(F.relu(self.conv3(x)))
        x = self.pool(F.relu(self.conv4(x)))
        x = self.pool(F.relu(self.conv5(x)))
        x = self.pool(F.relu(self.conv6(x)))

        x = x.view(x.shape[0], -1)

        x = F.relu(self.fc1(x))
        x = self.fc1_drop(x)
        x = self.fc2(x)

        return x
