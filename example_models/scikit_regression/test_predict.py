import unittest 
import predict
class TestPredict(unittest.TestCase):

    def test_predict_single_row(self):
        pass

    def test_predict_multiple_rows(self):
        input_json = """{"color":{"1":"Color","2":"Color","3":"Color"},"director_name":{"1":"Gore Verbinski","2":"Sam Mendes","3":"Christopher Nolan"},"num_critic_for_reviews":{"1":302.0,"
2":602.0,"3":813.0},"duration":{"1":169.0,"2":148.0,"3":164.0},"director_facebook_likes":{"1":563.0,"2":0.0,"3":22000.0},"actor_3_facebook_likes":{"1":1000.0,"2":161
.0,"3":23000.0},"actor_2_name":{"1":"Orlando Bloom","2":"Rory Kinnear","3":"Christian Bale"},"actor_1_facebook_likes":{"1":40000.0,"2":11000.0,"3":27000.0},"gross":{
"1":309404152.0,"2":200074175.0,"3":448130642.0},"genres":{"1":"Action|Adventure|Fantasy","2":"Action|Adventure|Thriller","3":"Action|Thriller"},"actor_1_name":{"1":
"Johnny Depp","2":"Christoph Waltz","3":"Tom Hardy"},"movie_title":{"1":"Pirates of the Caribbean: At World\'s End\\u00a0","2":"Spectre\\u00a0","3":"The Dark Knight
Rises\\u00a0"},"num_voted_users":{"1":471220,"2":275868,"3":1144337},"cast_total_facebook_likes":{"1":48350,"2":11700,"3":106759},"actor_3_name":{"1":"Jack Davenport
","2":"Stephanie Sigman","3":"Joseph Gordon-Levitt"},"facenumber_in_poster":{"1":0.0,"2":1.0,"3":0.0},"plot_keywords":{"1":"goddess|marriage ceremony|marriage propos
al|pirate|singapore","2":"bomb|espionage|sequel|spy|terrorist","3":"deception|imprisonment|lawlessness|police officer|terrorist plot"},"movie_imdb_link":{"1":"http:\
\/\\/www.imdb.com\\/title\\/tt0449088\\/?ref_=fn_tt_tt_1","2":"http:\\/\\/www.imdb.com\\/title\\/tt2379713\\/?ref_=fn_tt_tt_1","3":"http:\\/\\/www.imdb.com\\/title\\
/tt1345836\\/?ref_=fn_tt_tt_1"},"num_user_for_reviews":{"1":1238.0,"2":994.0,"3":2701.0},"language":{"1":"English","2":"English","3":"English"},"country":{"1":"USA",
"2":"UK","3":"USA"},"content_rating":{"1":"PG-13","2":"PG-13","3":"PG-13"},"budget":{"1":300000000.0,"2":245000000.0,"3":250000000.0},"title_year":{"1":2007.0,"2":20
15.0,"3":2012.0},"actor_2_facebook_likes":{"1":5000.0,"2":393.0,"3":23000.0},"imdb_score":{"1":7.1,"2":6.8,"3":8.5},"aspect_ratio":{"1":2.35,"2":2.35,"3":2.35},"movi
e_facebook_likes":{"1":0,"2":85000,"3":164000}}"""
        pass

    def test_predict_bad_input(self):
        pass
    
    def test_main(self):
        pass