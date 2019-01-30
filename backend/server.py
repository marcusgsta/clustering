#!/usr/bin/python3
from flask import Flask, request, jsonify, render_template, make_response, jsonify
from flask_cors import CORS
from flask_restful import Resource, Api
from json import dumps

from clusters import *
from hierarchical import *


app = Flask(__name__,
            static_folder = "../dist/static",
            template_folder = "../dist")
cors = CORS(app, resources={r"/*": {"origins": "*"}})

api = Api(app)


def readfile(filename):
    """
    Reads text file with columns, rows and data
    Returns:
    array of rownames (blog names)
    array of colnames (words)
    array of data (occurrences of words)
    """
    # create array for lines in textfile
    # and fill array
    lines=[line for line in open(filename)]

    # - Create array and fill with colnames
    # - Strip from chars and split on tabs
    # - Slice/Leave out the first word in the lines array
    # since it is not a blogname
    colnames=lines[0].strip().split('\t')[1:]

    # Create array for rownames
    rownames=[]
    # Create array for each blog's data (occurences of each word)
    data=[]
    # loop through lines (except first which contains the words)
    for line in lines[1:]:
        row=line.strip().split('\t')
        # Fill rownames array with each blog name
        rownames.append(row[0])
        # Fill data array with data for each blog
        data.append([float(x) for x in row[1:]])

    return rownames,colnames,data


def convertFinalList(kclust, blognames):
    # Create a new list of lists with blognames instead of ids
    new_kclust = []
    for cluster in kclust:
        kclust_names = []
        for blogid in cluster:
            kclust_names.append(blognames[blogid])
        new_kclust.append(kclust_names)
    return new_kclust

class Kmeans(Resource):
    def get(self, iters):
        headers = {'Content-Type': 'text/html'}

        iters = int(iters)
        # read data file
        blognames,words,data = readfile('blogdata.txt')
        kclust = kcluster(data,nrOfClusters=10,nrOfIterations=iters)

        new_kclust = convertFinalList(kclust,blognames)

        response = {
            'blognames': blognames,
            'kclust': new_kclust,
            'iters': iters
        }

        return jsonify(response)

        # return make_response(render_template('clust.html', kclust=kclust, blognames=blognames, iters=iters), 200, headers)


class Kmeans2(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        # read data file
        blognames,words,data = readfile('blogdata.txt')
        kclust = kcluster(data,nrOfClusters=10)

        new_kclust = convertFinalList(kclust,blognames)

        response = {
            'blognames': blognames,
            'kclust': new_kclust,
        }

        return jsonify(response)


class Hierarchical(Resource):
    def get(self):
        header = {'Content-Type': 'text/html'}
        #read data file
        blognames,words,data = readfile('blogdata.txt')
        # data contains a list of lists with word counts
        initialClusters = createClusters(data)
        finalCluster = hierarchical(initialClusters)

        response = {
            'data': finalCluster,
            'blognames': blognames
        }
        return jsonify(response)


class Test(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        response = {
            'data': "Data from backend"
        }
        return jsonify(response)

api.add_resource(Test, '/test') # Route
api.add_resource(Kmeans2, '/') # Route
api.add_resource(Kmeans, '/iterations/<iters>') # Route
api.add_resource(Hierarchical, '/hierarchical') # Route



@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")



if __name__ == '__main__':
     app.run(host='0.0.0.0')
