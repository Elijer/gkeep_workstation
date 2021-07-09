# README

## Getting keep.login() method to work
So what worked for me on my personal email address is this:
1. Make sure multi-factor authentication is on for google [here](https://myaccount.google.com/)
    - Not sure if it's necessary, but I also ticked a box that said "allow less secure apps" or something
2. Create an app password for the device you are using[here](https://myaccount.google.com)
3. Mess around with every python version you can -- for me, the 3.9.6 interpreter runngin Python 2.7.18 worked for me
4. Try downgrading the 'requests' package, whatever that is with `pip install requests==2.23.0`, a tip I found [in this thread.](https://github.com/simon-weber/gpsoauth/issues/24)

I went through a few error messages. At first, I just couldn't get python to recognize gkeepapi, which probably just has to do with me using pyenv wrong and not understanding it well. Only certain version of python on my machine can access the gkeepapi module I downloaded, no matter how many times I tried to download it.

Once I found the python version that played nice with gkeepsapi, then I got this error message for a while:

`gkeepapi.exception.LoginException: ('BadAuthentication')`

I fixed this one by messing around with python version more. 3.9.6 (tip #3) and possibly also downgrading the 'requests' package (tip #4) got rid of this error message, at which point I got this one instead:

`gkeepapi.LoginException: NeedsBrowser`

This is what was fixed by all the other tips. Using an app password, making sure 2 factor auth was on, and making sure to omit the `device id`. Some of the threads talk about supplying a device id, but when I got the login method to eventually work, I actually only supplied the first two arguments. My code, therefore, ended up looking like this:

```
import gkeepapi
keep = gkeepapi.Keep()
success = keep.login('email@gmail.com', 'xxxxxxxxxxxxxxxx')
```

# Next Steps
On some of these threads and in the gkeeps docs, there is mention of saving a masterkey for use, which eliminates the need to keep logging in with google keep. This might be useful.

