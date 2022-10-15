import turtle
import pandas
import easygui

def main():
    screen = turtle.Screen()
    screen.title("U.S. States Game")

    shape = "blank_states_img.gif"
    screen.addshape(shape)
    turtle.shape(shape)
    turtle.tracer(0)

    data = pandas.read_csv("50_states.csv")
    state_li = data.state.to_list()

    score = 0
    turts = []
    known_states = []
    
    on = True
    while on:
        answer_state = screen.textinput(title=f"{score}/50 states correct", prompt="Name a state:").title()

        if score == 50:
            easygui.msgbox(msg="Congratulations!", title='U.S. states game')
            break

        if answer_state == 'Exit':
            break

        if answer_state in state_li:
            turts.append(turtle.Turtle())
            known_states.append(answer_state)
            turts[score].penup()

            x = int(data[data.state == answer_state]['x'])
            y = int(data[data.state == answer_state]['y'])
            turts[score].goto(x,y)

            turts[score].write(answer_state, move=False, align='center', font=('Courier', 6, 'normal'))
            score += 1

    states_to_learn = [str(x) for x in state_li if x not in known_states]
    pandas.DataFrame(states_to_learn).to_csv('states_to_learn.csv')\

    
    screen.exitonclick()

if __name__ == '__main__':
    main()