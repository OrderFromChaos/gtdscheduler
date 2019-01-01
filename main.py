import os                         # Clearing display at exit
import curses                     # Interface library
from pages import numberSelectWithTitle # Subpages for CursesWrapper to render

### TODO: For text input, use curses.textpad
### TODO: Handle exceptions gracefully so as to not break terminal

class CursesWrapper:
    """
    This class keeps a consistent curses display state, and slots in
    screens to display from other functions.

    Attributes:
        screen:   the screen object from curses.initscr()
        metadata: keeps track of any temp data the subscreens need
    """

    def __init__(self):
        self.screen = curses.initscr()
        self.running = True      # Tracking state if needed later on

        # Configure curses
        curses.noecho()          # Curses outputs keys by default, which would be distracting
        curses.cbreak()          # Makes curses react to key presses instantly (no buffer)
        curses.curs_set(False)   # Hide cursor
        curses.start_color()     # Allows for color rendering
        self.screen.keypad(True) # Gracefully handles keys like Page Up
    
    def kill(self):
        # TODO: Make sure this gracefully works when subscreens are displayed.
        curses.endwin()
        self.running = False
        os.system('clear') # TODO: Is this necessary?

    def render(self,subscreen,page_options):
        """
        Renders an arbitrary subscreen, which represents individual pages of the interface.
        
        Subscreen should be a class that expects a dictionary for
            rendering instructions (hence page_options).
            It should also have a class.show(mainscreen) function.
        
        Returns whatever value class.show(mainscreen) spits out.
        """
        page = subscreen(page_options)
        returnval = page.show(self.screen)
        # self.kill() # TODO: Only here for short-term dev reasons
        return returnval

def main():
    m = CursesWrapper()

    ###################################################
    ###    MAIN PAGE (SELECTING GTDSCH FUNCTION)    ###
    ###################################################
    menu = {'title' : 'Todo List',
            'type' : 'menu',
            'subtitle' : 'What would you like to do?'}
    option_1 = {'title' : 'Capturing (task entry)',
                'subscreen': 'capturing'}
    option_2 = {'title' : 'Clarifying (drill down/add expected time)',
                'subscreen': 'clarifying'}
    option_3 = {'title' : 'Autoschedule',
                'subscreen': 'autoschedule'}

    menu['options'] = [option_1, option_2, option_3]

    next_subscreen = m.render(numberSelectWithTitle,menu)

    raise NotImplementedError

    if next_subscreen['title'] == option_1:
        ##################################
        ###    CAPTURING/TASK ENTRY    ###
        ##################################
        screen_options = {'save_each': True, # If true, will write to json for every task input.
                                             #  Else, wll save at end of capturing.
                          'show_old': True   # If true, will start task scrolldown with tasks
                                             #  most recently added to todo.json.
        } 
        _ = m.render(capturingTasks, screen_options)
    else:
        m.kill()
        raise NotImplementedError

if __name__ == "__main__": # If this file itself is run
    main()