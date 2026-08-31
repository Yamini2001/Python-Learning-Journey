#  Movie Night Playlist
playlist = ["Inception","Interstellar","The Matrix"]
name_of_movie = str(input("Enter the name of the movie: "))
if(name_of_movie in playlist):
    print("Already added!")
else:
    playlist.append(name_of_movie)
playlist.sort()
print(playlist)