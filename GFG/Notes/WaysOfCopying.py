# Copying in Python

"""

    There are three ways of copying an object
    1) Assigning using the assignment operator (=)
    2) Shallow Copy
    3) Deep Copy

    -------------------------------------------------------------
    1) Assigning using the assignment operator (=)

    when the original object is copied using the '=' operator to a new variable
    Lets say new_obj = old_obj
    The original object's reference is assigned to the new_obj variable.
    That means the new_obj variable points to the original object
    Whatever changes done to the elements of original object will reflect in the new object

    old_obj -> [_____]  <- new_obj

    Any changes to the original object will have effect on the new object and vice versa

    2) Shallow Copy

    Shallow copy creates a new object but copies the references of the elements of original object
    to the new object

    old_obj = [1, 2, [3, 4], 5]
    new_obj = shallow copy of old_obj

    => new_obj = [1, 2, [3, 4], 5]. But id(new_obj) != id(old_obj)
    if old_obj[2][0] = 9 then
    new_obj == [1, 2, [9, 4], 5] since it copied the reference of elements inside the original object

    Any changes to the original object will reflect in the new object and vice versa

    In python Shallow Copy can be done using copy module's copy method => copy.copy(old_obj)

    3) Deep Copy

    Deep copy creates a new object and recursively copies the elements of original object.
    The new object will be a deep clone of the original object

    In python deep copying can be done using copy module's deepcopy method => copy.deepcopy(x)

    Any changes to the original object will have no effect on the new object and vice versa.

"""