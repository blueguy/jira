"""
https://jira.readthedocs.io/en/master/examples.html

"""

from jira import JIRA
 
jira = JIRA(basic_auth=('<ID>', '<API_KEY>'), options={'server':'<SERVER_ADDRESS>'})
for p in jira.projects():
  try:
    issues = jira.search_issues('project=%s' % p)
  except:
    pass

  for issue in issues:
    print ('ticket-no=',issue)
    print ('Assignee=',issue.fields.assignee)
    print ('Status=',issue.fields.status.name)
    print ('Summary=',issue.fields.summary)

