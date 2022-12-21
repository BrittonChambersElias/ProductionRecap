import pandas as pd
from IPython.display import display
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

cls()

df = pd.read_html('*')[0]


df['date'] = pd.to_datetime(df['mc_pack_event_timestamp'], format="%Y-%m-%d %H:%M:%S")
print("Enter Todays date")
start_date=input("'yyyy-mm-dd': ")
cls()
mask = (df['date'] > start_date) 
df = df.loc[mask]


cls()
def dataSplit(df):
    df = df.groupby([pd.Grouper(key='date', freq='H'),df.line_id]).size().reset_index(name='Units/Hour')
    df1 = df[df.line_id == 'KITTILELINE1']
    df2 = df[df.line_id == 'KITTILELINE2']
    df3 = df[df.line_id == 'KITTILELINE3']
    df4 = df[df.line_id == 'KITTILELINE4']
    df5 = df[df.line_id == 'KITTILELINE5']
    df6 = df[df.line_id == 'KITTILELINE6']

    pd.concat([
    pd.concat([df1, df2], axis=1),
    pd.concat([df3, df4], axis=1),
    pd.concat([df5, df6], axis=1)]).to_csv('UPHperLine.csv')
    
dataSplit(df)

try:
    Line1Count = df.isin(['KITTILELINE1']).any().any()
except:
    print("")
try:
    Line2Count = df.isin(['KITTILELINE2']).any().any()
except:
    print("")
try:
    Line3Count = df.isin(['KITTILELINE3']).any().any()
except:
    print("")
try:
    Line4Count = df.isin(['KITTILELINE4']).any().any()
except:
    print("")
try:
    Line5Count = df.isin(['KITTILELINE5']).any().any()
except:
    print("")
try:
    Line6Count = df.isin(['KITTILELINE6']).any().any()
except:
    print("")
TotalPack = df.event_type.value_counts().PACK

perHour = df.groupby([pd.Grouper(key='date', freq='H'),df.line_id]).size().reset_index(name='Units/Hour')
try:
    L1average = perHour.line_id.value_counts().KITTILELINE1
except:
    print("")
try:
    L2average = perHour.line_id.value_counts().KITTILELINE2
except:
    print("")
try:
    L3average = perHour.line_id.value_counts().KITTILELINE3
except:
    print("")
try:
    L4average = perHour.line_id.value_counts().KITTILELINE4
except:
    print("")
try:
    L5average = perHour.line_id.value_counts().KITTILELINE5
except:
    print("")
try:
    L6average = perHour.line_id.value_counts().KITTILELINE6
except:
    print("")

def Count_Line():
    if Line1Count:
        Count_Line.L1Count = df.line_id.value_counts().KITTILELINE1
        print("Line 1 Total Packed: ", Count_Line.L1Count)  
    else:
        Count_Line.L1Count = print("Line 1 didn't run today")
    if Line2Count:
        Count_Line.L2Count = df.line_id.value_counts().KITTILELINE2
        print("Line 2 Total Packed: ", Count_Line.L2Count)
        #return Count_Line.L2Count
    else:
       Count_Line.L2Count = print("Line 2 didn't run today")
    if Line3Count:
        Count_Line.L3Count = df.line_id.value_counts().KITTILELINE3
        print("Line 3 Total Packed: ", Count_Line.L3Count)
        #return Count_Line.L3Count
    else:
       Count_Line.L3Count= print("Line 3 didn't run today")
    if Line4Count:
        Count_Line.L4Count = df.line_id.value_counts().KITTILELINE4
        print("Line 4 Total Packed: ", Count_Line.L4Count)
        #return Count_Line.L4Count
    else:
       Count_Line.L4Count= print("Line 4 didn't run today")
    if Line5Count:
        Count_Line.L5Count = df.line_id.value_counts().KITTILELINE5
        print("Line 5 Total Packed: ", Count_Line.L5Count)
        #return Count_Line.L5Count
    else:
        Count_Line.L5Count=print("Line 5 didn't run today")
    if Line6Count:
        Count_Line.L6Count = df.line_id.value_counts().KITTILELINE6
        print("Line 6 Total Packed: ", Count_Line.L6Count)
        #return Count_Line.L1Count,Count_Line.L2Count,Count_Line.L3Count,Count_Line.L4Count,Count_Line.L5Count,Count_Line.L6Count
    else:
        Count_Line.L6Count = 'None'
        
    print("--------------------------------------------")

    print("Average Units Per Hour:\n")
    try:
        L1avg = Count_Line.L1Count / L1average
        float = L1avg
        Count_Line.format_float1 = "{:.2f}".format(float)
        print("line 1:", Count_Line.format_float1)
    except:
        Count_Line.format_float1 = print("Line 1: Didn't Run Today")
    try:
        L2avg = Count_Line.L2Count / L2average
        float = L2avg
        Count_Line.format_float2 = "{:.2f}".format(float)
        print("line 2:", Count_Line.format_float2)
    except:
        Count_Line.format_float2 = print("Line 2: didn't run today")
    try:
        L3avg = Count_Line.L3Count / L3average
        float = L3avg
        Count_Line.format_float3 = "{:.2f}".format(float)
        print("line 3:", Count_Line.format_float3)
    except:
        Count_Line.format_float3 = print("Line 3: didn't run today")
    try:
        L4avg = Count_Line.L4Count / L4average
        float = L4avg
        Count_Line.format_float4 = "{:.2f}".format(float)
        print("line 4:", Count_Line.format_float4)
    except:
        Count_Line.format_float4 = print("Line 4: didn't run today")
    try:
        L5avg = Count_Line.L5Count / L5average
        float = L5avg
        Count_Line.format_float5 = "{:.2f}".format(float)
        print("line 5:", Count_Line.format_float5)
    except:
        Count_Line.format_float5=print("Line 5 didn't run today")
    try:
        L6avg = Count_Line.L6Count / L6average
        float = L6avg
        Count_Line.format_float6 = "{:.2f}".format(float)
        print("line 6:", Count_Line.format_float6)
    except:
        Count_Line.format_float6=print("Line 6: didn't run today \n")
    print("--------------------------------------------")
    return Count_Line.format_float1,Count_Line.format_float2,Count_Line.format_float3,Count_Line.format_float4,Count_Line.format_float5,Count_Line.format_float6,Count_Line.L1Count,Count_Line.L2Count,Count_Line.L3Count,Count_Line.L4Count,Count_Line.L5Count,Count_Line.L6Count




print("\nProduction Unit Recap for the date of",start_date)

print("\nTotal Packed:", TotalPack,"\n")
Count_Line()

print("File UPHperLine.csv was updated..")
print("--------------------------------------------")
