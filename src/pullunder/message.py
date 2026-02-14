import requests


def send_message(
    message: str,
    image_path: str = None,
    title: str = None,
    url: str = None,
    url_title: str = None,
    priority: int = None,
    timestamp: int = None,
    retry: int = None,
    expire: int = None,
    ttl: int = None,
    sound: str = None,
    html: bool = False,
    markdown: bool = False,
    token: str = None,
    user: str = None,
    device: str = None,
):
    """
    Send a message using the Pushover message api.

    Parameters
    ----------

    """

    r = requests.post(
        "https://api.pushover.net/1/messages.json",
        data={
            "token": token,
            "user": user,
            "message": message,
        },
        # files={
        #     "attachment": ("image.jpg", open("your_image.jpg", "rb"), "image/jpeg"),
        # },
    )
    print(r.text)
