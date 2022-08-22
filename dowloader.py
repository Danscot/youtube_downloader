from pytube import *


class Downloader:

    def __int__(self):

        print("""                 _____                                         _              _____                               _                       _
                |  __ \                                       | |            |  __ \                             | |                     | |              
                | |  | |   __ _   _ __    ___    ___    ___   | |_   ______  | |  | |   ___   __      __  _ __   | |   ___     __ _    __| |   ___   _ __ 
                | |  | |  / _` | | '_ \  / __|  / __|  / _ \  | __| |______| | |  | |  / _ \  \ \ /\ / / | '_ \  | |  / _ \   / _` |  / _` |  / _ \ | '__|
                | |__| | | (_| | | | | | \__ \ | (__  | (_) | | |_           | |__| | | (_) |  \ V  V /  | | | | | | | (_) | | (_| | | (_| | |  __/ | |   
                |_____/   \__,_| |_| |_| |___/  \___|  \___/   \__|          |_____/   \___/    \_/\_/   |_| |_| |_|  \___/   \__,_|  \__,_|  \___| |_|   """)

        print()

        self.url = input("Please enter the file url: ")

        self.youtube_video = YouTube(self.url)

        self.youtube_video.register_on_progress_callback(self.download_progress)

        self.format = ""

        self.type = ""

        self.itag = ""

        self.file_format = ""

    def download_progress(self, stream, chunk, bytes_remaining):

        bytes_downloaded = stream.filesize - bytes_remaining

        percent = bytes_downloaded * 100 / stream.filesize

        print(f"Download progression : {int(percent)}%")

    def downloading(self):

        print()

        self.num = input("[1]. Video download\n[2]. Audio download\n\nPlease select a number for your download type: ")

        print()

        if self.num == "1":

            self.video_infos()

            if self.question == "yes":

                self.youtube_video.streams.get_by_itag(int(self.itag)).download()
            else:

                print("THANKS")

        else:

            self.audio_infos()

            if self.question == "yes":

                self.youtube_video.streams.get_by_itag(int(self.itag)).download()

            else:

                print("THANKS")

    def video_downloader(self):

        for stream in self.youtube_video.streams.fmt_streams:

            if stream.is_progressive:

                if stream.mime_type == "video/mp4":

                    if stream.resolution == self.file_format:

                        if stream.type == self.type:

                            print(stream)

    def video_infos(self):

        self.type = "video"

        self.format = input("[1]. 720p\n[2]. 360p\n[3]. 480p\n\nPlease select the file format: ")

        if self.format == "1":

            self.file_format = "720p"

        elif self.format == "2":

            self.file_format = "360p"

        else:

            self.file_format = "480p"

        print()

        self.file_name = self.youtube_video.title

        print(f"The file name is: {self.file_name}")

        print()

        self.question = input("Are you sure you want to downloade this video ? [yes/no]: ")

        print()

        self.video_downloader()

        print()

        self.itag = input("Enter the itag for your download: ")

        print()

        print("Downloading ...")

    def audio_infos(self):

        self.type = "audio"

        self.format = input("[1]. 128kbps\n[2]. 48kbps\n\nPlease select the file format: ")

        if self.format == "1":

            self.file_format = "128kbps"

        elif self.format == "2":

            self.file_format = "48kbps"

        else:

            self.file_format = "64kbps"

        print()

        self.file_name = self.youtube_video.title

        print(f"The file name is: {self.file_name}")

        print()

        self.question = input("Are you sure you want to downloade this audio [yes/no] ? : ")

        print()

        self.audio_downloader()

        print()

        self.itag = input("Enter the itag for your download: ")

        print()

        print("Downloading ...")

    def audio_downloader(self):

        for stream in self.youtube_video.streams.fmt_streams:

            if stream.mime_type == "audio/mp4":

                if stream.abr == self.file_format:

                    if stream.type == self.type:

                        print(stream)















