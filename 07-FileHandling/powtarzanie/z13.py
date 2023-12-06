movie_title = ["IOG", "OMG", "If", "While", "Nevertheless"]
file=open("movies.txt", 'w')
for i in movie_title:
    file.write(i+"\n")
file.close()