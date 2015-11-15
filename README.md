# factorial_bot
##Reddit bot to evaluate factorials in comments

This bot should monitor comments as they're posted, use regex to check if the comment contains something of the form '1234!' or '1,234!', and post the solutions to any factorials the user mentions. Factorials get big pretty fast, so I'm assuming if a user posts about a factorial that they don't know its value. 

Unfortunately, as a result of how big factorials get and reddit's comment limit size of 10,000 characters, the highest factorial that can be evaluated is 3248!. In the future this may be mitigated by using a language that is actually fast (maybe [this project](https://github.com/stensonowen/longer), if it ever goes anywhere) and spanning multiple comments.

I'm mostly using this as an excuse to play around with Reddit's API, so I won't be too disappointed (or surprised) if it gets banned immediately.
