import numoy as np

def print_id(student_id):
    print("Student ID = ",student_id)

def calculate_sum(array):
    return array.sum()

def print_name(name):
    print("Your name is {} ".format(name))


if "__name__" == "__main__":
    print_id("345678")
    calculate_sum(np.array([1,2,3]))
    print_name("Sang")