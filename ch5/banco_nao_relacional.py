import pymongo


def manipula_dados():
    cliente = pymongo.MongoClient("mongodb://192.168.56.1:27017")
    db = cliente.conheca_python

    for i in range(1, 10):
        obj_dic = {"codigo": i}
        db.conheca_mongo.insert_one(obj_dic)

    res_con = db.conheca_mongo.find({})
    for doc in res_con:
        print(doc)
    db.conheca_mongo.delete_one({"codigo": 1})
    db.conheca_mongo.update({"codigo": 2}, {"$set": {"atributo_novo": 789}})


def main():
    manipula_dados()


if __name__ == "__main__":
    main()
