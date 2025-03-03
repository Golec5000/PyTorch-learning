# 1. Desing model (input, output size, forward pass)
# 2. Construct loss and optimizer
# 3. Training loop
#     - forward pass: compute prediction
#     - backward pass: gradients
#     - update weights

import torch
import torch.nn as nn
from torch.optim import SGD

from chapter_11_model_rating.basic_model_creating import X_test

X = torch.tensor([
    [1],
    [2],
    [3],
    [4]

], dtype=torch.float32)

Y = torch.tensor([
    [2],
    [4],
    [6],
    [8]

], dtype=torch.float32)

n_snameples, n_features = X.shape

print(n_snameples, n_features)

input_size = n_features
output_size = n_features


class LinearRegression(nn.Module):
    def __init__(self, input_dim, output_dim):
        super(LinearRegression, self).__init__()
        # define layers
        self.lin = nn.Linear(input_dim, output_dim)

    def forward(self, x):
        return self.lin(x)


model = LinearRegression(input_size, output_size)

x_test = torch.tensor([
    [5]
], dtype=torch.float32)

print(f'Prediction before training: f(5) = {model(x_test).item():.3f}')

# Training
learning_rate = 0.01
n_iters = 100

loss = nn.MSELoss()
optimizer = SGD(model.parameters(), lr=learning_rate)

for epoch in range(n_iters):
    # prediction = forward pass
    y_pred = model(X)

    # loss
    l = loss(Y, y_pred)

    # gradients = backward pass
    l.backward()  # dl/dw

    # update weights
    optimizer.step()

    # zero gradients
    optimizer.zero_grad()

    if epoch % 10 == 0:
        [w, b] = model.parameters()
        print(f'epoch {epoch + 1}: w = {w[0][0].item():.3f}, loss = {l:.8f}')

print(f'Prediction before training: f(5) = {model(x_test).item():.3f}')
