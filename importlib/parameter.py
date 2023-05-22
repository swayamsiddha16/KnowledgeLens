import importlib

def create_shape(shape_type):
    module_name = shape_type.lower()
    class_name = shape_type.capitalize()
    try:
        module = importlib.import_module(module_name)
        return getattr(module, class_name)
    except (ImportError, AttributeError):
        return None


if __name__=='__main__':
    shape_type = input("Enter the type of shape: ")
    if shape_class := create_shape(shape_type):
        shape = shape_class(12, 10) if shape_type == 'rect' else shape_class(12)
        shape.getArea()
        shape.getPerimeter()
    else:
        print("Invalid shape type")
    
    
