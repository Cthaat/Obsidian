---
title: "VQVAE生成模型梗概"
category: "AI+量化"
tags: [AI+量化]
source: "quant-wiki.com"
created: 2026-05-30
---

![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/10/21/1729466068183-23134fce-3131-4262-b18c-f378d71af4f6.gif)

# VQVAE生成模型梗概

![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2024/10/20/1729465031968-b3c8959e-1d37-4b8a-91b1-b0b0dfe25143.png)

这是VQVAE生成模型的 PyTorch 实现 (<https://arxiv.org/abs/1711.00937>).

您可以在此处找到作者 [在 Tensorflow 中的原始实现](https://github.com/deepmind/sonnet/blob/master/sonnet/python/modules/nets/vqvae.py) 其中包含 [可以在 Jupyter 笔记本中运行的示例](https://github.com/deepmind/sonnet/blob/master/sonnet/examples/vqvae_example.ipynb).

## 安装依赖项

要安装依赖项，请使用 Python 3 创建 conda 或虚拟环境，然后运行 `pip install -r requirements.txt`.

## 运行 VQ VAE

To run the VQ-VAE simply run `python3 main.py`. Make sure to include the `-save` flag if you want to save your model. You can also add parameters in the command line. The default values are specified below:

要运行 VQ-VAE，只需运行`python3 main.py`。如果要保存模型，请确保包含`-save`标志。您还可以在命令行中添加参数。默认值如下所示：

```python
parser.add_argument("--batch_size", type=int, default=32)
parser.add_argument("--n_updates", type=int, default=5000)
parser.add_argument("--n_hiddens", type=int, default=128)
parser.add_argument("--n_residual_hiddens", type=int, default=32)
parser.add_argument("--n_residual_layers", type=int, default=2)
parser.add_argument("--embedding_dim", type=int, default=64)
parser.add_argument("--n_embeddings", type=int, default=512)
parser.add_argument("--beta", type=float, default=.25)
parser.add_argument("--learning_rate", type=float, default=3e-4)
parser.add_argument("--log_interval", type=int, default=50)
```

## 模型

VQ VAE 具有以下基本模型组件

1. `Encoder` 类并定义了 `x -> z_e`
2. 将编码器输出转换为离散的独热向量的类 `VectorQuantizer`，该向量是最近嵌入向量的索引 `z_e -> z_q`
3. `Decoder` 类并定义映射 `z_q -> x_hat` 并重建原始图像的类

编码器/解码器类是卷积和逆卷积堆栈，其架构中包含残差块 [参见 ResNet 论文](https://arxiv.org/abs/1512.03385). 其中残差模块由 `ResidualLayer` 和 `ResidualStack` 类定义。

这些组件按以下文件夹结构组织：

```
models/
    - decoder.py -> Decoder
    - encoder.py -> Encoder
    - quantizer.py -> VectorQuantizer
    - residual.py -> ResidualLayer, ResidualStack
    - vqvae.py -> VQVAE
```

## PixelCNN - 从 VQ VAE 潜在空间采样

为了从潜在空间中采样，我们在潜在像素值上拟合一个 PixelCNN `z_ij`。这里的技巧是认识到 VQ VAE 将图像映射到具有与 1 通道图像相同结构的潜在空间。例如，如果您运行默认的 VQ VAE 参数，您将 RGB 形状的图像映射`(32,32,3)`到具有形状的潜在空间(8,8,1)，这相当于 `(8,8,1)` 灰度图像。因此，您可以使用 PixelCNN 来拟合 8x8 1 通道潜在空间的“像素”值的分布。

要对潜在表示进行 PixelCNN 训练，首先需要遵循以下步骤：

1. 在您选择的数据集上训练 VQ VAE
2. 使用已保存的 VQ VAE 参数对数据集进行编码，并使用`np.save`保存离散潜在空间表示。在`quantizer.py`中quantizer.py是min_encoding_indices`变量。
3. 在函数`utils.load_latent_block`中指定保存的潜在空间数据集的路径.
4. 运行 PixelCNN 脚本

要运行 PixelCNN，只需输入

`python pixelcnn/gated_pixelcnn.py`

以及任何参数（参见 argparse 语句）。默认数据集是`LATENT_BLOCK`，它仅在您训练了 VQ VAE 并保存了潜在表示后才有效。
