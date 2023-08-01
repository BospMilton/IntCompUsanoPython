def week():
    dsc = {'Mon':'Monday',
        'Tue':'Tuesday',
        'Thu':'Thursday',
        'Sat':'Saturday',
        'Sun':'Sunday'}
    while True:
        week = input('Enter a day of the week: ')
        if week in dsc:
            print(dsc[week])
        elif week == '':
            break
