import json


def load_data():
    try:
        with open('videos.txt','r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data(video):
    with open('videos.txt', 'w') as file:
        json.dump(video,file)

def list_all_videos(video):
    for index, video in enumerate(video, start=1):
        print(f"{index}.")

    

def add_your_video(video):
    name = input("Enter your video name: ")
    time = input("Enter your video time: ")
    video.append({'name':name, 'time':time})
    save_data(video)

def update_your_video(video):
    pass

def delete_your_video(video):
    pass


def main():

    video =load_data()

    while True:
        print("\n Welcome to Video Manager | Please Choosee from the following")
        print("\n 1. List all Videos")
        print("\n 2. Add your Video")
        print("\n 3. Update Your Video")
        print("\n 4. Delete your video")
        print("\n 5. Exit The App")
        choice = input("Enter your choice:  ")
        print(video)

        match choice:
            case '1':
                list_all_videos(video)

            case '2':
                add_your_video(video)

            case '3':
                update_your_video(video)

            case '4':
                delete_your_video(video)
            case '5':
                break
            case _:
                print("Invalid Choice")

if __name__ == "__main__":
    main()