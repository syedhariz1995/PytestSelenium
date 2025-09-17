# Note that this right now in in python file, as JSON can't be comment.
# JSON starts with { }

# inside can be like :

# {
#     "data" : hariz,
# }

# put an array, and inside the array, there can be sub-JSON. Each sub-JSON is one set of test data to run on another file
# example JSON format : 

# esentially its like [{"a" : "hehe"}, {"b" : "haha"}, {"c" : "hoho"}]
#                       1st test run,   2nd test run,    3rd test run
{
    # main key, full of sets of data in an array
    "data" : [
        # 1st data set, (index 0)
        {
            "userEmail" : "rahulshettyacademy",
            "userPassword" : "learning",
            "productName" : "Blackberry"
        },
        
        # 2nd data set , (index 1)
        {
            "userEmail" : "rahulshettyacademy",
            "userPassword" : "learning",
            "productName" : "Samsung Note 8"
        }
    ]
}



