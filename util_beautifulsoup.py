# Navigate through the siblings 
def navigate_siblings(header):
    # Check the next brother
    next_sibling = header.find_next_sibling()
    if next_sibling:
        print('Next sibling of first <h1> tag:', next_sibling)
    else:
        print('No next sibling found for the <h1> tag.')

    # Check the previous brother
    previous_sibling = header.find_previous_sibling()
    if previous_sibling:
        print('Previous sibling of first <h1> tag:', previous_sibling)
    else:
        print('No previous sibling found for the <h1> tag.')

