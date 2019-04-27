import pandas as pd
import time
# need itemProfiles & utilityMatrix

# TODO
# for each user x
#     for each tag y
#         look in utility matrix for x's row
#         for each item in the row
#             check item_profile to see if item has tag y
#             if item has tag y, add to sum variable
#         compute average of y items for user x
#         set average to be the user profile value for user x about y tag

tags = ['1 Star', '2 Star', '3 Star', '4 Star', '5 Star', 'Accessible Hotel', 'Accessible Parking', 'Adults Only',
       'Air Conditioning', 'Airport Hotel', 'Airport Shuttle', 'All Inclusive (Upon Inquiry)', 'Balcony', 'Bathtub',
       'Beach', 'Beach Bar', 'Beauty Salon', 'Bed & Breakfast', 'Bike Rental', 'Boat Rental', 'Body Treatments',
       'Boutique Hotel', 'Bowling', 'Bungalows', 'Business Centre', 'Business Hotel', 'Cable TV', 'Camping Site',
       'Car Park', 'Casa Rural (ES)', 'Casino (Hotel)', 'Central Heating', 'Childcare', 'Club Hotel',
       'Computer with Internet', 'Concierge', 'Conference Rooms', 'Convenience Store', 'Convention Hotel',
       'Cosmetic Mirror', 'Cot', 'Country Hotel', 'Deck Chairs', 'Design Hotel', 'Desk', 'Direct beach access',
       'Diving', 'Doctor On-Site', 'Eco-Friendly hotel', 'Electric Kettle', 'Excellent Rating',
       'Express Check-In / Check-Out', 'Family Friendly', 'Fan', 'Farmstay', 'Fitness', 'Flatscreen TV',
       'Free WiFi (Combined)', 'Free WiFi (Public Areas)', 'Free WiFi (Rooms)', 'Fridge', 'From 2 Stars',
       'From 3 Stars', 'From 4 Stars', 'Gay-friendly', 'Golf Course', 'Good Rating', 'Guest House', 'Gym',
       'Hairdresser', 'Hairdryer', 'Halal Food', 'Hammam', 'Health Retreat', 'Hiking Trail', 'Honeymoon',
       'Horse Riding', 'Hostal (ES)', 'Hostel', 'Hot Stone Massage', 'Hotel', 'Hotel Bar', 'House / Apartment',
       'Hydrotherapy', 'Hypoallergenic Bedding', 'Hypoallergenic Rooms', 'Ironing Board', 'Jacuzzi (Hotel)',
       "Kids' Club", 'Kosher Food', 'Large Groups', 'Laundry Service', 'Lift', 'Luxury Hotel', 'Massage', 'Microwave',
       'Minigolf', 'Motel', 'Nightclub', 'Non-Smoking Rooms', 'On-Site Boutique Shopping', 'Openable Windows',
       'Organised Activities', 'Pet Friendly', 'Playground', 'Pool Table', 'Porter', 'Pousada (BR)', 'Radio',
       'Reception (24/7)', 'Resort', 'Restaurant', 'Romantic', 'Room Service', 'Room Service (24/7)', 'Safe (Hotel)',
       'Safe (Rooms)', 'Sailing', 'Satellite TV', 'Satisfactory Rating', 'Sauna', 'Self Catering', 'Senior Travellers',
       'Serviced Apartment', 'Shooting Sports', 'Shower', 'Singles', 'Sitting Area (Rooms)', 'Ski Resort', 'Skiing',
       'Solarium', 'Spa (Wellness Facility)', 'Spa Hotel', 'Steam Room', 'Sun Umbrellas', 'Surfing',
       'Swimming Pool (Bar)', 'Swimming Pool (Combined Filter)', 'Swimming Pool (Indoor)', 'Swimming Pool (Outdoor)',
       'Szep Kartya', 'Table Tennis', 'Telephone', 'Teleprinter', 'Television', 'Tennis Court', 'Tennis Court (Indoor)',
       'Terrace (Hotel)', 'Theme Hotel', 'Towels', 'Very Good Rating', 'Volleyball', 'Washing Machine', 'Water Slide',
       'Wheelchair Accessible', 'WiFi (Public Areas)', 'WiFi (Rooms)']


# Item Profiles (excluding prices)
def get_item_profs():
    file = open('C:\\Users\\banana\\PycharmProjects\\trivago\\data\\item_metadata.csv')
    line = file.readline()
    line = file.readline()
    items = []
    iprofs = {}
    while line:
        line = line.split(',')
        items.append(str(line[0]))
        line[1] = line[1].split('|')
        line[1][-1] = line[1][-1].strip('\n')
        iprofs[line[0]] = line[1]
        line = file.readline()
    file.close()
    items.sort()
    # iprofs: a dictionary where key is item number & value is list of metadata tags
    return iprofs


# Utility Matrix
def util_matrix_format():
    util_mat_file = open('C:\\Users\\banana\\PycharmProjects\\trivago\\src\\content_based\\output.csv')
    line = util_mat_file.readline()
    util_mat = {}
    while line:
        line = line.split(',')
        name = line[0]
        item_weights = line[1:]
        weights = {}
        j = 0
        for i in range(len(item_weights)//2):
            weights[item_weights[j]] = item_weights[j+1].strip('\n')
            j += 2
        util_mat[name] = weights
        line = util_mat_file.readline()
    util_mat_file.close()
    return util_mat


t1 = time.time()
print('Creating item profiles...')
# i_profs: a dictionary where key is item number & value is list of metadata tags
i_profs = get_item_profs()
t2 = time.time()
print('Done: ' + str(t2-t1))

print('Formatting utility matrix...')
# Format kev's utility matrix output file into dictionary of key = users, value = dictionary of item,weight pairs
util_matrix = util_matrix_format()
t3 = time.time()
print('Done: ' + str(t3-t2) + '\n')

print('Processing utility matrix & item profiles to calculate user profiles...')
user_profs = {}
for user, weights in util_matrix.items():  # 730,803
    user_profs[user] = []
    items = weights.keys()  # all items the user has interacted with
    if len(items) > 0:
        for t in tags:  # 157 make a summed value for every item with tag t
            summ = 0
            numm = 0
            for i in items:
                if t in i_profs[i]:
                    summ += float(weights[i])
                    numm += 1
            # this is the value for user & tag t
            if numm > 0:
                avg_weight = summ/numm
                user_profs[user].append((t, avg_weight))
t4 = time.time()
print('Done:' + str(t4-t3))
