from bs4 import BeautifulSoup

def extract_hrefs_from_html(file_path):
    """
    Extract all href attributes from an HTML file.
    
    Args:
        file_path (str): Path to the HTML file
        
    Returns:
        list: List of href values found in the file
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()
    
    soup = BeautifulSoup(html_content, 'html.parser')
    hrefs = []
    
    # Find all elements with href attribute
    for element in soup.find_all(href=True):
        hrefs.append(element['href'])
    
    return hrefs

# Usage example
if __name__ == "__main__":
    hrefs = extract_hrefs_from_html('blog.html')
    for i, href in enumerate(hrefs, 1):
        print(f"{href}")
