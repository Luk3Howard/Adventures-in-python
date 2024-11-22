# Create the guest list and print a personalised message for each invitee

dreamGuestList = ['Harrison Ford', 'Cal Newport', 'Aragorn', 'Me from the future']

print(f"\n First round of invitations")
print(f"\t{dreamGuestList[0].title()}, you are cordially invited to my super cool dinner party. There will be parking for your plane outside!")
print(f"\t{dreamGuestList[1].title()}, you are cordially invited to my super cool dinner party. No deep work allowed.")
print(f"\t{dreamGuestList[2].title()}, you are cordially invited to my super cool dinner party. There is a strict \"No Sword Policy\" in place.")
print(f"\t{dreamGuestList[3].title()}, you are cordially invited to my super cool dinner party. Please leave the time machine outside.")

# One of the guests can't make it! Need to remove 'Me from the future' from the guestlist, and send out an invite to someone new.
print(f"\nWell, well, well...sadly {dreamGuestList[3].title()} can't make it. How upsetting. I'll have to send out an invite to somebody else.")
excusedGuest = dreamGuestList.pop()
dreamGuestList.append('Bethany Coull')

print(f"punted:", excusedGuest)
print(f"current glist", dreamGuestList)

print(f"\n Second round of invitations:")
print(f"\t{dreamGuestList[0].title()}, you are cordially invited to my super cool dinner party. There will be parking for your plane outside!")
print(f"\t{dreamGuestList[1].title()}, you are cordially invited to my super cool dinner party. No deep work allowed.")
print(f"\t{dreamGuestList[2].title()}, you are cordially invited to my super cool dinner party. There is a strict \"No Sword Policy\" in place.")
print(f"\t{dreamGuestList[3].title()}, you are cordially invited to my super cool dinner party. I love you.")

# I just moved house and ordered a bigger table! I can invite 3 more people now. I need to tell invitees about this...

moveHouseMessage = "please be aware - I have moved house a found a bigger table. Therefore a bigger party! Hope to see you there this weekend."

print(f"\n I better tell them about the change of location...")
print(f"\tHello {dreamGuestList[0]}, {moveHouseMessage}")
print(f"\tHello invitees ({dreamGuestList[1]}), {moveHouseMessage}")
print(f"\tHello invitees ({dreamGuestList[2]}), {moveHouseMessage}")
print(f"\tHello invitees ({dreamGuestList[3]}), {moveHouseMessage}")

dreamGuestList.insert(0,'the swiftologist') # Beth will be thrilled lol
dreamGuestList.insert(2,'sally pooface') # stinky but will bring a good present
dreamGuestList.append('jeffrey star') # Beth, Sally and the swiftologist said they wouldn't come unless I invited them. God I hate planning parties.

print(f"punted:", excusedGuest)
print(f"current glist", dreamGuestList)

print(f"\nUpdated Party invites for all, including newly invited guests:")
print(f"\t{dreamGuestList[0].title()}, here's the details for the party: swing by Fanny Bawz Manor about from 7pm for a night of good food and entertainment - come hungry!")
print(f"\t{dreamGuestList[1].title()}, here's the details for the party: swing by Fanny Bawz Manor about from 7pm for a night of good food and entertainment - come hungry!")
print(f"\t{dreamGuestList[2].title()}, here's the details for the party: swing by Fanny Bawz Manor about from 7pm for a night of good food and entertainment - come hungry!")
print(f"\t{dreamGuestList[3].title()}, here's the details for the party: swing by Fanny Bawz Manor about from 7pm for a night of good food and entertainment - come hungry!")
print(f"\t{dreamGuestList[4].title()}, here's the details for the party: swing by Fanny Bawz Manor about from 7pm for a night of good food and entertainment - come hungry!")
print(f"\t{dreamGuestList[5].title()}, here's the details for the party: swing by Fanny Bawz Manor about from 7pm for a night of good food and entertainment - come hungry!")
print(f"\t{dreamGuestList[6].title()}, here's the details for the party: swing by Fanny Bawz Manor about from 7pm for a night of good food and entertainment - come hungry!")

# Aw crap - the table isn't coming in time! I've only got space for two guests. 
print("\nSorry everyone - I will have to cancel the party - my table order has been delayed due to Sauron himself holding it for ransom. I will reschedule soon and send out invites again.")
excusedGuest1 = dreamGuestList.pop(6)
print(f"\t{excusedGuest1.title()}, I'm so sorry but I'm having to cancel the party due to my table not arriving in time")
excusedGuest2 = dreamGuestList.pop(4)
print(f"\t{excusedGuest2.title()}, I'm so sorry but I'm having to cancel the party due to my table not arriving in time.")
excusedGuest3 = dreamGuestList.pop(3)
print(f"\t{excusedGuest3.title()}, I'm so sorry but I'm having to cancel the party due to my table not arriving in time.")
excusedGuest4 = dreamGuestList.pop(2)
print(f"\t{excusedGuest4.title()}, I'm so sorry but I'm having to cancel the party due to my table not arriving in time.")
excusedGuest5 = dreamGuestList.pop(1)
print(f"\t{excusedGuest5.title()}, I'm so sorry but I'm having to cancel the party due to my table not arriving in time.")

print(f"punted:", excusedGuest)
print(f"current glist", dreamGuestList)

#Let the two remaining guests they can still come and chill in the loungue!
print(f"\nBetter let my favourites know they can still come over on Saturday.")
print(f"\t{dreamGuestList[0].title()}, just to let you know I'll still be free this Saturday and with all this food...please come over and play some board games with me and {dreamGuestList[1].title()}")
print(f"\t{dreamGuestList[1].title()}, just to let you know I'll still be free this Saturday and with all this food...please come over and play some board games with me and {dreamGuestList[0].title()}")

# Take the remaining names of the list, then print it to confirm it's empty
del dreamGuestList[1]
del dreamGuestList[0]
print(f"\nThe dream dinner guest list now contains: ", dreamGuestList)



