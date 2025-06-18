from aws.secret import get_secret
import dotenv
import os


def set_environment_by_secret_manager() -> None:
    """
    Secret Manager에서 가져온 환경변수를 설정한다.
    :rtype: None
    """
    secrets_dict = dict(get_secret())
    if not secrets_dict:
        print("환경변수가 없습니다.")

    for k, v in secrets_dict.items():
        if k in os.environ:
            continue
        if v is not None:
            os.environ[k] = v

def set_environment_by_dotenv() -> None:
    """
    .env 파일에서 환경변수를 설정한다.
    :rtype: None
    """
    dotenv.load_dotenv(override=True)


# set_environment_by_secret_manager()
# set_environment_by_dotenv()
