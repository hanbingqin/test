from zhipuai import ZhipuAI
client = ZhipuAI(api_key="b7e88901786f46cca64c3629b37caee9.azmT0tAvhVrOzSNe") # 填写您自己的APIKey
response = client.chat.completions.create(
    model="glm-4v",  # 填写需要调用的模型名称
    messages=[
       {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "图里有什么"
          },
          {
            "type": "image_url",
            "image_url": {
                "url" : "https://img1.baidu.com/it/u=1369931113,3388870256&fm=253&app=138&size=w931&n=0&f=JPEG&fmt=auto?sec=1703696400&t=f3028c7a1dca43a080aeb8239f09cc2f"
            }
          }
        ]
      }
    ]
)
print(response.choices[0].message)