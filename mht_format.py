
import email
import email.message
import sys
import glob
import bs4



def extract_html(file):
    with open(file,'r') as ifp:
        data=ifp.read()
        ifp.close()
    soup=bs4.BeautifulSoup(data,"lxml")

    #When debugging this is very useful
    #print(''+soup.prettify())
    #
    letters = soup.find_all("div", id="slide_description")
    rv=""
    for element in letters:
        parts=element.get_text().split(':')
        rv=rv+str.format('## {} \n\n {} \n\n ',parts[0].strip(),parts[1].strip())
    return rv




images=[]
htmlfiles=[]
ifp=open(sys.argv[1],'r')
data=ifp.read()
ifp.close()

em=email.message_from_string(data)

print("These are the parts of the mht file")
for p in em.get_payload():
    ct = p.get_content_type()
    fp = p.get("content-location") or "index.html"
    print("Writing %s to %s, %d bytes...\n" % (ct, fp, len(p.get_payload())))
    open(fp, "wb").write(p.get_payload(decode=True))


for file in glob.glob("*.jpeg"):
    images.append(file)


for file in glob.glob("slide*.htm"):
    htmlfiles.append(file)

if len(htmlfiles)>0:
    ofp=open("Topic.md","w")
    ofp.write("# Training Subject\n\n")
    for i in range(len(htmlfiles)):
        tv=extract_html(htmlfiles[i])
        ofp.write(str.format("{}\n\n![Image]({})\n\n",tv,images[i]))

    ofp.close()
else:
    print("I did not get the expected number of extracted files")