import math
import timeit
from sorting import *

class Song:
    def __init__(self, track_id, song_id, title, band):
        self.track_id = track_id
        self.song_id = song_id
        self.title = title
        self.band = band
    
    # Compares the song between twp
    def __lt__(self, other):
        other: Song
        if self.band < other.band:
            return True
        
        return False;

    def __str__(self):
        return f"{self.title} - {self.band}"



def main():
    
    lines  = []
    songs = list()
    

    print("Reading lines in file...")
    with open("unique_tracks.txt") as file:
        lines = [line.rstrip() for line in file];
    print("Done!")
    
    print ("Creating objects...")
    for line in lines:
        refined_line = line.split("<SEP>")
        songs.append(Song(refined_line[0], refined_line[1], refined_line[3], refined_line[2]))
    print ("Done!")


    #search_test(songs, 250000, songs[10000].band)
    #search_test(songs, 500000, songs[20000].band)
    #search_test(songs, 1000000, songs[40000].band)

    sorting_test(songs, 1000)
    sorting_test(songs, 10000)
    #sorting_test(songs, 100000)
    #sorting_test(songs, 1000000)

    
    

# This function tries a search with with a spliced list to element n
# and handles output
def search_test(list, n, target):
    print("n =", n)
    spliced_list = list[0:n]
    hashtable = dict()
    for element in list:
        hashtable[element.band] = element.title
    
    sorted_songs = sorted(spliced_list, key=lambda x: x.band, reverse= False)
    # man hade kunnat använda sig av __lt__ här men explicit är bättre än implicit...


    linear_time = timeit.timeit(stmt = lambda: linear_search(spliced_list, target), number=10000)
    bin_time = timeit.timeit(stmt= lambda: bin_search(sorted_songs, target), number=10000)
    hash_time = timeit.timeit(stmt= lambda: hash_search(hashtable, target), number=10000)

    print("Linear search took", round(linear_time, 4), "seconds")
    print("Binary search took", round(bin_time, 4), "seconds")
    print("Hash search took", round(hash_time, 4),"seconds\n\n")


def linear_search(list, target):
    for i in range(len(list)):
        if list[i].band == target:
            return i, list[i].title;
    raise Exception("No artist found")


# Algorithm is built upon the logic from english Wiki page
def bin_search(list, target):
    L = 0
    R = len(list)-1

    while L<R:
        index = math.floor((L+R)/2)
        if list[index] < Song(None, None, None, target): # This is in order to use __lt__. It could be implemented in another way.
            L = index+1
        elif list[index] > Song(None, None, None, target):
            R = index-1
        else:
            return index, list[index].title 

    raise Exception("No artist found")

def hash_search(hashtable, target):
    return hashtable[target]
    

if __name__ == "__main__":
    main()


#
# KOMMENTAR OCH ANALYS
#
# Resultatet finnes i table.csv. Vi ser att linjärsökningen
# var linjär, men i sista fallet fann den troligtvis en
# en låt som var från samma artist fast tidigare. Det syns
# att sökningen i hashtabellen är av konstant tidskomplexitet.
# Binärsökningen är också avsevärt snabare än linjär vilket den
# ska vara (O(log n)).
#
# Vid sorteringen kunde man se att tidskomplexiteten hos Bubble
# sort var kvadratisk, vilket överensstämmer med teorin.
# Quick Sort var något långsammare än linjär vilket överensstämmer
# med dess teoretiska tidskomplexitet O(n log(n)).
# Vi körde inte n=100 000 och n=1 000 000 på Bubble Sort
# eftersom det skulle ta cirka 10 000 s och 1 000 000 s.