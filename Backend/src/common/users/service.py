from src.common.users.schema import UserBase
from src.database import read_database, write_database


class UsersService:
    def __init__(self):
        pass

    def create(self, name: str, email: str) -> UserBase:
        data = read_database()
        
        for user in data:
            if user.get("email") == email:
                return "An account with this email already exists"
        
        new_id = len(data) + 1  # Assign ID automatically
        new_user = UserBase(id=new_id, name=name, email=email)
        data.append(vars(new_user))
        write_database(data)
        return new_user

    def find_all(self) -> list[UserBase]:
        data = read_database()
        return [
            UserBase(email=user["email"], id=user["id"], name=user["name"])
            for user in data
        ]

    def find(self, id: int) -> UserBase:
        try:
            data = read_database()
            for user in data:
                if user["id"] == id:
                    return UserBase(
                        id=user["id"], name=user["name"], email=user["email"]
                    )
            return None  # Return None if user with the given id is not found
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            # Handle file or JSON decoding errors here
            return None

    def update(self, id: int, name: str,email:str) -> UserBase:
        data = read_database()
        for user_data in data:
            if user_data["id"] == id:
                user_data["name"] = name
                user_data["email"] = email
                write_database(data)
                return UserBase(**user_data)
        return None

    def delete(self, id: int) -> None:
        data = read_database()
        updated_data = [user_data for user_data in data if user_data.get("id") != id]
        write_database(updated_data)
