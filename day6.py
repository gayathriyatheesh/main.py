playlist = list(map(int, input("Enter song durations separated by space: ").split()))

if any(duration <= 0 for duration in playlist):
    print("Invalid Playlist: Contains non-positive duration.")
else:
    total_duration = sum(playlist)
    number_of_songs = len(playlist)

    if number_of_songs % 9 == 0:
        category = "Premium Structured Playlist"
        recommendation = "Highly organized listening pattern"

    if total_duration < 300:
        category = "Too Short Playlist"
        recommendation = "Add more songs"

    elif total_duration > 3600:
        category = "Too Long Playlist"
        recommendation = "Consider shortening the playlist"

    elif any(playlist.count(song) > 1 for song in playlist):
        category = "Repetitive Playlist"
        recommendation = "Add variety"

    elif total_duration >= 300 and total_duration <= 3600 and len(set(playlist)) == number_of_songs:
        category = "Balanced Playlist"
        recommendation = "Good listening session"

    else:
        category = "Irregular Playlist"
        recommendation = "Adjust playlist for better balance"

    print("Total Duration:", total_duration, "seconds")
    print("Songs:", number_of_songs)
    print("Category:", category)
    print("Recommendation:", recommendation)