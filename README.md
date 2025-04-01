## Parsed article links from wiz.io academy blog

1. Load the page of https://wiz.io/academy to the most bottom article.
2. Save the page to an blog.html file
3. Run the python script in the same directory with blog.html and pipe the output into the page_links.txt as following : `python3 solution.py > page_links.txt`
4. Run the `grep -Eo 'https://www\.wiz\.io/academy/[^ ]*' page_links.txt | uniq > result.txt` to filter article links into result.txt file
