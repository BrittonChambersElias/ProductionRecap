import pandas as pd
import os
import EndOfDayReport
from EndOfDayReport import Count_Line

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

#data frames for each line
df1 = pd.read_html('https://rfa.tile.hiveplatform.org/bc_scan_event?cell_id=tile-line1-qc&page_size=2000&offset=0')[0]
df2 = pd.read_html('https://rfa.tile.hiveplatform.org/bc_scan_event?cell_id=tile-line2-qc&page_size=2000&offset=0')[0]
df3 = pd.read_html('https://rfa.tile.hiveplatform.org/bc_scan_event?cell_id=tile-line3-qc&page_size=2000&offset=0')[0]
df4 = pd.read_html('https://rfa.tile.hiveplatform.org/bc_scan_event?cell_id=tile-line4-qc&page_size=2000&offset=0')[0]
df5 = pd.read_html('https://rfa.tile.hiveplatform.org/bc_scan_event?cell_id=tile-line5-qc&page_size=2000&offset=0')[0]
df6 = pd.read_html('https://rfa.tile.hiveplatform.org/bc_scan_event?cell_id=tile-line6-qc&page_size=2000&offset=0')[0]
bc = pd.read_html('https://rfa.tile.hiveplatform.org/mc_pack_event?cell_id=&page_size=25000&offset=0')[0]

#Date and Time Mask
df1['date'] = pd.to_datetime(df1['scan_event_timestamp'], format="%Y-%m-%d %H:%M:%S")
df2['date'] = pd.to_datetime(df2['scan_event_timestamp'], format="%Y-%m-%d %H:%M:%S")
df3['date'] = pd.to_datetime(df3['scan_event_timestamp'], format="%Y-%m-%d %H:%M:%S")
df4['date'] = pd.to_datetime(df4['scan_event_timestamp'], format="%Y-%m-%d %H:%M:%S")
df5['date'] = pd.to_datetime(df5['scan_event_timestamp'], format="%Y-%m-%d %H:%M:%S")
df6['date'] = pd.to_datetime(df6['scan_event_timestamp'], format="%Y-%m-%d %H:%M:%S")
bc['date'] = pd.to_datetime(bc['mc_pack_event_timestamp'], format="%Y-%m-%d %H:%M:%S")
#start_date=input("'yyyy-mm-dd H:M:S': ")
mask1 = (df1['date'] > EndOfDayReport.start_date)
mask2 = (df2['date'] > EndOfDayReport.start_date)
mask3 = (df3['date'] > EndOfDayReport.start_date)
mask4 = (df4['date'] > EndOfDayReport.start_date)
mask5 = (df5['date'] > EndOfDayReport.start_date)
mask6 = (df6['date'] > EndOfDayReport.start_date)
mask7 = (bc['date'] > EndOfDayReport.start_date)

df1 = df1.loc[mask1]
df2 = df2.loc[mask2]
df3 = df3.loc[mask3]
df4 = df4.loc[mask4]
df5 = df5.loc[mask5]
df6 = df6.loc[mask6]
bc = bc.loc[mask7]


#Count QC Total Per Line L1Count = bc.line_id.value_counts().KITTILELINE1
def countL1():
    try:
        l1 = df1[df1['barcode_data'].str.startswith('F0', na=False)]
        totalQC_L1 = l1.line_id.value_counts().KITTILELINE1
        print("Line1:",totalQC_L1,"envelopes")

        #l1count = bc.line_id.value_counts().KITTILELINE1
        l1perc = totalQC_L1 / Count_Line.L1Count * 100
        float = l1perc
        countL1.format_float = "{:.2f}".format(float)
        print("Line1:","%s%%"%countL1.format_float,"%", "of", Count_Line.L1Count, "went to QC\n")
       
        return "%s%%"%countL1.format_float
    except:
        countL1.format_float = print("Line 1: Didn't Run\n")
        print("Line 1: Didn't Run\n")


def countL2():
    try:
        l2 = df2[df2['barcode_data'].str.startswith('F0', na=False)]
        totalQC_L2 = l2.line_id.value_counts().KITTILELINE2
        print("Line2:",totalQC_L2,"envelopes")
        
        #l2count = bc.line_id.value_counts().KITTILELINE2
        l2perc = totalQC_L2 / Count_Line.L2Count * 100
        float = l2perc
        countL2.format_float = "{:.2f}".format(float)
        print("Line2:",countL2.format_float,"%", "of", Count_Line.L2Count, "went to QC\n")
        return countL2.format_float
    except:
        countL2.format_float = print("Line 2: Didn't Run")
        return countL2.format_float
def countL3():
    try:
        l3 = df3[df3['barcode_data'].str.startswith('F0', na=False)]
        totalQC_L3 = l3.line_id.value_counts().KITTILELINE3
        print("Line3:",totalQC_L3,"envelopes")
        
        #l3count = bc.line_id.value_counts().KITTILELINE3
        l3perc = totalQC_L3 / Count_Line.L3Count * 100
        float = l3perc
        countL3.format_float = "{:.2f}".format(float)
        print("Line3:",countL3.format_float,"%", "of", Count_Line.L3Count, "went to QC\n")
        return countL3.format_float
    except:
        countL3.format_float = print("Line 3: Didn't Run")
        return countL3.format_float

def countL4():
    try:
        l4 = df4[df4['barcode_data'].str.startswith('F0', na=False)]
        totalQC_L4 = l4.line_id.value_counts().KITTILELINE4
        print("Line4:",totalQC_L4,"envelopes")
        
        #l4count = bc.line_id.value_counts().KITTILELINE4
        l4perc = totalQC_L4 / Count_Line.L4Count * 100
        float = l4perc
        countL4.format_float = "{:.2f}".format(float)
        print("Line4:",countL4.format_float,"%", "of", Count_Line.L4Count, "went to QC\n")
        return countL4.format_float
    except:
        countL4.format_float = print("Line 4: Didn't Run")
        return countL4.format_float

def countL5():
    try:
        l5 = df5[df5['barcode_data'].str.startswith('F0', na=False)]
        totalQC_L5 = l5.line_id.value_counts().KITTILELINE5
        print("Line5:",totalQC_L5,"envelopes")
        
        #l5count = bc.line_id.value_counts().KITTILELINE5
        l5perc = totalQC_L5 / Count_Line.L5Count * 100
        float = l5perc
        countL5.format_float = "{:.2f}".format(float)
        print("Line5:",countL5.format_float,"%", "of", Count_Line.L5Count, "went to QC\n")
        return countL5.format_float
    except:
        countL5.format_float = print("Line 5: Didn't Run")
        return countL5.format_float

def countL6():
    try:
        l6 = df6[df6['barcode_data'].str.startswith('F0', na=False)]
        totalQC_L6 = l6.line_id.value_counts().KITTILELINE6
        print("Line6:",totalQC_L6,"envelopes")
        
        #l6count = bc.line_id.value_counts().KITTILELINE6
        l6perc = totalQC_L6 / Count_Line.L6Count * 100
        float = l6perc
        countL6.format_float = "{:.2f}".format(float)
        print("Line6:",countL6.format_float,"%", "of", Count_Line.L6Count, "went to QC\n")
        return countL6.format_float
    except:
        countL6.format_float = print("Line 6: Didn't Run")
        return countL6.format_float

print("Total QC Per Line:\n")

countL1()

countL2()

countL3()

countL4()

countL5()

countL6()

print("\n             Production Unit Recap for the date of",EndOfDayReport.start_date)
print("\n                            Total Packed:", EndOfDayReport.TotalPack,"\n")

new_df = {'ProductionLine ': ['Line 1', 'Line 2', 'Line 3', 'Line 4', 'Line 5', 'Line 6'],
        'TotalPacked ': [Count_Line.L1Count, Count_Line.L2Count, Count_Line.L3Count, Count_Line.L4Count, Count_Line.L5Count,Count_Line.L6Count],
        'ProductionLine ':['Line 1', 'Line 2', 'Line 3', 'Line 4', 'Line 5', 'Line 6'],
        'AverageCountPerHour ': [Count_Line.format_float1, Count_Line.format_float2, Count_Line.format_float3, Count_Line.format_float4, Count_Line.format_float5, Count_Line.format_float6],
        'ProductionLine ':['Line 1', 'Line 2', 'Line 3', 'Line 4', 'Line 5', 'Line 6'],
        '% SentToQC ': ["%s%%"%countL1.format_float, "%s%%"%countL2.format_float, "%s%%"%countL3.format_float, "%s%%"%countL4.format_float, "%s%%"%countL5.format_float, "%s%%"%countL6.format_float]  
        }


outFileName = ("Production Unit Recap for the date of ")
title = outFileName + EndOfDayReport.start_date
frame = pd.DataFrame(new_df)
frame.to_csv(title+".csv", index=False)
print (frame)