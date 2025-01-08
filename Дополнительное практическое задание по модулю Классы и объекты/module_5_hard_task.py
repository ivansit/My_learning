from time import sleep


class User:
    """ Class User with attr: nickname, password, age """
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age


class Video:
    """ Class Video with attr: title, duration, time_now, adult_mode """
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:
    """ Class UrTube with attr: users, videos, current_user. Methods: login, logout, register, add video, get videos, watch video """
    def __init__(self, users = [], videos = [], current_user = None):
        self.users = users
        self.videos = videos
        self.current_user = current_user

    def log_in(self, nickname, password):
        for i in self.users:
            if nickname in i and password in i:
                self.current_user = nickname

    def log_out(self):
        self.current_user = None

    def register(self, nickname, password, age):
        flag = True
        for i in self.users:
            if nickname.__eq__(i[0]):
                print(f'User {nickname} already exist')
                flag = False
                break

        if flag.__eq__(True):
            new_user = User(nickname, password, age)

            self.nickname = new_user.nickname
            self.password = new_user.password
            self.age = new_user.age

            info = [self.nickname, self.password, self.age]

            self.users.append(info)
            self.current_user = self.nickname

    def add(self, *args):
        video_list = [*args]
        for i in video_list:
            if isinstance(i, Video):
                title = i.title
                if title in self.videos:
                    continue
                else:
                    self.videos.append(i)

    def get_videos(self, search_word):
        video_list = []
        for i in self.videos:
            if isinstance(i, Video):
                title = i.title
                if search_word.upper() in title.upper():
                    video_list.append(title)

            else:
                continue
        return video_list

    def watch_video(self, video_name):
        flag = False
        age = 0
        for i in self.users:
            if self.current_user.__eq__(i[0]):
                age = i[2]
                flag = True
            else:
                flag = False

        if flag.__eq__(True):
            for i in self.videos:
                if isinstance(i, Video):
                    title = i.title
                    if video_name.__eq__(title):
                        if i.adult_mode and age.__lt__(18):
                            print('You are under 18 years old, please leave the page')
                            break
                        else:
                            for j in range(1, i.duration + 1):
                                sleep(1)
                                if j.__eq__(i.duration)
                                    print(f'{j} End of video')
                                else:
                                    print(j, end= ' ')
                            i.duration = 0
                else:
                    continue
        else:
            print('Login to your account to watch the video')


if __name__ == '__main__':
    ur = UrTube
    v1 = Video('Best programming language 2024!', 200)
    v2 = Video('Why do girls want a programmer guy?', 10, adult_mode=True)

    # Adding video
    ur.add(v1, v2)

    # Checking the search
    print(ur.get_videos('best'))
    print(ur.get_videos('PROG'))

    # User login verification and age restriction checking
    ur.watch_video('Why do girls a programmer guy?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Why do girls a programmer guy?')
    ur.register('urban_pythonist','iScX4vIJClb9YQavjAgF',25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Checking account login
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Trying to play a non-existent video
    ur.watch_video('Best programming language 2024!')












