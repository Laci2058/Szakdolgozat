from flask import Flask, render_template, request
import requests
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection
from gremlin_python.process.anonymous_traversal import traversal

app = Flask(__name__)


@app.route('/')
def index():
    g = traversal().with_remote(DriverRemoteConnection('ws://localhost:8182/gremlin', 'g'))
    """ issue_url = f"https://api.github.com/repos/CsharptutorialHungary/egyetemikurzus-2022/issues"
     all_issue = requests.get(issue_url).json()
     commit_url = f"https://api.github.com/repos/CsharptutorialHungary/egyetemikurzus-2022/commits"
     all_commit = requests.get(commit_url).json()

     issue_id = []  # issuek id-jének tömbje
     issue_assignees = []  # issue-hoz rendelt fejlesztők adatai
     commit_author = []  # commitok szerzőinek a neve

     for issue in all_issue:  # issuek id-jének és a hozzárendelt hallgatók lekérése
         issue_id.append(issue["id"])
         issue_assignees.append(issue["assignees"])

     for commit in all_commit:
         commit_author.append(commit["commit"]["author"]["name"])

     commits_per_author = {i: commit_author.count(i) for i in
                           commit_author}  # commitok szerzőinek a neve és commitjainak száma

     number_of_issues = len(issue_id)  # issuek száma
     number_of_commits = len(commit_author)  # commitok száma """

    return render_template("index.html")


@app.route('/result', methods=['POST', 'GET'])
def result():
    output = request.form.to_dict()
    name = output["api_link"].split('/')

    all_issue = requests.get(f"https://api.github.com/repos/{name[-2]}/{name[-1]}/issues").json()
    all_commit = requests.get(f"https://api.github.com/repos/{name[-2]}/{name[-1]}/commits").json()

    return render_template("index.html")


if __name__ == '__main__':
    app.run()
