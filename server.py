from flask import Flask, request, Response, jsonify
import flask
import win32com.client
import random
import math
import json
from datetime import date
import string_utils
import numpy as np



qng = win32com.client.Dispatch("QWQNG.QNG") 

app = Flask(__name__)



@app.route('/1kball/dev/api/v1/5d', methods=['GET'])
def get_five_d():
    
    try:
        random32_from_device: str = abs(qng.RandInt32)
        qng.Clear()
        qng.Reset()

        my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        new_number = str(random.choice(my_list))

        # numbers: int
        # numbers = abs(random32_from_device)
        fixed_number = int(new_number)
        output_numbers: int
        temp_numbers = []
        draw_numbers = []
        data = ""
        # draw_numbers2 = random.sample(range(0, 9), 5)
        
    
        S1 = str(random32_from_device)
        S2 = str(fixed_number)

        if(len(S1) < 10 ):

            S3 = S1 + S2

            retsults = int(S3)
            output_numbers = retsults
            
        else:
            output_numbers = random32_from_device


        for i in range(5):
                temp_numbers.append(string_utils.shuffle(str(output_numbers)))

        for i in range(5):
            draw_numbers.append(random.choice(str(output_numbers)))
        

        data = ','.join(map(str, draw_numbers))
      
            

    except Exception as e:
        print(e)

    
    return jsonify({'draw_number': data})

#------------------------------------------------------------------------#

@app.route('/1kball/dev/api/v1/3d', methods=['GET'])
def get_three_d():

    try:
        random32_from_device: str = abs(qng.RandInt32)
        qng.Clear()
        qng.Reset()

        my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        new_number = str(random.choice(my_list))

        fixed_number = int(new_number)
        output_numbers: int
        temp_numbers = []
        draw_numbers = []
        data = ""
        
        S1 = str(random32_from_device)
        S2 = str(fixed_number)

        if(len(S1) < 10 ):

            S3 = S1 + S2

            retsults = int(S3)
            output_numbers = retsults
            
        else:
            output_numbers = random32_from_device


        for i in range(3):
                temp_numbers.append(string_utils.shuffle(str(output_numbers)))

        for i in range(3):
            draw_numbers.append(random.choice(str(output_numbers)))
        

        data = ','.join(map(str, draw_numbers))
      
            

    except Exception as e:
        print(e)

    
    return jsonify({'draw_number': data})


#------------------------------------------------------------------------#

@app.route('/1kball/dev/api/v1/fast_3', methods=['GET'])
def get_fast_3():

    try:
        random32_from_device: str = abs(qng.RandInt32)
        qng.Clear()
        qng.Reset()

        my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        new_number = str(random.choice(my_list))
        nums_list = [int(x) for x in str(random32_from_device)]
        draw_number1to6 = random.sample(range(1, 7), 3)
    
        
        #------------------  Not used   ------------------------------#
        fixed_number = int(new_number)
        output_numbers: int
        temp_numbers = []
        draw_numbers = []
        data = ""
        
        S1 = str(random32_from_device)
        S2 = str(fixed_number)

        if(len(S1) < 10 ):

            S3 = S1 + S2

            retsults = int(S3)
            output_numbers = retsults
            
        else:
            output_numbers = random32_from_device


        for i in range(3):
                temp_numbers.append(string_utils.shuffle(str(output_numbers)))

        for i in range(3):
            draw_numbers.append(random.choice(str(output_numbers)))
        
        #--------------------------  Not used  ----------------------------------------#

        data = ','.join(map(str, draw_number1to6))
      
            

    except Exception as e:
        print(e)

    
    return jsonify({'draw_number': data})


#------------------------------------------------------------------------#

@app.route('/1kball/dev/api/v1/pc_28', methods=['GET'])
def get_pc_28():

    try:
        random32_from_device: str = abs(qng.RandInt32)
        qng.Clear()
        qng.Reset()

        my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        new_number = str(random.choice(my_list))

        fixed_number = int(new_number)
        output_numbers: int
        temp_numbers = []
        draw_numbers = []
        data = ""
        
        S1 = str(random32_from_device)
        S2 = str(fixed_number)

        if(len(S1) < 10 ):

            S3 = S1 + S2

            retsults = int(S3)
            output_numbers = retsults
            
        else:
            output_numbers = random32_from_device


        for i in range(3):
                temp_numbers.append(string_utils.shuffle(str(output_numbers)))

        for i in range(3):
            draw_numbers.append(random.choice(str(output_numbers)))
        

        data = ','.join(map(str, draw_numbers))
      
            

    except Exception as e:
        print(e)

    
    return jsonify({'draw_number': data})


#------------------------------------------------------------------------#

@app.route('/1kball/dev/api/v1/pk_10', methods=['GET'])
def get_pk_10():

    
    numbers = random.sample(range(1, 11), 10)
    random.shuffle(numbers)
    return jsonify({'draw_number': numbers})


#------------------------------------------------------------------------#

@app.route('/1kball/dev/api/v1/11x5', methods=['GET'])
def get_11x5():

    numbers = random.sample(range(1, 12), 5)
    random.shuffle(numbers)
    return jsonify({'draw_number': numbers})


#------------------------------------------------------------------------#

@app.route('/1kball/dev/api/v1/49x7', methods=['GET'])
def get_49x7():

    numbers = random.sample(range(1, 50), 7)
    random.shuffle(numbers)
    my_set = set(numbers)
    clx = ""

    if(len(numbers) != len(my_set)):
        clx = "Duplicate found"
    else:
        clx = "Duplicate not found"

    print(clx)
    return jsonify({'draw_number': numbers})






if(__name__ == '__main__'):
    app.run()