#!/usr/bin/env python3
"""
图像高清修复脚本
使用多种图像增强技术提升照片质量
"""

from PIL import Image, ImageEnhance, ImageFilter

def enhance_image(input_path, output_path):
    """
    增强图像质量

    Args:
        input_path: 输入图像路径
        output_path: 输出图像路径
    """
    print(f"正在读取图像: {input_path}")

    # 打开图像
    img = Image.open(input_path)

    # 获取原始尺寸
    original_size = img.size
    print(f"原始尺寸: {original_size}")

    # 1. 放大图像 (2倍) - 使用LANCZOS高质量插值
    print("步骤 1/6: 放大图像...")
    enlarged_size = (original_size[0] * 2, original_size[1] * 2)
    img = img.resize(enlarged_size, Image.Resampling.LANCZOS)

    # 2. 降噪 - 使用中值滤波
    print("步骤 2/6: 降噪处理...")
    img = img.filter(ImageFilter.MedianFilter(size=3))

    # 3. 锐化增强
    print("步骤 3/6: 锐化处理...")
    img = img.filter(ImageFilter.UnsharpMask(radius=2, percent=150, threshold=3))

    # 4. 增强细节
    print("步骤 4/6: 增强细节...")
    img = img.filter(ImageFilter.DETAIL)

    # 5. 调整对比度
    print("步骤 5/6: 调整对比度...")
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(1.2)

    # 6. 调整清晰度
    print("步骤 6/6: 调整清晰度...")
    enhancer = ImageEnhance.Sharpness(img)
    img = enhancer.enhance(1.5)

    # 7. 轻微调整色彩
    enhancer = ImageEnhance.Color(img)
    img = enhancer.enhance(1.1)

    # 保存增强后的图像
    print(f"保存增强图像到: {output_path}")
    img.save(output_path, quality=95, optimize=True)

    print("✅ 图像增强完成！")
    print(f"输出尺寸: {img.size}")

    return img

def enhance_image_advanced(input_path, output_path):
    """
    高级图像增强（保持原始尺寸）
    """
    print(f"正在读取图像: {input_path}")

    img = Image.open(input_path)
    original_size = img.size
    print(f"原始尺寸: {original_size}")

    # 先放大4倍进行处理
    print("超分辨率处理...")
    temp_size = (original_size[0] * 4, original_size[1] * 4)
    img = img.resize(temp_size, Image.Resampling.LANCZOS)

    # 降噪
    img = img.filter(ImageFilter.MedianFilter(size=3))

    # 多次锐化
    for i in range(2):
        img = img.filter(ImageFilter.UnsharpMask(radius=2, percent=120, threshold=2))

    # 增强细节
    img = img.filter(ImageFilter.DETAIL)
    img = img.filter(ImageFilter.EDGE_ENHANCE)

    # 调整
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(1.15)

    enhancer = ImageEnhance.Sharpness(img)
    img = enhancer.enhance(1.3)

    enhancer = ImageEnhance.Brightness(img)
    img = enhancer.enhance(1.05)

    # 最终输出为2倍大小
    final_size = (original_size[0] * 2, original_size[1] * 2)
    img = img.resize(final_size, Image.Resampling.LANCZOS)

    print(f"保存到: {output_path}")
    img.save(output_path, quality=98, optimize=True)

    print("✅ 高级增强完成！")
    print(f"输出尺寸: {img.size}")

    return img

if __name__ == "__main__":
    input_path = "/Users/maxiao/Downloads/13671776.png"
    output_path = "/Users/maxiao/Downloads/13671776_enhanced.png"
    output_path_hd = "/Users/maxiao/Downloads/13671776_enhanced_hd.png"

    print("=" * 60)
    print("图像高清修复工具")
    print("=" * 60)
    print()

    # 标准增强
    print("【方案1：标准增强 - 2倍放大】")
    enhance_image(input_path, output_path)

    print("\n" + "=" * 60 + "\n")

    # 高级增强
    print("【方案2：高级增强 - 超清处理】")
    enhance_image_advanced(input_path, output_path_hd)

    print("\n" + "=" * 60)
    print("🎉 所有处理完成！")
    print(f"标准版: {output_path}")
    print(f"超清版: {output_path_hd}")
    print("=" * 60)
