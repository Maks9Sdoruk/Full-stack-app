from common.users.service import UsersService


class UserService:

    def __init__(self):
        self.users_service: UsersService = UserService()

    def perform_create_user(self):
        self.users_service.create()
    
    def perform_find_all(self):
        self.users_service.find_all()
        
    def perform_find(self):
        self.users_service.find()
    
    def perform_delete(self):
        self.users_service.delete()
    
    def perform_update(self):
        self.users_service.update()
            
