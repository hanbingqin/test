import os
import time
import sys
from unittest.mock import MagicMock


# 将 capture.py 的路径添加到 sys.path 中，以便导入 WebcamCapture 类
sys.path.append('/home/hanbingpi/projects/sixth-_sense-main/python_files')

from capture import WebcamCapture

# 模拟一个简化的语音助手类
class MockVoiceAssistant:
    def __init__(self):
        self.messages = []

    def speak(self, message):
        self.messages.append(message)
        print(f"Voice Assistant: {message}")

def test_capture_photo():
    # 创建一个模拟的语音助手实例
    voice_assistant = MockVoiceAssistant()

    # 创建 WebcamCapture 实例并传入模拟语音助手
    webcam_capture = WebcamCapture(voice_assistant)

    # 捕获一张照片并保存到指定路径
    save_path = "test_image.jpg"
    print("Starting photo capture...")
    
    # 运行捕获照片的方法
    image_path = webcam_capture.capture_photo(save_path=save_path)

    # 验证图像是否被保存
    assert os.path.exists(image_path), f"Image was not saved at {image_path}"

    print(f"Photo saved at: {image_path}")
    assert image_path.endswith(save_path), "The saved file path does not match the expected one."

    # 验证语音助手是否正确说了"Photo Captured"
    assert "Photo Captured" in voice_assistant.messages, "Voice assistant did not announce photo capture."

    print("Test passed!")

if __name__ == "__main__":
    test_capture_photo()
