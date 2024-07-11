import bcrypt
import hashlib

def hash_password(password):
    # Generate a salt and hash the password
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

def verify_password(TimelinePost, name, input_password):
    try:
        user = TimelinePost.get(TimelinePost.name == name)
        hashed_password = user.password.encode('utf-8')
        return bcrypt.checkpw(input_password.encode('utf-8'), hashed_password)
    
    except TimelinePost.DoesNotExist:
        return False
    
