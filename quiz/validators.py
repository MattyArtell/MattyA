from django.core.exceptions import ValidationError

def strip(name):
    myindex = name.index('.')
    new = name[myindex:]
    print(new)
    return new

def validate_file_size(value):
    filesize= value.size
    filename = value.name
    
    if filesize > 1048576:
        raise ValidationError("The maximum file size that can be uploaded is 1MB")
    elif strip(filename) != ".csv":
        raise ValidationError("The file must be csv")
    else:
        return value
