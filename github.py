import requests
def get_issue_title(owner,repo,issue):
  html = requests.get("https://api.github.com/repos/{}/{}/issues/{}".format(owner,repo,str(issue))).content
  return eval(html.decode().replace("false","False").replace("true","True").replace("null","None"))["title"]
get_issue_title("TechDudie","TechTest",12)
