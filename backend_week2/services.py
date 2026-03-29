from repository import get_user_by_email, create_user as repo_create_user

class DuplicateEmailError(Exception):
    pass

def create_user(name: str, email: str) -> dict:
        if get_user_by_email(email) is not None:
            raise DuplicateEmailError()
        
        user=repo_create_user(name=name,email=email)
        return user

