from flask import Flask, render_template, request
import requests
import json
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection
from gremlin_python.process.anonymous_traversal import traversal

app = Flask(__name__)


# g = traversal().with_remote(DriverRemoteConnection('ws://localhost:8182/gremlin', 'g'))


# g.addV('person').property('name', 'marko').next()
# f"{g.V().has('person','name','marko').toList()}"

def adatb(name):
    # issue_id = []  # issuek id-jének tömbje
    # issue_assignees = []  # issue-hoz rendelt fejlesztők adatai
    # bubble layout

    commit_author = []  # commitok szerzőinek a neve

    # issues = requests.get(f"https://api.github.com/repos/{name[-2]}/{name[-1]}/issues").json()
    commits = requests.get(f"https://api.github.com/repos/{name[-2]}/{name[-1]}/commits").json()

    for commit in commits:
        commit_author.append(commit["commit"]["author"]["name"])

    commits_per_author = {i: commit_author.count(i) for i in
                          commit_author}  # commitok szerzőinek a neve és commitjainak száma

    """for author in commits_per_author.keys():
        g.addV('student').property('name', author).next()"""

    """for issue in issues:  # issuek id-jének és a hozzárendelt hallgatók lekérése
        issue_id.append(issue["id"])
        issue_assignees.append(issue["assignees"])"""

    # number_of_issues = len(issue_id)  # issuek száma
    # number_of_commits = len(commit_author)  # commitok száma


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/result', methods=['POST', 'GET'])
def result():
    output = request.form.to_dict()
    name = output["api_link"].split('/')
    cpa_list = []

    # issue_id = []  # issuek id-jének tömbje
    # issue_assignees = []  # issue-hoz rendelt fejlesztők adatai
    # bubble layout

    commit_author = []  # commitok szerzőinek a neve

    # issues = requests.get(f"https://api.github.com/repos/{name[-2]}/{name[-1]}/issues").json()
    commits = requests.get(f"https://api.github.com/repos/{name[-2]}/{name[-1]}/commits").json()

    for commit in commits:
        commit_author.append(commit["commit"]["author"]["name"])

    commits_per_author = {i: commit_author.count(i) for i in
                          commit_author}  # commitok szerzőinek a neve és commitjainak száma

    for kulcs, ertek in commits_per_author.items():
        cpa_list.append(dict(Name=kulcs,Szam=ertek))


    # for issue in issues:  # issuek id-jének és a hozzárendelt hallgatók lekérése
    #         issue_id.append(issue["id"])
    #         issue_assignees.append(issue["assignees"])

    # adatb(name)
    # g.V().hasLabel('student').properties().key().dedup() #a "name" adattagot írja ki
    # g.V().hasLabel('student').values().dedup() #neveket írja ki

    json_object = json.dumps(cpa_list, indent=4)

    # Writing to sample.json
    with open("sample.json", "w", encoding="utf8") as outfile:
        outfile.write(json_object)

    return render_template("goofy.html")


if __name__ == '__main__':
    app.run()
