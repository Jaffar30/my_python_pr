import turtle 
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "us_states_game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
answer_marker = turtle.Turtle()
answer_marker.hideturtle()
answer_marker.penup()
# to get the coordinates of mouse clicks
# def get_mouse_click_coor(x, y):
#     print(x, y)   
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

data = pandas.read_csv("us_states_game/50_states.csv")
total = data.state.count()
count = 0
while data.state.count() > 0:
    answer_state = screen.textinput(title=f"{count}/{total}", prompt="What's another state's name?").title()
    state = data[data.state == answer_state]
    if state is not None and not state.empty:
        count += 1
        state_x = state.x.item()
        state_y = state.y.item()
        answer_marker.goto(state_x, state_y)
        answer_marker.write(answer_state)
        data.drop(state.index, inplace=True)
 
turtle.mainloop()