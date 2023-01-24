import pymongo


def manipula_dados():
    cliente = pymongo.MongoClient("mongodb://172.26.150.168:27017")
    db = cliente.conheca_python

    for i in range(1, 10):
        obj_dic = {"codigo": i}
        db.conheca_mongo.insert_one(obj_dic)

    res_con = db.conheca_mongo.find()
    db.conheca_mongo.delete_one({"codigo": 9})
    db.conheca_mongo.update_one(
        {"codigo": 2}, {"$set": {"atributo_novo": 789}})
    for doc in res_con:
        print(doc)
    print("[INFO] - Manipulação concluída!")


def main():
    manipula_dados()


if __name__ == "__main__":
    main()
