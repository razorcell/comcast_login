from typing import TypedDict, Optional

class TaskSettings(TypedDict):
    type: str
    websiteURL: str
    websiteKey: str
    pageAction: Optional[str]
    anchor: Optional[str]
    reload: Optional[str]

class CaptchaSettings(TypedDict):
    clientKey: str
    task: TaskSettings