from bs4 import BeautifulSoup
from accesError import accessError

class HtmlParser:
    def __init__(self,html) :
        self.soup = BeautifulSoup(html, 'html.parser')


    def get_page_words(self):
          return self.soup.find_all(["p","h1","h2","h3"])

    def get_image_tags(self):
         return self.soup.find_all("img")
    
    def get_missing_alt_text(self):
         return self.soup.find_all("img", attrs={"alt": False})

    def get_blank_alt_text(self):
         return self.soup.find_all("img", attrs={"alt": ""})
    
    def check_alt_text(self):
         out = []
         image_tags = self.get_image_tags()
         id_count = 0
         for image in image_tags:
              if(image['src'] == "" ):
                    out.append({"id":id_count,"type":"Alt text with no source","img":image["src"]})
                    id_count += 1
              elif(image.has_attr('alt') and (image['alt'] == "" or image['alt'] == " ")):
                    out.append({"id":id_count,"type":"Alt text blank, may be decorative","img":image["src"]})
                    id_count += 1
              elif(not(image.has_attr('alt'))):
                    out.append({"id":id_count,"type":"Alt attribute missing, maybe decorative","img":image["src"]})
                    id_count += 1

            
         return out