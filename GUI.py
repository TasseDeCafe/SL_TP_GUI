import PySimpleGUI as sg

def window_layout():
    """ Layout for the GUI window. """
    layout = [
        [sg.Text('Winning %'), sg.InputText(key='winning_percentage', size=(5, 1)),
         sg.Radio('long', 'RADIO1', default=True, key='long'),
         sg.Radio('short', 'RADIO1', key='short'),
         sg.Button('Calculate', bind_return_key=True)],
        [sg.Text('Risk %'), sg.InputText(key='risk_percentage', size=(5, 1)),
         sg.Text('Reward %'), sg.InputText(key='reward_percentage', size=(5, 1)),
         sg.Text('Average risk %'), sg.Text('', key='average_risk_percentage', size=(5, 1))],
        [sg.Text('Entry'), sg.InputText(key='entry', size=(5, 1)),
         sg.Text('TP'), sg.Text(key='TP', size=(5, 1)),
         sg.Text('SL'), sg.Text(key='SL', size=(5, 1)),
         sg.Text('STAT QUO'), sg.Text(key='STAT_QUO', size=(5, 1))],
        [sg.Exit()]
    ]
    return layout

def main():
    window = sg.Window('MEGA CALCULATOR 3000', window_layout())
    while True:
        # Initializes the window with PySimpleGUI.
        event, values = window.Read()
        average_risk = 0
        TP = 0
        SL = 0
        STAT_QUO = 0
        winning_percentage, risk_percentage, reward_percentage, entry = float(values['winning_percentage']), \
                                                                        float(values['risk_percentage']), \
                                                                        float(values['reward_percentage']), \
                                                                        float(values['entry'])
        if event not in (None, 'Exit'):
            try:
                average_risk = ((100 - winning_percentage) * risk_percentage \
                               + winning_percentage * reward_percentage) / 100
                if window.FindElement('short').Get():
                    TP = (entry * (100 - reward_percentage)) / 100
                    SL = (entry * (100 - risk_percentage)) / 100
                    STAT_QUO = (entry * (100 - average_risk)) / 100
                if window.FindElement('long').Get():
                    TP = (entry * (100 + reward_percentage)) / 100
                    SL = (entry * (100 + risk_percentage)) / 100
                    STAT_QUO = (entry * (100 + average_risk)) / 100
            except:
                pass
                # average_risk = 'Invalid'

            window.FindElement('average_risk_percentage').Update(average_risk)
            window.FindElement('TP').Update(TP)
            window.FindElement('SL').Update(SL)
            window.FindElement('STAT_QUO').Update(STAT_QUO)
        else:
            break


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()