from http import HTTPStatus
import dashscope
from config import load_config

configs = load_config()


def simple_multimodal_conversation_call(is_online_image=True):
    """
    Simple single round multimodal conversation call.
    """
    if is_online_image:
        image_path = "https://dashscope.oss-cn-beijing.aliyuncs.com/images/dog_and_girl.jpeg"
    else:
        image_path = "file://./calculator.png"

    messages = [
        {
            "role": "user",
            "content": [
                {"image": image_path},
                {"text": "这是什么?"}
            ]
        }
    ]
    dashscope.api_key = configs["DASHSCOPE_API_KEY"]
    response = dashscope.MultiModalConversation.call(model=configs["QWEN_MODEL"],
                                                     messages=messages)
    # The response status_code is HTTPStatus.OK indicate success,
    # otherwise indicate request is failed, you can get error code
    # and message from code and message.
    if response.status_code == HTTPStatus.OK:
        print(response)
    else:
        print(response.code)  # The error code.
        print(response.message)  # The error message.


if __name__ == '__main__':
    # online image
    simple_multimodal_conversation_call()
    # local image
    # simple_multimodal_conversation_call(is_online_image=False)
