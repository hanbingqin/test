import speech_recognition as sr

def recognize_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("请说话...")
        recognizer.adjust_for_ambient_noise(source)  # 调整环境噪声
        audio = recognizer.listen(source)  # 监听音频

        try:
            print("正在识别...")
            # text = recognizer.recognize_google(audio, language="zh-CN")  # 使用Google识别
            text = recognizer.recognize_sphinx(audio)
            print(f"识别结果: {text}")
        except sr.UnknownValueError:
            print("无法理解语音")
        except sr.RequestError as e:
            print(f"语音识别服务请求失败: {e}")

if __name__ == "__main__":
    recognize_speech()
