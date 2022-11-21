
from asyncio.log import logger
import requests
import json
import sys
import cohere


good_cal = 750
good_protein = 0.4
good_fat = 0.4
good_carb = 0.2

appid = "4347c720"
appkey = "4d86d5131bfbdd425244ed82f151fda3"


def search_food(query):
        url = 'https://api.edamam.com/api/food-database/parser?nutrition' \
              '-type=logging&ingr={query}&app_id={id}&app_key={key}' \
            .format(id=appid, key=appkey, query=query)

        r = requests.get(url)
        if r.status_code == 401:
            logger.error("invalid food api key")
            raise InvalidFoodApiKey

        r = r.json()
        if r.get("status") == "error":
            error = r.get("message")
            if not error:
                error = "Api request failed"
            logger.error(error)
            raise APIError
        return r


def create_data(name) :
    foods = search_food(name)
    #foods = json.load(foods)
    names = name
    #print(foods.keys())
    #print(foods['hints'])
    data = foods['hints'][0]
    # #print(data.keys())
    data_food = data['food']
    # data_measures = data['measures']
    # #print(data_food) 
    #print(data_food.keys())
    nutrients = data_food['nutrients']
    #print(nutrients)
    calories = nutrients["ENERC_KCAL"]
    protein = nutrients["PROCNT"]
    fat = nutrients["FAT"]
    carbs = nutrients["CHOCDF"]
    tot = protein + carbs + fat
    return carbs, fat, protein, calories, names

def food_data(list_food) :
    name = ""
    str_carb = ""
    str_prot = ""
    str_fat = ""
    carbs = 0
    l = len(list_food)
    data_list = [["", "", "", "", "", ""] for i in range(l)]
    fat = 0
    protein = 0
    for i in range(l) :
        data = create_data(list_food[i])
        serving = 1
        carbs = serving*data[0]
        fat = serving*data[1]
        protein = serving*data[2]
        tot = carbs + protein + fat 
        fp = float(fat/tot)
        pp = float(protein/tot)
        cp = float(carbs/tot)
        str_fib = "no"
        str_micro = "no"
        if cp <  0.1 : 
            str_carb = "na"
        elif cp > 0.1 and cp < 0.25:
            str_carb = "bad"
        elif cp > 0.25 and cp < 0.4:
            str_carb = "good"
        else :
            str_carb = "great"
       
        if pp <  0.1 : 
            str_prot = "na"
        elif pp > 0.1 and pp < 0.25:
            str_prot = "bad"
        elif pp > 0.25 and pp < 0.4:
            str_prot = "good"
        else :
            str_prot = "great"
        
        if fp <  0.1 : 
            str_fat = "na"
        elif fp > 0.1 and fp < 0.25:
            str_fat = "bad"
        elif fp > 0.25 and fp < 0.4:
            str_fat = "good"
        else :
            str_fat = "great"
        
        if str_prot == "na" and str_fat == "na" :
            str_fib = "yes"
            str_micro = "yes"
        if str_prot == "good" and str_fat == "na" :
            str_micro = "yes"
        if (str_fat ==  "great") and (str_carb == "great") :
            str_fat = ""
        name = data[4]
        data_list[i][0] = name
        data_list[i][1] = str_prot
        data_list[i][2] = str_fat
        data_list[i][3] = str_carb 
        data_list[i][4] = str_micro
        data_list[i][5] = str_fib

    return data_list

def grade(list_food) :
    x = ""
    data_list = food_data(list_food)
    
    count = 0
    sum = 0
    for i in range(len(list_food)) : 
        for j in range(6) :
            if data_list[i][j] == "good" :
                count += 1
            elif data_list[i][j] == "great" :
                count += 2
            elif data_list[i][j] == "sat" :
                count -= 2
            elif data_list[i][j] == "yes" :
                count += 1
            else :
                count += 0
            
    

    if count < 4 :
        x = "D"
    elif count <= 8 and count >= 4:
        x = "C"
    elif count < 12 and count > 8:
        x = "B"
    else :
        x = "A"
    
    return x

print(grade(["spinach", "broccoli", "steak"]))

def nut_sum(list_food) :
    text = "The following is a comma separated table of ingredients and their quality as a source of nutrients such as (protein, fat, carbs, fibrous, micro):  "
    data = food_data(list_food) 
    for i in range(len(list_food)) :
        for j in range (6) :
            if j == 5 :
                s = "\n"
            else :
                s = ","

            text += (" " + data[i][j] +  s)
    print(text)

    
    
    co = cohere.Client('rgQ0vkNrfhNpttrjPU6dGgcNSTjlcqhOOz3fPaev') 
    response = co.generate( 
        model='large', 
        prompt='The following is a comma separated table of ingredients and their quality as a source of nutrients such as (protein, fat, carbs, fibrous, micro):\n \nChicken,great,na,na,na,na\nBrocolli,na,na,na,yes,yes\nRice,na,na,good,no,no\n \nAnswer: This meal contains great sources of protein and healthy fibrous vegtables with high micronutrient contents. The meal has a good source of carbohydrates.\n \n--\n \nThe following is a comma separated table of ingredients and their quality as a source of nutrients such as (protein, fat, carbs, fibrous, micro):\n \nSteak,great,na,na\nButter,bad,sat,na\nGreen beans,na,na,na,yes,yes\n \nAnswer: This meal contains great sources of protein and healthy fibrous vegtables with high micronutrient contents. However, the meal contains saturated fats.\n--\nThe following is a comma separated table of ingredients and their quality as a source of nutrients such as (protein, fat, carbs, fibrous, micro):\n \nFish,great,great,bad,na,na\nPeas,good,na,na,yes,yes\nSweet Potatoes,na,na,goodGI\n \nAnswer: This meal contains great sources of protein, fats, and fibre with high micronutrient contents. The carbohydrate sources in this meal are amazing.\n \n--\n \nThe following is a comma separated table of ingredients and their quality as a source of nutrients such as (protein, fat, carbs, fibrous, micro):\n \nChickpeas,great,na,goodGI,na,na\nBrown rice,na,na,goodGI,na,na\n \nAnswer: This meal contains great sources of protein. The carbohydrate sources in this meal are amazing.\n \n--\n \nThe following is a comma separated table of ingredients and their quality as a source of nutrients such as (protein, fat, carbs, fibrous, micro):\n \nKidney Beans,great,na,goodGI,na,na\nWhite rice,na,na,good,na,na\n \nAnswer: This meal contains great sources of protein. The carbohydrate sources in this meal are amazing.\n \n--\n \nThe following is a comma separated table of ingredients and their quality as a source of nutrients such as (protein, fat, carbs, fibrous, micro):\n \nBanana, na, na, goodGI, yes,na\n \nAnswer: The carbohydrate sources in this meal are amazing. This meal contains great sources of fibre.\n \n--\n \nThe following is a comma separated table of ingredients and their quality as a source of nutrients such as (protein, fat, carbs, fibrous, micro):\n \nBlueberries,na,na,na,na,yes\n \nAnswer: This meal contains high micronutrient contents.\n \n--\n \nThe following is a comma separated table of ingredients and their quality as a source of nutrients such as (protein, fat, carbs, fibrous, micro):\n \nHummus,good,good,good,na,na\nPita,na,na,good,na,na\n \nAnswer: This meal good sources of protein, carbohydrates, and fat.\n \n--\n \nThe following is a comma separated table of ingredients and their quality as a source of nutrients such as (protein, fat, carbs, fibrous, micro):\n \nPeanut Butter,good,great,na,na,na\nMultigrain Bread,good,na,goodGI,na,na\n \nAnswer: This meal good sources of protein and fat. The carbohydrate sources in this meal are amazing.\n \n--\n \nThe following is a comma separated table of ingredients and their quality as a source of nutrients such as (protein, fat, carbs, fibrous, micro):\n \nBeef,great,good,na,na,na\nPotatoes,na,na,good,yes,na\npeas,good,na,na,yes,yes\n \nAnswer: This meal contains great sources of protein and healthy fibrous vegtables with high micronutrient contents. The meal has a good source of carbohydrates.\n \n--\n \nThe following is a comma separated table of ingredients and their quality as a source of nutrients such as (protein, fat, carbs, fibrous, micro):\n \nTofu,good,na,good,na,na\n \nAnswer: This meal contains good sources of protein. The carbohydrate sources in this meal are good.\n \n--\n \nThe following is a comma separated table of ingredients and their quality as a source of nutrients such as (protein, fat, carbs, fibrous, micro):\n \nFried Chicken,good,sat,bad,na,na\n \nAnswer: This meal contains good sources of protein. The carbohydrate and fat sources in this meal are inadequate.\n \n--\n \nThe following is a comma separated table of ingredients and their quality as a source of nutrients such as (protein, fat, carbs, fibrous, micro):\n \npoutine,bad,sat,bad,na,na\n \nAnswer: The proteins and carbohydrates in this meal are inadequate. The meal contains saturated fats.\n \n--\nThe following is a comma separated table of ingredients and their quality as a source of nutrients such as (protein, fat, carbs, fibrous, micro):\n \nChessecake,good,sat,na,na,na\n \nAnswer: The meal contains goos sources of protein. The meal contains saturated fats.\n \n--\n \nThe following is a comma separated table of ingredients and their quality as a source of nutrients such as (protein, fat, carbs, fibrous, micro):\n \ntest,good,sat,good,na,na\n \nAnswer: The meal contains good sources of protein and carbohydrates. The meal contains saturated fats.\n \n--\n\ntest2 : great,sat,great\n\n\n\n\n' + text, 
        max_tokens=50, 
        temperature=0.5, 
        k=0, 
        p=1, 
        frequency_penalty=0, 
        presence_penalty=0, 
        stop_sequences=["--"], 
        return_likelihoods='NONE') 
    resp = response.generations[0].text
    return resp 
    


    

    


        




 



        

  











