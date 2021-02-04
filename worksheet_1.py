import math
import random
import matplotlib.pyplot as plt


#Question 3 code
def question_one():
    x = [0, 1.5, 3, 4, 5, 7, 9, 10]
    y = []

    for x_val in x:
        y_val = 0.5*x_val - 2
        y.append(y_val)

    print('question 1:', y)

#Question 2 code
def question_two():
    t = [1,2,3,4,5,6,7,8,9,10]

    def compute_x():
        x = []
        for t_val in t:
            x_val = t_val*math.sin(t_val)
            x.append(x_val)
        print('x vals:', x)

    def compute_y():
        y = []
        for t_val in t:
            y_val = (t_val-1)/(t_val+1)
            y.append(y_val)
        print('y vals:', y)

    def compute_z():
        z = []
        for t_val in t:
            z_val = (math.sin(t_val**2))/(t_val**2)
            z.append(z_val)
        print('z vals:', z)

    compute_x()
    compute_y()
    compute_z()

#Question 3 code
def question_three():
    """
    Take r = 2 and compute the column vectors x and y.
    Also check that x and y indeed satisfy the equation of a
    circle by computing the radius r

    coords = [(x1, y1), (x2, y2), ]
    """
    theta = [0, math.pi/4, math.pi/2, 3*math.pi/4, math.pi, 5*math.pi/4]
    r = 2
    coords = []
    r_candidates = []

    #Compute x's and y's
    def compute_x_y():
        nonlocal coords
        for t in theta:
            x = r * math.cos(t)
            y = r * math.sin(t)
            coords.append((x, y))
        print('column vectors x & y:', coords)

    #Check r
    def check_r():
        for x, y in coords:
            r_cand = math.sqrt((x**2 + y**2))
            r_candidates.append(r_cand)
        print('radius candidates:', r_candidates)

    compute_x_y()
    check_r()

def question_four():
    # n = [0,1,2,3,4,5,6,7,8,9,10]
    r = 0.5
    x_50 = []
    x_100 = []

    for i in range(51):
        x_ = r**i
        x_50.append(x_)
    limit_50 = 1/(1-x_50[-1])
    s_50 = sum(x_50)

    for i in range(101):
        x_ = r**i
        x_100.append(x_)
    limit_100 = 1/(1-x_100[-1])
    s_100 = sum(x_100)

    print('x_50:', x_50)
    print('limit_50:', limit_50)
    print('s_50:', s_50)

    print('x_100:', x_100)
    print('limit_100:', limit_100)
    print('s_100:', s_100)

def question_five():
    #Create matrix
    m, n = 4, 3
    A = [[random.randint(1,50) for i in range(n)] for j in range(m)]
    print(A)

    #Get those elements of A that are located in rows 3 to 4 and columns 2 to 3
    sub_A = [[0 for i in range(2)] for j in range(2)]
    for i in range(2, 4):
        for j in range(1, 3):
            sub_A[i-2][j-1] = A[i][j]
    print("Elements that are located in rows 3 to 4 and columns 2 to 3:", sub_A)

    #Add a fourth column to A and set it equal to the first column of A.
    extra_col = []
    #get values of new col
    for i in range(m):
        extra_col.append(A[i][0])

    #set new col in A
    for i in range(m):
        A[i].append(extra_col[i])
    print("Post adding fourth column:", A)

    # Replace the last 3 × 3 submatrix of A(rows 2 to 4, columns 2 to 4)
    # by a 3 × 3 identity matrix.
    for i in range(1, 4):
        for j in range(1, 4):
            if i == j:
                A[i][j] = 1
            else:
                A[i][j] = 0
    print("Post replacing submatrix with identity matrix:", A)

    #Delete the first and third rows of A.
    A.remove(A[0])
    A.remove(A[2])
    print('Post removing first & last row:', A)

    #Round off all entries of A towards the nearest integer.
    m, n = len(A), len(A[0])
    for i in range(m):
        for j in range(n):
            A[i][j] = int(A[i][j])

    print('Post rounding:', A)

    string_out = []
    for i in range(m):
        for j in range(n):
            string_out.append(str(A[i][j]))
    print('string out elements in row:', string_out)

def question_six():
    """
 Create a vector and a matrix with the following commands: v=0:0.2:12;
 and M=[sin(v); cos(v)];.
 Find the size of v and M using the size command.

    """
    # create vector
    vector = []
    count = 0
    for i in range(60):
        count+=0.2
        vector.append(count)
    print("vector:", vector)

    matrix = [[0 for i in range(len(vector))] for j in range(2)]
    # Create matrix
    for i in range(len(matrix)):
        for j in range(len(vector)):
            if i == 0:
                matrix[i][j] = math.sin(vector[j])
            else:
                matrix[i][j] = math.cos(vector[j])
    print(' ')
    print("matrix M:", matrix)

    # Extract the first 10 elements of each row of the matrix and display them as column vectors
    col_vector_1 = []
    col_vector_2 = []
    for i in range(len(matrix)):
        for j in range(10):
            if i == 0:
                col_vector_1.append([matrix[i][j]])
            else:
                col_vector_2.append([matrix[i][j]])
    print("Column Vector 1:", col_vector_1)
    print("Column Vector 2:", col_vector_2)


def question_seven(a, b, c):
    """
    Compute the real roots of a quadratic equation
    """
    x_pos = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)

    x_neg = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)

    print('root 1:', x_pos)
    print('root 2:', x_neg)

def question_eight(A, B):
    """
    Perform the multiplication of A x B

              7  8
    1 2 3     9  10
    4 5 6  x  11 12
    """
    result = [[0 for i in range(len(B[0]))] for j in range(len(A))]
    # print('result:', result)

    #iterate through rows of A
    for i in range(len(A)):
        #iterate through cols of B
        for j in range(len(B[0])):
            #iterate through rows of B
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]


    print("result:", result)

def question_nine():
    x_vector = []
    x_val = 0
    #creating x
    for i in range(200):
        x_val += (math.pi/100)
        x_vector.append(x_val)
    # print("x_vector:", x_vector)

    #creating y
    y_vector_sin = []
    y_vector_cos = []
    for val in x_vector:
        y_vector_sin.append(math.sin(val))
        y_vector_cos.append(math.cos(val))
    # print("y_vector:", y_vector)

    plt.plot(y_vector_sin, label="sin")
    plt.plot(y_vector_cos, label="cos")
    plt.xlabel('x axis')
    plt.ylabel('y axis')
    plt.title('Sin and Cos plots in the range of 0 to 2pi')
    plt.legend()
    plt.show()


#Calling functions
# question_one()
print(" ----------------------- ")
# question_two()
print(" ----------------------- ")
# question_three()
print(" ----------------------- ")
# question_four()
print(" ----------------------- ")
# question_five()
print(" ----------------------- ")
# question_six()
print(" ----------------------- ")
# question_seven()
print(" ----------------------- ")
# question_eight([[1,2,3], [4,5,6]], [[7,8], [9,10], [11,12]])
print(" ----------------------- ")
question_nine()
