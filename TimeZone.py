from datetime import datetime, timedelta

utctime = datetime.utcnow()
ISTtime = utctime + timedelta(hours=5,minutes=30)
NYtime=ISTtime+timedelta(hours=-9,minutes=-30)
Sydtime=ISTtime+timedelta(hours=5,minutes=30)
Jotime=ISTtime+timedelta(hours=-3,minutes=-30)
print("The time in New York is",str(NYtime)[11:19:])
print("The time in Sydney is",str(Sydtime)[11:19:])
print("The time in Johannesburg is",str(Jotime)[11:19:])
