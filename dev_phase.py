import math
import random
import cProfile

###################################################################################################################################################################################
###-----------------------------------------------------------------------------------RATING ---------------------------------------------------------------------------------
###################################################################################################################################################################################
def find_movies_between_T1_T2(T1, T2):
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
            if T1 <= average_rating <= T2:
                filtered_ratings[Title] = average_rating

    for Title in filtered_ratings:
        print("Movie Title:", Title, "Average Rating:", filtered_ratings[Title], "\n")

###################################################################################################################################################################################
###-----------------------------------------------------------------------------------TOP MOVIES ---------------------------------------------------------------------------------
###################################################################################################################################################################################

def find_top_movies(K):

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

    sorted_ratings = sorted(filtered_ratings.items(), key=lambda x: x[1], reverse=True)

    top_K_movies = sorted_ratings[:K]
    
    for Title, Average_Rating in top_K_movies:
        print("Movie Title:", Title, "Average Rating:", Average_Rating, "\n")

###################################################################################################################################################################################
###-----------------------------------------------------------------------------------USER PAIRS ---------------------------------------------------------------------------------
###################################################################################################################################################################################

def find_user_pairs(K):
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

    for Title in filtered_pairs:
        print("Movie Title:", Title, "Users:", filtered_pairs[Title], "\n")

###################################################################################################################################################################################
###-----------------------------------------------------------------------------------ICEBERG ---------------------------------------------------------------------------------
###################################################################################################################################################################################

def iceberg(K,T):

    iceberg_movies = dict()
    filtered_movies = dict()
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
            if iceberg_movies[MovieID]['Count'] < K or average_rating < T:
                del iceberg_movies[MovieID]
            else:
                Title = movies[MovieID]
                filtered_movies[Title] = iceberg_movies[MovieID]

    for Title in filtered_movies:
        print("Movie Title:", Title, "Number of critics:", filtered_movies[Title]['Count'], "Average Rating:", filtered_movies[Title]['Total_Rating'], "\n")

###################################################################################################################################################################################
###-----------------------------------------------------------------------------------TOP USER---------------------------------------------------------------------------------
###################################################################################################################################################################################

def top_users(K):
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


    top_K_users = sorted_users[:K]

    for UserID, Movies in top_K_users:
        print("User:", UserID, "Movies:", Movies, "\n")
###################################################################################################################################################################################
###-----------------------------------------------------------------------------------MOVIE SAMPLE---------------------------------------------------------------------------------
###################################################################################################################################################################################


def movie_sample(S):
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

    for Category in categorised_movies:
        size = math.ceil(int((S/100)*len(categorised_movies[Category])))
        categorised_movies[Category] = categorised_movies[Category][:size]
        print("Category:", Category, "Movies:", categorised_movies[Category], "\n")

###################################################################################################################################################################################
###-----------------------------------------------------------------------------------COSINE SIMILARITY---------------------------------------------------------------------------------
###################################################################################################################################################################################
def cosine_similarity(Thetta):
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

    final_cosine_users = dict()
    for ((UserID1, UserID2), similarity) in sorted_users:
        if similarity >= Thetta:
            final_cosine_users[(UserID1, UserID2)] = similarity

    for (UserID1, UserID2) in final_cosine_users:
        print("Users:", UserID1, UserID2, "Cosine Similarity:", final_cosine_users[(UserID1, UserID2)], "\n")
###################################################################################################################################################################################
###-----------------------------------------------------------------------------------DOMINANCE---------------------------------------------------------------------------------
###################################################################################################################################################################################
def dominance():
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

###################################################################################################################################################################################
###-----------------------------------------------------------------------------------MAIN---------------------------------------------------------------------------------
###################################################################################################################################################################################
'''def main():
    while(True):
        print("\nChoose\n\n 1) rating T1 T2: find all movies with rating between T1 and T2\n\n 2) top_movies K: find all movies with rating over K \n\n 3) user_pairs K: find all user pairs that have given rating to the same movie\n\n\
 4) dominance: find users that aren't dominated from other movies\n\n 5) iceberg K T: find movies that have been rated at least K times with average score over T\n\n 6) top_user K: find the K users that have rated the most movies\n\n\
 7) movie_sample S: find a percentage of movies from all categories\n\n 8) similar_users Θ: find users that have similar tastes in movies based on cosine similarity\n\n 9) S to stop\n\n")
        mode = [i for i in input(" ").split(' ')]

        if mode[0] == "S":
            break;

        if mode[0] == "rating":
            profiler = cProfile.Profile()
            profiler.enable()
            find_movies_between_T1_T2(float(mode[1]), float(mode[2]))
            profiler.disable()
            profiler.print_stats(sort="cumulative")

        elif mode[0] == "top_movies":
            profiler = cProfile.Profile()
            profiler.enable()
            find_top_movies(int(mode[1]))
            profiler.disable()
            profiler.print_stats(sort="cumulative")

        elif mode[0]== "user_pairs":
            profiler = cProfile.Profile()
            profiler.enable()
            find_user_pairs(int(mode[1]))
            profiler.disable()
            profiler.print_stats(sort="cumulative")

        elif mode[0]== "iceberg":
            profiler = cProfile.Profile()
            profiler.enable()
            iceberg(int(mode[1]), float(mode[2]))
            profiler.disable()
            profiler.print_stats(sort="cumulative")

        elif mode[0]== "top_user":
            profiler = cProfile.Profile()
            profiler.enable()
            top_users(int(mode[1]))
            profiler.disable()
            profiler.print_stats(sort="cumulative")

        elif mode[0]== "movie_sample":
            profiler = cProfile.Profile()
            profiler.enable()
            movie_sample(int(mode[1]))
            profiler.disable()
            profiler.print_stats(sort="cumulative")

        elif mode[0]== "similar_users":
            profiler = cProfile.Profile()
            profiler.enable()
            cosine_similarity(float(mode[1]))
            profiler.disable()
            profiler.print_stats(sort="cumulative")

        elif mode[0]== "dominance":
            profiler = cProfile.Profile()
            profiler.enable()
            dominance()

        else : print("not a choice, choose again")
        k =1

if __name__ == "__main__":
    main()'''

cProfile.run("find_movies_between_T1_T2(2.0, 2.2)")
