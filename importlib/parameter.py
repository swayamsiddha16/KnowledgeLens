import importlib

def create_shape(shape_type):
    module_name = shape_type.lower()
    class_name = shape_type.capitalize()
    try:
        module = importlib.import_module(module_name)
        shape_class = getattr(module, class_name)
        return shape_class
    except (ImportError, AttributeError):
        return None

shape_type = input("Enter the type of shape: ")
shape_class = create_shape(shape_type)

if shape_class:
    shape = shape_class(12, 10) if shape_type == 'rect' else shape_class(12)
    shape.getArea()
    shape.getPerimeter()
else:
    print("Invalid shape type")