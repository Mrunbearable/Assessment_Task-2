#----Modules----#
import pandas as pd
import matplotlib.pyplot as plt

#----Global Variables----#
quit = False

#----Setup dataframe and query it here prior to creating visualisation and UI functions----#
original_df = pd.read_csv('Time-Wasters_on_Social_Media.csv')


social_media_df = pd.read_csv('Time-Wasters_on_Social_Media.csv')

#----Define Functions Below----#
def showOriginalData():
    print(original_df)

def showUpdatedData():
    print(social_media_df)

def showCharts():
    social_media_df.plot(
                        kind='scatter',
                        x='Age',
                        y='Addiction Level',
                        color='blue',
                        alpha=0.5,
                        title='The Connection Type and Addiction Level of user')
    plt.show()

def userOptions():
    global quit

    print("""Welcome to the Social Media Extraordinaire!
          
    Please select an option:
    1 - Show the original dataset
    2 - Show the updated Data Frame
    3 - Visualise the information of a User
    4 - Quit Program
        """)
    
    try:
        choice = int(input('Enter Selection: '))

        if choice == 1:
            showOriginalData()
        elif choice == 2:
            showUpdatedData()
        elif choice == 3:
            showCharts()
        elif choice == 4:
            quit = True
        else:
            print('A number between 1 and 4, come on!')

    except:
        print('Enter a number, it is not that hard.')

   

#----Main program----#
while not quit:
    userOptions()