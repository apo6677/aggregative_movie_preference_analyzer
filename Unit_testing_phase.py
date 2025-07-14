import math
import random

###################################################################################################################################################################################
###-----------------------------------------------------------------------------------RATING ---------------------------------------------------------------------------------
###################################################################################################################################################################################

def data_handling_ratings():

    filtered_ratings = dict()
    average_ratings = dict()
    movies = dict()

    with open("movies.dat","r", encoding="utf-8") as Mov:
            for line in Mov:
                data = line.strip().split('::')

                MovieID = data[0]
                Title = data[1]
                
                movies[MovieID] = Title

    with open("ratings.dat","r") as ratings:
        for line in ratings:
            data = line.strip().split('::')

            MovieID = data[1]
            Rating = float(data[2])
            
            if MovieID in average_ratings:
                average_ratings[MovieID]['Total_Rating'] +=Rating
                average_ratings[MovieID]['Count'] += 1
            else:
                average_ratings[MovieID] = {'Total_Rating': Rating, 'Count': 1}

    for MovieID in movies:
        if MovieID in average_ratings.keys():
            Title = movies[MovieID]
            average_rating = average_ratings[MovieID]['Total_Rating']/average_ratings[MovieID]['Count']
            filtered_ratings[Title] = average_rating

    with open("first_user_search_of_ratings.txt", "w", encoding="utf-8") as searched_ratings:
        for Title in filtered_ratings.keys():
            searched_ratings.write(Title +"::"+str(filtered_ratings[Title])+ '\n') 
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def find_movies_between_T1_T2(T1, T2, a):
    final_ratings = dict()

    if a == 0:
        data_handling_ratings()

    with open("first_user_search_of_ratings.txt", "r", encoding="utf-8") as searched_ratings:
            for line in searched_ratings:
                data = line.strip().split('::')

                Title = data[0]
                Rating = float(data[1])
                if T1 <= Rating <= T2:
                    final_ratings[Title] = Rating

    for Title in final_ratings:
        print("Movie Title:", Title, "Average Rating:", final_ratings[Title], "\n")

    T1_T2_a = f"rating_{T1}_{T2}.txt"

    with open(T1_T2_a, "w", encoding="utf-8") as new_entry:
        for Title in final_ratings.keys():
            new_entry.write(f"Movie Title: {Title}, Average Rating: {final_ratings[Title]}\n")   
    
    returning_variable = ""
    with open(T1_T2_a, "r", encoding="utf-8") as returning_file:
        returning_variable = returning_file.read()
    return returning_variable

###################################################################################################################################################################################
###-----------------------------------------------------------------------------------TOP MOVIES ---------------------------------------------------------------------------------
###################################################################################################################################################################################

def data_handling_top_movies():

    filtered_ratings = dict()
    average_ratings = dict()
    movies = dict()

    with open("movies.dat","r", encoding="utf-8") as Mov:
        for line in Mov:
            data = line.strip().split('::')

            MovieID = data[0]
            Title = data[1]
            
            movies[MovieID] = Title

    with open("ratings.dat","r") as ratings:
        for line in ratings:
            data = line.strip().split('::')

            MovieID = data[1]
            Rating = float(data[2])
            
            if MovieID in average_ratings:
                average_ratings[MovieID]['Total_Rating'] +=Rating
                average_ratings[MovieID]['Count'] += 1
            else:
                average_ratings[MovieID] = {'Total_Rating': Rating, 'Count': 1}
        
    for MovieID in movies:
        if MovieID in average_ratings.keys():
            Title = movies[MovieID]
            average_rating = average_ratings[MovieID]['Total_Rating']/average_ratings[MovieID]['Count']
            filtered_ratings[Title] = average_rating

    with open("first_top_movies_search.txt", "w", encoding="utf-8") as searched_top_movies:
        for Title in filtered_ratings.keys():
            searched_top_movies.write(Title +"::"+str(filtered_ratings[Title])+ '\n')

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def find_top_movies(K, b): 
    filtered_ratings = dict()

    if b == 0:
        data_handling_top_movies()

    with open("first_top_movies_search.txt", "r", encoding="utf-8") as searched_top_movies:
            for line in searched_top_movies:
                data = line.strip().split('::')

                Title = data[0]
                Rating = float(data[1])
                filtered_ratings[Title] = Rating

    sorted_ratings = sorted(filtered_ratings.items(), key=lambda x: x[1], reverse=True)
    top_K_movies = sorted_ratings[:K]
    
    for Title, Average_Rating in top_K_movies:
        print("Movie Title:", Title, "Average Rating:", Average_Rating, "\n")

    Kappa = f"top_movies_{K}.txt"

    with open(Kappa, "w", encoding="utf-8") as new_entry:
        for Title, Average_Rating in top_K_movies:
            new_entry.write(f"Movie Title: {Title}, Average Rating: {Average_Rating}\n")

    returning_variable = ""
    with open(Kappa, "r", encoding="utf-8") as returning_file:
        returning_variable = returning_file.read()
    return returning_variable

###################################################################################################################################################################################
###-----------------------------------------------------------------------------------USER PAIRS ---------------------------------------------------------------------------------
###################################################################################################################################################################################
def handling_user_pairs(K):
    user_pairs = dict()
    filtered_pairs = dict()
    movies = dict()
    MovieIds = []

    with open("movies.dat","r", encoding="utf-8") as Mov:
        for line in Mov:
            data = line.strip().split('::')

            MovieID = data[0]
            Title = data[1]
            
            movies[MovieID] = Title
            MovieIds.append(MovieID)


    with open("ratings.dat","r") as ratings:
        for line in ratings:
            data = line.strip().split('::')

            MovieID = data[1]
            UserID = data[0]
            
            if MovieID in user_pairs:
                if len(user_pairs[MovieID]) == 2:
                    continue;
                else:
                    user_pairs[MovieID].append(int(UserID))    
            else:
                user_pairs[MovieID] = [int(UserID)]

    chosen_movies = random.sample(MovieIds, min(K, len(MovieIds)))
  
    for MovieID in chosen_movies:
        if MovieID in user_pairs.keys():
            Title = movies[MovieID]
            filtered_pairs[Title] = user_pairs[MovieID]
    
    with open("first_user_pairs_search.txt", "w", encoding="utf-8") as searched_user_pairs:
        for Title in filtered_pairs.keys():
            searched_user_pairs.write(Title +"::"+str(filtered_pairs[Title])+ '\n')
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def find_user_pairs(K, c):
    final_pairs = dict()
    if c == 0:
        handling_user_pairs(K)

    with open("first_user_pairs_search.txt", "r", encoding="utf-8") as searched_user_pairs:
            for line in searched_user_pairs:
                data = line.strip().split('::')

                Title = data[0]
                Pair = data[1]
                final_pairs[Title] = Pair

    for Title in final_pairs:
        print("Movie Title:", Title, "Users Pair:", final_pairs[Title], "\n")

    Kappa = f"user_pairs_{K}.txt"

    with open(Kappa, "w", encoding="utf-8") as new_entry:
        for Title in final_pairs.keys():
            new_entry.write(f"Movie Title: {Title}, Users Pair: {final_pairs[Title]}\n")

    returning_variable = ""
    with open(Kappa, "r", encoding="utf-8") as returning_file:
        returning_variable = returning_file.read()
    return returning_variable

###################################################################################################################################################################################
###-----------------------------------------------------------------------------------ICEBERG ---------------------------------------------------------------------------------
###################################################################################################################################################################################
def handling_iceberg():

    iceberg_movies = dict()
    movies = dict()

    with open("movies.dat","r", encoding="utf-8") as Mov:
        for line in Mov:
            data = line.strip().split('::')

            MovieID = data[0]
            Title = data[1]
            
            movies[MovieID] = Title


    with open("ratings.dat","r") as ratings:
        for line in ratings:
            data = line.strip().split('::')

            MovieID = data[1]
            Rating = float(data[2])
            
            if MovieID in iceberg_movies:
                iceberg_movies[MovieID]['Total_Rating'] +=Rating
                iceberg_movies[MovieID]['Count'] += 1   
            else:
                iceberg_movies[MovieID] = {'Movie': MovieID, 'Total_Rating': Rating, 'Count': 1}

  
    for MovieID in movies:
        if MovieID in iceberg_movies.keys():
            average_rating = iceberg_movies[MovieID]['Total_Rating']/iceberg_movies[MovieID]['Count']
            iceberg_movies[MovieID]['Total_Rating'] = average_rating

    
    with open("first_user_search_of_iceberg.txt", "w", encoding="utf-8") as searched_iceberg:
        for Title in iceberg_movies.keys():
            searched_iceberg.write(Title +"::"+str(iceberg_movies[Title]['Total_Rating'])+"::"+ str(iceberg_movies[Title]['Count'])+ '\n')  

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def iceberg(K,T, d):
    final_movies = dict()
    if d==0:
        handling_iceberg()

    with open("first_user_search_of_iceberg.txt", "r", encoding="utf-8") as searched_iceberg:
        for line in searched_iceberg:
            data = line.strip().split('::')

            Title = data[0]
            Rating = float(data[1])
            Count = int(data[2])

            if Count >= K and Rating >= T:
                final_movies[Title] = {'Count': Count, 'Total_Rating': Rating}

    for Title in final_movies:
        print("Movie Title:", Title, "Number of critics:", final_movies[Title]['Count'], "Average Rating:", final_movies[Title]['Total_Rating'], "\n")

    K_T = f"iceberg_{K}_{T}.txt"

    with open(K_T, "w", encoding="utf-8") as new_entry:
        for Title in final_movies.keys():
            new_entry.write(f"Movie Title: {Title}, Average Rating: {final_movies[Title]}\n")

    returning_variable = ""
    with open(K_T, "r", encoding="utf-8") as returning_file:
        returning_variable = returning_file.read()
    return returning_variable

###################################################################################################################################################################################
###-----------------------------------------------------------------------------------TOP USER---------------------------------------------------------------------------------
###################################################################################################################################################################################
def handling_top_user():
    users = dict()
   
    with open("ratings.dat","r") as ratings:
        for line in ratings:
            data = line.strip().split('::')

            UserID = data[0]
            
            if UserID in users:
                users[UserID]+=1    
            else:
                users[UserID] = 1

    sorted_users = sorted(users.items(), key=lambda x: x[1], reverse=True)

    with open("first_user_search_of_top_user.txt", "w", encoding="utf-8") as searched_top_user:
        for User, Critics in sorted_users:
            searched_top_user.write(User +"::"+str(Critics)+ '\n')
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------           
def top_users(K, e):
    Users = list()
    if e ==0:
        handling_top_user()
    with open("first_user_search_of_top_user.txt", "r", encoding="utf-8") as searched_top_user:
            for line in searched_top_user:
                data = line.strip().split('::')

                User = data[0]
                Critics = data[1]

                Users.append((User,Critics))

    top_K_users = Users[:K]

    for UserID, Critics in top_K_users:
        print("User:", UserID, "Movies:", Critics, "\n")

    Kappa = f"top_user_{K}.txt"

    with open(Kappa, "w", encoding="utf-8") as new_entry:
        for UserID, Critics in top_K_users:
            new_entry.write(f"User: {UserID}, Movies: {Critics}\n")

    returning_variable = ""
    with open(Kappa, "r", encoding="utf-8") as returning_file:
        returning_variable = returning_file.read()
    return returning_variable
###################################################################################################################################################################################
###-----------------------------------------------------------------------------------MOVIE SAMPLE---------------------------------------------------------------------------------
###################################################################################################################################################################################
def handling_movie_sample():
    movies = dict()
    categorised_movies = dict()

    with open("movies.dat","r", encoding="utf-8") as Mov:
        for line in Mov:
            data = line.strip().split('::')

            Categories = data[2].split('|')
            Title = data[1]
                
            movies[Title] = Categories

    for Title in movies:
        for Category in movies[Title]:
            if  Category in categorised_movies.keys():
                categorised_movies[Category].append(Title)
            else: categorised_movies[Category] = [Title]
    with open("first_user_search_of_movie_sample.txt", "w", encoding="utf-8") as searched_movie_sample:
        for Category in categorised_movies:
            movies_str = '|'.join(categorised_movies[Category])
            searched_movie_sample.write(f"{Category}::{movies_str}\n")
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def movie_sample(S, f):
    final_movies = dict()
    Movies = list()
    if f ==0:
        handling_movie_sample()

    with open("first_user_search_of_movie_sample.txt", "r", encoding="utf-8") as searched_movie_sample:
        for line in searched_movie_sample:
            data = line.strip().split('::')

            Category = data[0]
            Movies = data[1].split('|')
            final_movies[Category] = Movies

    for Category in final_movies:
        size = math.ceil(int((S/100)*len(final_movies[Category])))
        final_movies[Category] = final_movies[Category][:size]
        print("Category:", Category, "Movies:", final_movies[Category], "\n")

    Sigma = f"movie_sample_{S}.txt"

    with open(Sigma, "w", encoding="utf-8") as new_entry:
        for Category in final_movies:
            movies_str = ', '.join(final_movies[Category])
            new_entry.write(f"Category: {Category}, Movies: {movies_str}\n")

###################################################################################################################################################################################
###-----------------------------------------------------------------------------------COSINE SIMILARITY---------------------------------------------------------------------------------
###################################################################################################################################################################################
def handling_cosine():
    users_with_same_movies = dict()
    users = dict()
    user_movies = dict()
    cosine_users = dict()

    with open("ratings.dat","r") as ratings:
        for line in ratings:
            data = line.strip().split('::')

            UserID = data[0]
            MovieID = data[1]
            Rating = float(data[2])
            
            if UserID not in users:
                users[UserID] = []
            rating_entry = {MovieID: Rating}
            users[UserID].append(rating_entry)

            if UserID not in user_movies:
                user_movies[UserID] = []
            user_movies[UserID].append(MovieID)

    common_user_ids = list(set(users.keys()))
    selected_user_ids = random.sample(common_user_ids, 100)

    trimmed_users = {user_id: users[user_id] for user_id in selected_user_ids}
    trimmed_user_movies = {user_id: user_movies[user_id] for user_id in selected_user_ids}

    for UserID1 in trimmed_user_movies:
        for UserID2 in trimmed_user_movies:
            if UserID1 != UserID2: 
                common_movies = [movie for movie in trimmed_user_movies[UserID1] if movie in trimmed_user_movies[UserID2]]

                if len(common_movies) != 0:
                    if (UserID1, UserID2) not in users_with_same_movies:
                        if (UserID2, UserID1) not in users_with_same_movies:
                            users_with_same_movies[(UserID1, UserID2)] = []

                            for MovieID in common_movies:
                                users_with_same_movies[(UserID1, UserID2)].append(MovieID)
    

    for (UserID1, UserID2) in users_with_same_movies:
        cos_similar = 0
        sum_cos_sim_nominator = 0
        sum_cos_sim_denominator_user1 = 0
        sum_cos_sim_denominator_user2 = 0

        for MovieID in users_with_same_movies[(UserID1, UserID2)]:

            ratings_user1 = {list(movie.keys())[0]: list(movie.values())[0] for movie in trimmed_users[UserID1]}

            rating1 = 0
            for rating_entry in trimmed_users[UserID1]:
                rating1 = ratings_user1.get(MovieID, 0)

            ratings_user2 = {list(movie.keys())[0]: list(movie.values())[0] for movie in trimmed_users[UserID2]}

            rating2 = 0
            for rating_entry in trimmed_users[UserID2]:
                rating2 = ratings_user2.get(MovieID, 0)

            sum_cos_sim_nominator += rating1*rating2
            sum_cos_sim_denominator_user1 += rating1**2
            sum_cos_sim_denominator_user2 += rating2**2

        cos_similar = sum_cos_sim_nominator/(math.sqrt(sum_cos_sim_denominator_user1)*math.sqrt(sum_cos_sim_denominator_user2)) if (math.sqrt(sum_cos_sim_denominator_user1)*math.sqrt(sum_cos_sim_denominator_user2))!=0 else 0

        cosine_users[(UserID1, UserID2)] = cos_similar

    sorted_users = sorted(cosine_users.items(), key=lambda x: x[1], reverse=True)

    with open("first_user_search_of_cosine.txt", "w", encoding="utf-8") as searched_cosine:
        for ((UserID1, UserID2), similarity) in sorted_users:
            searched_cosine.write(f"{UserID1, UserID2}::{similarity}\n")

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def cosine_similarity(Thetta, g):
    cosine_users = dict()
    if g==0:
        handling_cosine()

    with open("first_user_search_of_cosine.txt", "r", encoding="utf-8") as searched_cosine:
        for line in searched_cosine:
            data = line.strip().split('::')

            pair = data[0]
            similarity = float(data[1])
            cosine_users[pair] = similarity

    final_cosine_users = dict()
    for pair in cosine_users:
        if cosine_users[pair] >= Thetta:
            final_cosine_users[pair] = cosine_users[pair]

    for pair in final_cosine_users:
        print("Users:", pair, "Cosine Similarity:", final_cosine_users[pair], "\n")

    Cos = f"similar_users_{Thetta}.txt"

    with open(Cos, "w", encoding="utf-8") as new_entry:
        for pair in final_cosine_users:
            new_entry.write(f"Users: {pair}, Similarity: {final_cosine_users[pair]}\n")
###################################################################################################################################################################################
###-----------------------------------------------------------------------------------DOMINANCE---------------------------------------------------------------------------------
###################################################################################################################################################################################
def dominance(h):
    if h == 1:
        prints = list()
        with open("dominance.txt", "r", encoding="utf-8") as prev_entry:
                for line in prev_entry:
                    prints.append(line+"\n")
        for i in prints:
            print(i)
        
        returning_variable = ""
        with open("dominance.txt", "r", encoding="utf-8") as returning_file:
            returning_variable = returning_file.read()
        return returning_variable

    movies_that_are_not_dominated = dict()
    average_ratings = dict()
    movies = dict()

    with open("movies.dat","r", encoding="utf-8") as Mov:
        for line in Mov:
            data = line.strip().split('::')

            MovieID = data[0]
            Title = data[1]
            
            movies[MovieID] = Title

    with open("ratings.dat","r") as ratings:
        for line in ratings:
            data = line.strip().split('::')

            MovieID = data[1]
            Rating = float(data[2])
            
            if MovieID in average_ratings:
                average_ratings[MovieID]['Total_Rating'] +=Rating
                average_ratings[MovieID]['Count'] += 1
            else:
                average_ratings[MovieID] = {'Total_Rating': Rating, 'Count': 1}

    for MovieID in movies:
        if MovieID in average_ratings.keys():
            Title = movies[MovieID]
            average_rating = average_ratings[MovieID]['Total_Rating']/average_ratings[MovieID]['Count']
            count = average_ratings[MovieID]['Count']
            movies_that_are_not_dominated[Title] = [count, average_rating]
            for MovieID2 in movies:
                if MovieID2!=MovieID:
                    if MovieID2 in average_ratings.keys():
                        average_rating2 = average_ratings[MovieID2]['Total_Rating']/average_ratings[MovieID2]['Count']
                        count2 = average_ratings[MovieID2]['Count']
                        if average_rating2 >= average_rating and count2>=count:
                            del movies_that_are_not_dominated[Title]
                            break;

    for Title in movies_that_are_not_dominated:
        count, average_rating = movies_that_are_not_dominated[Title]
        print("Movie Title:", Title, "Average Rating:", average_rating, "Total Votes:", count, "\n") 

    with open("dominance.txt", "w", encoding="utf-8") as dom:
        for Title in movies_that_are_not_dominated:
            count, average_rating = movies_that_are_not_dominated[Title]
            dom.write(f"Movie Title: {Title}, Average Rating: {average_rating}, Total Votes: {count}\n")

    returning_variable = ""
    with open("dominance.txt", "r", encoding="utf-8") as returning_file:
        returning_variable = returning_file.read()
    return returning_variable
###################################################################################################################################################################################
###-----------------------------------------------------------------------------------CALL PREVIOUS ENTRIES---------------------------------------------------------------------------------
###################################################################################################################################################################################  
def call_previous_entries(a, b, c):
    prints = list()
    a_b_c = f"{a}_{b}_{c}.txt"
    with open(a_b_c, "r", encoding="utf-8") as prev_entry:
            for line in prev_entry:
                prints.append(line+"\n")
    for i in prints:
        print(i)

    returning_variable = ""
    with open("a_b_c", "r", encoding="utf-8") as returning_file:
        returning_variable = returning_file.read()
    return returning_variable

def call_previous_entries2(a, b):
    prints = list()
    a_b = f"{a}_{b}.txt"
    with open(a_b, "r", encoding="utf-8") as prev_entry:
            for line in prev_entry:
                prints.append(line+"\n")
    for i in prints:
        print(i)

def check_if_previous_entry_exists(prev_entries, key, b, c):
    for entry in prev_entries:
        print(entry,"\n\n")
        if key in entry:
            if c is None:
                if entry[key] == b:
                    return False
            else:
                if entry[key] == [b,c]:
                   return False       
    return True
###################################################################################################################################################################################
###-----------------------------------------------------------------------------------MAIN---------------------------------------------------------------------------------
###################################################################################################################################################################################
def main():
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    g = 0
    h = 0
    previous_entries = list()
    last_10_inputs = dict()
    new_entry = False
    while(True):
        print("\nChoose\n\n 1) rating T1 T2: find all movies with rating between T1 and T2\n\n 2) top_movies K: find all movies with rating over K \n\n 3) user_pairs K: find all user pairs that have given rating to the same movie\n\n\
 4) dominance: find users that aren't dominated from other movies\n\n 5) iceberg K T: find movies that have been rated at least K times with average score over T\n\n 6) top_user K: find the K users that have rated the most movies\n\n\
 7) movie_sample S: find a percentage of movies from all categories\n\n 8) similar_users Θ: find users that have similar tastes in movies based on cosine similarity\n\n 9) S to stop\n\n")
        mode = [i for i in input(" ").split(' ')]

        if mode[0] == "S":
            break;
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
        if mode[0] == "rating":

            new_entry = check_if_previous_entry_exists(previous_entries, mode[0], mode[1], mode[2])
            if(new_entry):
                find_movies_between_T1_T2(float(mode[1]), float(mode[2]), a)
            else:
                call_previous_entries(mode[0], float(mode[1]), float(mode[2]))
            a = 1
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
        elif mode[0] == "top_movies":

            new_entry = check_if_previous_entry_exists(previous_entries, mode[0], mode[1], None)
            if(new_entry):
                find_top_movies(int(mode[1]), b)
            else:
                call_previous_entries2(mode[0], int(mode[1]))
            b = 1
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
        elif mode[0]== "user_pairs":

            new_entry = check_if_previous_entry_exists(previous_entries, mode[0], mode[1], None)
            if(new_entry):
                find_user_pairs(int(mode[1]), c)
            else:
                call_previous_entries2(mode[0], int(mode[1]))
            c = 1
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
        elif mode[0]== "iceberg":

            new_entry = check_if_previous_entry_exists(previous_entries, mode[0], mode[1], mode[2]) 
            if(new_entry):
                iceberg(int(mode[1]), float(mode[2]), d)
            else:
                call_previous_entries(mode[0], int(mode[1]), float(mode[2]))
                d = 1
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
        elif mode[0]== "top_user":

            new_entry = check_if_previous_entry_exists(previous_entries, mode[0], mode[1], None)
            if(new_entry):
                top_users(int(mode[1]), e)
            else:
                call_previous_entries2(mode[0], int(mode[1]))
            e = 1
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
        elif mode[0]== "movie_sample":

            new_entry = check_if_previous_entry_exists(previous_entries, mode[0], mode[1], None)
            if(new_entry):
                movie_sample(int(mode[1]), f)
            else:
                call_previous_entries2(mode[0], int(mode[1]))
            f = 1
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
        elif mode[0]== "similar_users":

            new_entry = check_if_previous_entry_exists(previous_entries, mode[0], mode[1], None)
            if(new_entry):
                cosine_similarity(float(mode[1]), g)
            else:
                call_previous_entries2(mode[0], float(mode[1]))
            g = 1
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
        elif mode[0]== "dominance":
            dominance(h)
            h = 1
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
        else : 
            print("not a choice, choose again")
            new_entry = False

        if(new_entry):
            if len(last_10_inputs)<10:
                if len(mode)==2:
                    last_10_inputs[mode[0]] = mode[1]
                elif len(mode)== 3:
                    last_10_inputs[mode[0]] = [mode[1], mode[2]]
            previous_entries.append({mode[0]: last_10_inputs[mode[0]]})

if __name__ == "__main__":
    main()
