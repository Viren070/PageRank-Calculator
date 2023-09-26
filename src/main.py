D = 0.85

class Page:
    def __init__(self, name):
        self.name = name
        self.outbound = []
        self.inbound = []
        self.PageRank = 1

    def calculate_pagerank(self):
        series_sum = 0
        for page in self.inbound:
            series_sum += (page.PageRank / len(page.outbound))
        self.PageRank = (1 - D) + D * (series_sum)

def find_page_input_from_name(name):
    for page_input in page_inputs:
        if page_input.split(":")[0] == name:
            return page_input
    raise Exception("Ensure that all pages and its relationships are defined")

def find_page_from_name(name):
    for page in page_array:
        if name == page.name:
            return page
    raise Exception("Ensure that all pages and its relationships are defined")


print("Please enter your link relations below in the format link1:link2,link3 where link1 has outbound links to link2 and link3\n\n")
page_inputs = []
while True:
    inp = input("")
    if inp == "exit":
        break
    page_inputs.append(inp.strip())

page_array = [Page(page_input.split(":")[0]) for page_input in page_inputs]

for page in page_array:
    page_input = find_page_input_from_name(page.name)
    outbounds = page_input.split(":")[1].split(",")
    
    # Remove duplicates and self-references
    unique_outbounds = []
    for outbound in outbounds:
        if outbound not in unique_outbounds and outbound != page.name and outbound != "":
            unique_outbounds.append(outbound)
    
    for outbound in unique_outbounds:
        outbound_page = find_page_from_name(outbound)
        if outbound_page:
            page.outbound.append(outbound_page)
            outbound_page.inbound.append(page)

iterations_to_run = int(input("Enter Number of iterations to run: "))
for current_iteration in range(1, iterations_to_run + 1):
    print(f"\nIteration {current_iteration}: \n")
    for page in page_array:
        page.calculate_pagerank()
        print(f"PageRank of {page.name}: {page.PageRank:.2f}")