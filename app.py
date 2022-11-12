from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    issue_url = f"https://api.github.com/repos/CsharptutorialHungary/egyetemikurzus-2022/issues"
    all_issue = requests.get(issue_url).json()
    commit_url = f"https://api.github.com/repos/CsharptutorialHungary/egyetemikurzus-2022/commits"
    all_commit = requests.get(commit_url).json()

    issue_id = []  # issuek id-jének tömbje
    issue_assignees = []  # issue-hoz rendelt fejlesztők adatai
    commit_author = []  # commitok szerzőinek a neve

    # commit_list = []

    for issue in all_issue:  # issuek id-jének és a hozzárendelt hallgatók lekérése
        issue_id.append(issue["id"])
        issue_assignees.append(issue["assignees"])

    for commit in all_commit:
        commit_author.append(commit["commit"]["author"]["name"])    # !!!!ellenőrizni hogy author nem null!!!!
    #   commit_list.append(commit["commit"]["author"])

    commits_per_author = {i: commit_author.count(i) for i in
                          commit_author}  # commitok szerzőinek a neve és commitjainak száma

    number_of_issues = len(issue_id)  # issuek száma
    number_of_commits = len(commit_author)  # commitok száma


    return all_commit # !!!!commitok száma nem pontos, mert üres author-ral is számolja!!!!


if __name__ == '__main__':
    app.run()
