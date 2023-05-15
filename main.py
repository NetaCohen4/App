from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

import cv2

class MainApp(App):
    def build(self):
        self.icon = "icon1.jpg"


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    app = MainApp()
    app.run()


def play_movie(filename):
    # Open the video file
    cap = cv2.VideoCapture(filename)

    # Check if the video file opened successfully
    if not cap.isOpened():
        print("Error opening video file")
        return

    # Read and display frames until the video ends or the user quits
    while cap.isOpened():
        # Read a frame from the video file
        ret, frame = cap.read()

        if ret:
            # Display the frame in a window named "Movie Player"
            cv2.imshow("Movie Player", frame)

            # Exit if the 'q' key is pressed
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        else:
            break

    # Release the video capture object and close the window
    cap.release()
    cv2.destroyAllWindows()

# Specify the filename of the movie
movie_filename = "path/to/your/movie/file.mp4"

# Call the play_movie function with the specified filename
play_movie(movie_filename)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
