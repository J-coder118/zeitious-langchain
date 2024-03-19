import csv

# Define the data for the CSV file
data = [
    {
        "name": "CTA_1",
        "example": "The Top Hack Business Owners and Career Professionals Use To Reinvent Themselves So That They Are Recognized Not Just For Their Achievements Or Title But For Who They Are— Their Ideas, Their Character, Their Unique Perspective",
        "focus": "",
    },
    {
        "name": "CTA_2",
        "example": "Even if they feel like they are barely keeping up",
        "focus": "",
    },
    {
        "name": "VIDEO_CTA",
        "example": """In This ONE DAY LIVE ONLINE Challenge You Will Learn:

STEP 1: The step by step game plan our clients use to create FREELY and bring their ideas to life without fear or restrictions because they are finissshheeeddd with just going through the motions, hiding their brilliance or feeling stagnant.

STEP 2: How you can create genuine, deep connections with people— relationships where you share your true thoughts and feelings, and they can do the same. Even if you have held yourself back because of people’s opinions for years.

Step 3: The 2-3 small tweaks you can make to how you think and operate at work, and at home that can allow you to reconnect with a deep sense of purpose, and passion, in things that deeply matter to you within the next one month… even if you have been buried in busyness for months.

Step 4: How to stop constantly chasing deadlines and finally have the most important things FIRST in your life. Your faith. Your family. Your impact. Your fun. Your money. 

Step 5: The real reason why you feel so frustrated when people congratulate you and then tell you to “settle down” because of your achievements when you know deep down that there is more — AND what you can do to let go of their expectations and start creating at the level you envision for yourself TODAY…

Step 6: AND…. how to do all of this while feeling that buzz of excitement about what you are doing with your time and without compromising on your values; or needing to ditch your achievements/pretend to be struggling when you are not. We know you are already winning. Show up with your full chest!""",
        "focus": "",
    },
    {
        "name": "VAR_3",
        "example": """[author_name] is recognized as one of the leading voices in the personal development space, exemplified by her selection as 1 of 50 women for the SUCCESS Magazine’s 2023 Women of Influence Awards. She is also the CEO of the 74th fastest-growing company in Canada and the creator of the Diamond Effect™ Neuroscience System.

She has trained over 50,000+ business owners and career professionals in how to use the power of neuroscience to master themselves, unlock their full potential, and confidently step into new realms of success and fulfillment.

She has helped clients increase their net worth by tens of millions of dollars, pay off millions of dollars worth of debt and do this without living on rice and beans. Using the principles she teaches, [author_name] went from being stuck in tens of thousands of debt, having no food for her family to 11 streams of income, multiple real estate properties and running a company that does multiple seven figures a year - In the span of FOUR years. It's your turn!""",
        "focus": "",
    },
]

# Specify the CSV file name
csv_file_name = "input.csv"

# Write the data to the CSV file
with open(csv_file_name, mode="w", newline="") as csvfile:
    fieldnames = ["name", "example", "focus"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Write the header
    writer.writeheader()

    # Write the rows
    for row in data:
        writer.writerow(row)
