import PySimpleGUI as sg


def window_layout():
    """ Layout for the GUI window. """
    positive_spin_values = [i for i in range(101)]
    negative_spin_values = [-i for i in range(101)]
    negative_spin_values.reverse()
    layout = [
        [sg.Text('Winning %'), sg.Spin(values=positive_spin_values, initial_value=60, key='winning_percentage', size=(5, 1)),
         sg.Radio('long', 'RADIO1', default=True, key='long'),
         sg.Radio('short', 'RADIO1', key='short'),
         sg.Button('Calculate', bind_return_key=True)],
        [sg.Text('Risk %'), sg.Spin(values=negative_spin_values, initial_value=-3, key='risk_percentage', size=(5, 1)),
         sg.Text('Reward %'), sg.Spin(values=positive_spin_values, initial_value=15, key='reward_percentage', size=(5, 1)),
         sg.Text('Average risk %'), sg.Text('', key='average_risk_percentage', size=(6, 1))],
        [sg.Text('Entry'), sg.InputText(key='entry', size=(5, 1)),
         sg.Text('TP'), sg.Text(key='TP', size=(6, 1)),
         sg.Text('SL'), sg.Text(key='SL', size=(6, 1)),
         sg.Text('STAT QUO'), sg.Text(key='STAT_QUO', size=(6, 1))],
        [sg.Exit()]
    ]
    return layout


def main():
    # Initializes the window with PySimpleGUI.
    window = sg.Window('MEGA CALCULATOR 3000', window_layout())
    while True:
        event, values = window.Read()
        TP = 0
        SL = 0
        STAT_QUO = 0
        if event not in (None, 'Exit'):
            try:
                winning_percentage, risk_percentage, reward_percentage, entry = float(values['winning_percentage']), \
                                                                                float(values['risk_percentage']), \
                                                                                float(values['reward_percentage']), \
                                                                                float(values['entry'])
                average_risk = ((100 - winning_percentage) * risk_percentage + winning_percentage * reward_percentage) / 100
                if window.FindElement('short').Get():
                    TP = (entry * (100 - reward_percentage)) / 100
                    SL = (entry * (100 - risk_percentage)) / 100
                    STAT_QUO = (entry * (100 - average_risk)) / 100
                if window.FindElement('long').Get():
                    TP = (entry * (100 + reward_percentage)) / 100
                    SL = (entry * (100 + risk_percentage)) / 100
                    STAT_QUO = (entry * (100 + average_risk)) / 100
            except (TypeError, ValueError):
                average_risk = 'N/A'
                TP = 'N/A'
                SL = 'N/A'
                STAT_QUO = 'N/A'

            window.FindElement('average_risk_percentage').Update(average_risk)
            window.FindElement('TP').Update(f"{TP:.2f}")
            window.FindElement('SL').Update(f"{SL:.2f}")
            window.FindElement('STAT_QUO').Update(f"{STAT_QUO:.2f}")
        else:
            break


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
