MONGO_URI = 'mongodb://localhost/stuff'
COLLECTION = 'cities'
PIPELINE = [
    {
        "$group": {
            "_id": "$CNTRY_NAME",
            "x": {"$avg": "$x"},
            "y": {"$avg": "$y"}
        }
    },
    {
        "$project": {
            'name': '$_id',
            'x': '$x',
            'y': '$y',
            '_id': 0
        }
    }
]
QUERY = {"POP": {"$gte": 100000}}
PROJECTION = {"CITY_NAME": 1, "x": 1, "y": 1, "_id": 0}