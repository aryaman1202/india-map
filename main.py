import turtle
import pandas
s = turtle.Screen()
t = turtle.Turtle()
s.bgcolor("black")
s.title("Indian States Game")
image = "python work/python-shape-by-turtle/India-map/india-map.gif"
s.addshape(image)
t.shape(image)

data = pandas.read_csv(
    "python work/python-shape-by-turtle/India-map/states.csv")
all_states = data.States.to_list()
guessed_state = []

while len(guessed_state) < 50:

    # def get_mouse_click_coor(x, y):
    #     print(x, y)

    # turtle.onscreenclick(get_mouse_click_coor)
    # turtle.mainloop()
    # s.exitonclick()

    answer_state = s.textinput(title=f"{len(guessed_state)}/29 States correct",
                               prompt="What's another state's name").title()

    if answer_state == "Exit":
        missing_states = [
            state for state in all_states if state not in guessed_state]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv(
            "python work/python-shape-by-turtle/India-map/states-to-learn.csv")
        break
    if answer_state in all_states:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.States == answer_state]
        t.goto(float(state_data.x), float(state_data.y))
        t.write(state_data.States.item())
    print(answer_state)
