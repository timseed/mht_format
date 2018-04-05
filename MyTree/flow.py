from anytree import Node, RenderTree

master_flow = [('OT_FTP', 'OT_PROCESS', 'LD_HBASE'),
               ('OT_FTP', 'OT_PROCESS', 'FILTER', 'LD_ES'),
               ('NW_FTP', 'NW_PROCESS', 'LD_HBASE'),
               ('NW_FTP', 'NW_PROCESS', 'LD_ES'),
               ('INT_FTP', 'INT_PROCESS', 'FILTER', 'LD_ES'),
               ('INT_FTP', 'INT_PROCESS', 'LD_HBASE'),
               ('OT_CRM_FTP', 'OT_PREPAID'),
               ('OT_CRM_FTP', 'OT_POSTPAID'),
               ('OT_CRM_FTP', 'OT_FENDI'),
               ('OT_CRM_FTP', 'OT_VSAT'),
               ('NW_CRM_FTP', 'NW_CRM'),
               ('SHAMSA','LEAVE','DRIVE','AMARAT'),
               ('Barakat','walk','stc','drink','coffee','now'),
               ('Barakat','run','gbm','programs'),
               ('tim','sleeps','soundly'),
               ('tim','sleeps','process','load1','load2','load4'),
               ('tim','sleeps','process2','load3','load2','load4'),
               ('tim','sleeps','badly')
               ]
##################

flows = []
first=[]
jobs=[]
#Link Master Jobs to the main job
for r in range(len(master_flow)):
    first.append(master_flow[r][0])
    for i in range(0, len(master_flow[r]) - 1):
        flows.append([master_flow[r][i], master_flow[r][i + 1]])
        jobs.append(master_flow[r][i])

jobs=list(set(jobs))
job_nodes={}

#Make the 1st Level Nodes Unique
result =[]
for a in flows:
    if a not in result:
        result.append(a)
flows=result

start=Node("Start")
for j in list(set(first)):
    print("{}->{}".format("Start",j))
    n=Node(j,parent=start,)
    job_nodes[j]=n

for pair in flows:
    from_job=pair[0]
    to_job=pair[1]
    if from_job in job_nodes:
        from_node=Node(to_job,job_nodes[from_job])
        job_nodes[to_job]=from_node
    else:
        print("Job {} has not been created".format(pair[0]))

from anytree.exporter import JsonExporter
exporter = JsonExporter(indent=2, sort_keys=False)
with open("web/flow.json","w") as ofile:
    ofile.write("{}".format(exporter.export(start)))

print("Please open web/t11.html ") 
