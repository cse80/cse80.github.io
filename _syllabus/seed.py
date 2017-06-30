#!/usr/bin/env python3

import arrow

template = """---
week: {week}
dates: {lecDate}
homeworkRelease: {hwDate} PDT
solutionRelease: {solDate} PDT
title: "{title}"
# lectureTopics:
#   - TBD
# homeworkTopics:
#   - TBD
# advancedTopics:
#   - TBD
lectureSummary:
---
"""

startDate = '07/03/2017'

lectures = [
    'Introduction, Setup, and History',
    'Shells and Editors',
    'Pipelining, Regex, and Scripting',
    'Git',
    'Everything is a File',
    'Quiz & Office Hours++',
    'Permissions, Compression, Env, and Binaries',
    'Productivity in the Terminal',
    'How to Fix Problems',
    'System Administration',
]

curLecDate = arrow.get(startDate, 'MM/DD/YYYY')
for idx, lecture in enumerate(lectures):
    with open('su17/week{0:02d}.md'.format(idx + 1), 'w') as f:
        lecDate = curLecDate
        hwDate  = lecDate.replace(hours=12)
        solDate = hwDate.shift(days=2, hours=-2)

        dayofweek = curLecDate.weekday()
        if dayofweek == 0: # Monday
            curLecDate = curLecDate.shift(days=2)
        elif dayofweek == 2: # Wednesday
            curLecDate = curLecDate.shift(days=5)

        weekData = template.format(
            lecDate= lecDate.format('MM/DD/YYYY'),
            hwDate= hwDate.format('YYYY-MM-DD HH:mm:ss'),
            solDate= solDate.format('YYYY-MM-DD HH:mm:ss'),
            title= lecture,
            week= idx + 1,
        )

        f.write(weekData)
