from TSN_Abstracter import *;
import time;

Log.Delete();

Log.Info(File.Tree("TSN_Abstracter"));
Log.Info(File.Tree("IDontFuckingExist"));

Config.Logging["File"] = True;
Log.Critical("Im the only log to be written bitches, for now");

File.JSON_Write("JSON/Test.json", {"hi": "balls"});

Awaited = Log.Info("Hey, I'm waiting for status shit here...");
Log.Critical("im gonna fucc shi up now")
print(Awaited)
OtherAwaited = Log.Warning("Doing LITERALLY nothing right now...");
time.sleep(1);
Awaited.OK();
OtherAwaited.OK();
Awaited = Log.Info("wahooo, this code is shit...");
Awaited.Status_Update("[Yeah it fuckin is]");

Config.Logging["File"] = False;

"""
Unix = 0;
while True:
    Log.Carriage(Time.Elapsed_String(Unix));
    Unix += 1;
"""

