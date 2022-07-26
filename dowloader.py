from pytube import *


class Dowloader:

    def __int__(self):

        self.video_url = input("What is the video url ? : ")

        self.youtube_video = YouTube(self.video_url)

        self.youtube_video.register_on_progress_callback(self.dowload_progress)

        self.lowest_res = self.youtube_video.streams.get_lowest_resolution().resolution

        self.highest_res = self.youtube_video.streams.get_highest_resolution().resolution

        self.title = self.youtube_video.title

        self.file_type = input("Select the file type [video/audio] : ")

        if self.file_type == "video":

            self.file_res = input("Select the video resolution [ 720p, 480p, 360p] : ")
        else:

            pass

        self.question = "Are you sure you want to download this video : "

    def downloading(self):

        for stream in self.youtube_video.streams.fmt_streams:

            if stream.is_progressive:

                if stream.type == self.file_type:

                    if stream.resolution == self.file_res:

                        if stream.mime_type == "video/mp4":

                            print("THIS IS THE VIDEO NAME , : ", self.title)

                            self.quest = input(self.question)

                            if self.quest == "yes":

                                print("", stream)

                                self.itag = input("Select an itag from the streams : ")

                                print("Downloading ...")

                                self.youtube_video.streams.get_by_itag(int(self.itag)).download()

                                print("End of download , enjoy your download")

                            else:

                                print("THANK")


    def dowload_progress(self, stream, chunk, bytes_remaining):

        bytes_downloaded = stream.filesize - bytes_remaining

        percent = bytes_downloaded * 100 / stream.filesize

        print(f"Download progression : {int(percent)}%")

    def dowloading_video(self):

        pass
