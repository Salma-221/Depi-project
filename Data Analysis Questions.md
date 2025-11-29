### **Data Analysis Questions :** 



**-- Calculate percentage distribution of Railcard types.**



railcard\_counts = df\['Railcard'].value\_counts()

print(railcard\_counts)



railcard\_pct = df\['Railcard'].value\_counts(normalize=True).mul(100).round(2)

print(railcard\_pct)



**-- Create a summary table containing each Railcard type with its count and percentage.**



railcard\_counts = df\['Railcard'].value\_counts().reset\_index()

railcard\_counts.columns = \['Railcard', 'Count']





railcard\_pct = df\['Railcard'].value\_counts(normalize=True).mul(100).round(2).reset\_index()

railcard\_pct.columns = \['Railcard', 'Percentage']





railcard\_summary = pd.merge(railcard\_counts, railcard\_pct, on='Railcard')



railcard\_summary



**-- Calculate refund rate for each Railcard type based on total trips and refund requests.**

refund\_by\_railcard = (

&nbsp;   df.groupby('Railcard')

&nbsp;   .agg(

&nbsp;       Total\_Trips=('Refund Request', 'size'),

&nbsp;       Refund\_Requests=('Refund Request', lambda x: (x == 'Yes').sum())

&nbsp;   )

&nbsp;   .assign(Refund\_Rate=lambda x: round((x\['Refund\_Requests'] / x\['Total\_Trips']) \* 100, 2))

&nbsp;   .reset\_index()

&nbsp;   .sort\_values('Refund\_Rate', ascending=False)

)



refund\_by\_railcard



**-- Count how many times each delay reason appears in the dataset.**



delay\_reason\_counts = df\['Reason for Delay'].value\_counts().reset\_index()

delay\_reason\_counts.columns = \['Reason for Delay', 'Count']

delay\_reason\_counts



**-- Delay reason counts (excluding ON TIME)**

\## Skipping the Journeys on time

delay\_reason\_counts = (

&nbsp;   df\[df\['Reason for Delay'] != 'ON TIME']\['Reason for Delay']

&nbsp;   .value\_counts()

&nbsp;   .reset\_index()

)



delay\_reason\_counts.columns = \['Reason for Delay', 'Count']

delay\_reason\_counts



**-- Refund rate by delay reason**

refund\_by\_reason = (

&nbsp;   df.groupby('Reason for Delay')\['Refund Request']

&nbsp;   .value\_counts(normalize=True)

&nbsp;   .unstack()

&nbsp;   .fillna(0)

)





refund\_rate\_by\_reason = (

&nbsp;   refund\_by\_reason

&nbsp;   .assign(\*\*{'Refund Rate (%)': refund\_by\_reason.get('Yes', 0) \* 100})

&nbsp;   \[\['Refund Rate (%)']]

&nbsp;   .sort\_values('Refund Rate (%)', ascending=False)

&nbsp;   .reset\_index()

)



refund\_rate\_by\_reason



**-- Average delay per month**

delay\_by\_month = df.groupby('Journey Month')\['Journey Delay (min)'].mean().reset\_index()

delay\_by\_month.columns = \['Journey Month', 'Average Delay (min)']

delay\_by\_month.sort\_values('Average Delay (min)', ascending=False)



**-- Revenue loss due to refunds**



refund\_loss = df\[df\['Refund Request'] == 'Yes']\['Price'].sum()



total\_revenue = df\['Price'].sum()



loss\_pct = (refund\_loss / total\_revenue) \* 100



loss\_summary = pd.DataFrame({

&nbsp;   'Total Revenue': \[total\_revenue],

&nbsp;   'Refund Loss': \[refund\_loss],

&nbsp;   'Loss Percentage (%)': \[round(loss\_pct, 2)]

})

loss\_summary



**-- Refund rate by price bins**

price\_refund = (

&nbsp;   df.groupby('Price Bins')\['Refund Request']

&nbsp;   .value\_counts(normalize=True)

&nbsp;   .unstack()

&nbsp;   .fillna(0)

)



price\_refund\_rate = (

&nbsp;   price\_refund

&nbsp;   .assign(\*\*{'Refund Rate (%)': price\_refund.get('Yes', 0) \* 100})

&nbsp;   \[\['Refund Rate (%)']]

&nbsp;   .reset\_index()

&nbsp;   .sort\_values('Refund Rate (%)', ascending=False)

)



price\_refund\_rate



**-- Refund rate by purchase type**



refund\_by\_purchase\_type = (

&nbsp;   df.groupby('Purchase Type')\['Refund Request']

&nbsp;   .value\_counts(normalize=True)

&nbsp;   .unstack()

&nbsp;   .fillna(0)

)





refund\_by\_purchase\_type\_rate = (

&nbsp;   refund\_by\_purchase\_type

&nbsp;   .assign(\*\*{'Refund Rate (%)': refund\_by\_purchase\_type.get('Yes', 0) \* 100})

&nbsp;   \[\['Refund Rate (%)']]

&nbsp;   .reset\_index()

&nbsp;   .sort\_values('Refund Rate (%)', ascending=False)

)



refund\_by\_purchase\_type\_rate



**-- Refund rate by Railcard + Purchase Type**



refund\_rate = (

&nbsp;   df\[df\['Refund Request'] == 'Yes']

&nbsp;   .groupby(\['Railcard', 'Purchase Type'])

&nbsp;   .size()

&nbsp;   .div(df.groupby(\['Railcard', 'Purchase Type']).size())

&nbsp;   .mul(100)

&nbsp;   .reset\_index(name='Refund Rate (%)')

&nbsp;   .sort\_values('Refund Rate (%)', ascending=False)

)



refund\_rate



**-- Delay count by ticket class**



class\_delay\_count = (

&nbsp;   df\[df\['Journey Delay (min)'] > 0]

&nbsp;   .groupby('Ticket Class')

&nbsp;   .size()

&nbsp;   .reset\_index(name='Delay Count')

&nbsp;   .sort\_values('Delay Count', ascending=False)

)



class\_delay\_count



**-- Average price by Railcard**

avg\_price\_by\_railcard = (

&nbsp;   df.groupby('Railcard')\['Price']

&nbsp;   .mean()

&nbsp;   .reset\_index()

&nbsp;   .rename(columns={'Price': 'Average Price'})

&nbsp;   .sort\_values('Average Price', ascending=False)

)



avg\_price\_by\_railcard



**-- Payment method distribution by Railcard**

payment\_by\_railcard = (

&nbsp;   df.groupby(\['Railcard', 'Payment Method'])

&nbsp;   .size()

&nbsp;   .reset\_index(name='Count')

)



payment\_by\_railcard\['Percentage'] = (

&nbsp;   payment\_by\_railcard.groupby('Railcard')\['Count']

&nbsp;   .transform(lambda x: (x / x.sum()) \* 100)

&nbsp;   .round(2)

)



payment\_by\_railcard.sort\_values(\['Railcard', 'Count'], ascending=\[True, False])



