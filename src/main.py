import re
D = 0.85
PAGE_INPUTS = []
PAGE_ARRAY = []
class Page:
    def __init__(self, name):
        self.name = name
        self.outbound_pages = []
        self.inbound_pages = []
        self.PageRank = 1

    def calculate_pagerank(self):
        series_sum = 0
        for inbound_page in self.inbound_pages:
            series_sum += (inbound_page.PageRank / len(inbound_page.outbound_pages))
        self.PageRank = (1 - D) + D * (series_sum)

def find_page_input_from_name(name):
    for page_input in PAGE_INPUTS:
        if page_input.split(":")[0] == name:
            return page_input
    raise Exception("Ensure that all pages and its relationships are defined")

def find_page_from_name(name):
    for page in PAGE_ARRAY:
        if name == page.name:
            return page
    raise Exception("Ensure that all pages and its relationships are defined")


print("Please enter your link relations below in the format page1:page2,page3 where page1 has outbound links to page2 and page3:\n")
page_inputs = []
while True:
    inp = input("")
    if inp == "exit":
        break
    if not re.match(r'^[A-Za-z]+:([A-Za-z]+,)*[A-Za-z]*$', inp):
        print("Invalid input format. Please use the format 'A:B,C,'")
        continue
    page_inputs.append(inp.strip())
    
PAGE_INPUTS = page_inputs
PAGE_ARRAY = [Page(page_input.split(":")[0]) for page_input in PAGE_INPUTS]

for page in PAGE_ARRAY:
    page_input = find_page_input_from_name(page.name)
    outbounds = page_input.split(":")[1].split(",")
    unique_outbounds = []
    for outbound in outbounds:
        if outbound not in unique_outbounds and outbound != page.name and outbound != "":
            unique_outbounds.append(outbound)
    for outbound in unique_outbounds:
        outbound_page = find_page_from_name(outbound)
        if outbound_page:
            page.outbound_pages.append(outbound_page)
            outbound_page.inbound_pages.append(page)

iterations_to_run = int(input("Enter Number of iterations to run: "))
for current_iteration in range(1, iterations_to_run + 1):
    print(f"\nIteration {current_iteration}: \n")
    for page in PAGE_ARRAY:
        page.calculate_pagerank()
        print(f"PageRank of {page.name}: {page.PageRank:.2f}")
        
print("------------FINAL RESULT--------------"+"Initial Problem:\n"+str(PAGE_INPUTS)+"Final Result:\n")
for page in PAGE_ARRAY:
    print(f"PageRank of {page.name}: {page.PageRank:.2f}")
