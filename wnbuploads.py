import os
import sys
import csv
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wnb.settings")
django.setup()

from rooms.models import *
from hosts.models import *

CATEGORY_PATH = 'wnb_csv_file/1_Category.csv'
ROOMTYPE_PATH = 'wnb_csv_file/2_RoomType.csv'
FACILITY_PATH = 'wnb_csv_file/3_Facilities.csv'
ROOM_PATH = 'wnb_csv_file/4_Rooms.csv'
ROOMFACILITY_PATH = 'wnb_csv_file/5_RoomFacility.csv'
IMAGE_PATH = 'wnb_csv_file/6_Images.csv'
DETAIL_IMAGE_PATH = 'wnb_csv_file/7_Detail_images.csv'


def insert_Category():
    with open(CATEGORY_PATH) as csv_file:
        data_reader = csv.reader(csv_file)
        next(data_reader, None)
        for row in data_reader:
            if row[0]:
                name    = row[0]
                img_url = row[1]
                
                Category.objects.create(name = name, img_url= img_url)
    print('Categegory DATA UPLOADED SUCCESSFULY!')

def insert_RoomType():
    with open(ROOMTYPE_PATH) as csv_file:
        data_reader = csv.reader(csv_file)
        next(data_reader, None)
        for row in data_reader:
            if row[0]:
                name    = row[0]
                RoomType.objects.create(name = name)
    print('Roomtype DATA UPLOADED SUCCESSFULY!')

# def insert_Host():
#     with open(HOST_PATH) as csv_file:
#         data_reader = csv.reader(csv_file)
#         next(data_reader, None)
#         for row in data_reader:
#             if row[0]:
#                 user = row[0]
#                 profile_img = row[1]
                
#                 Host.objects.create(
#                     user        = user,
#                     profile_img = profile_img
#                     )
#     print('Host DATA UPLOADED SUCCESSFULY!')

def insert_Facility():
    with open(FACILITY_PATH) as csv_file:
        data_reader = csv.reader(csv_file)
        next(data_reader, None)
        for row in data_reader:
            if row[0]:
                name = row[0]
                Facility.objects.create(name = name)
    print('Facility DATA UPLOADED SUCCESSFULY!')


def insert_Room():
    with open(ROOM_PATH) as csv_file:
        data_reader = csv.reader(csv_file)
        next(data_reader, None)
        for row in data_reader:
            if row[0]:
                name =row[0]
                address = row[1]
                detail_address = row[2]
                price = row[3]
                description = row[4]
                latitude = row[5]
                longitude = row[6]
                maximum_occupancy = row[7]
                bedroom = row[8]
                bathroom = row[9]
                bed = row[10]
                category = Category.objects.get(id  = row[11])
                room_type = RoomType.objects.get(id = row[12])

                Room.objects.create(
                    name = name,
                    address = address,
                    detail_address = detail_address,
                    price = price,
                    description = description,
                    latitude = latitude,
                    longitude = longitude,
                    maximum_occupancy = maximum_occupancy,
                    bedroom = bedroom,
                    bathroom = bathroom,
                    bed = bed,
                    host = None,
                    category = category,
                    room_type = room_type
                )
                
        print('insert_room DATA UPLOADED SUCCESSFULY!')


def insert_RoomFacility():
    with open(ROOMFACILITY_PATH) as csv_file:
        data_reader = csv.reader(csv_file)
        next(data_reader, None)
        for row in data_reader:
            if row[0]:
                room = Room.objects.get(id = row[0])
                room_facility = Facility.objects.get(id=row[1])
                RoomFacility.objects.create(room=room, room_facility = room_facility )
    print('Facility DATA UPLOADED SUCCESSFULY!')



def insert_Image():
    with open(IMAGE_PATH) as csv_file:
        data_reader = csv.reader(csv_file)
        next(data_reader, None)
        for row in data_reader:
            if row[0]:
                url     = row[0]
                room    = Room.objects.get(id=row[1])
                Image.objects.create(url = url, room = room)
    print('Image DATA UPLOADED SUCCESSFULY!')


def insert_DetailImage():
    with open(DETAIL_IMAGE_PATH) as csv_file:
        data_reader = csv.reader(csv_file)
        next(data_reader, None)
        for row in data_reader:
            if row[0]:
                url     = row[0]
                room    = Room.objects.get(id=row[1])
                DetailImage.objects.create(url = url, room = room)
    print('Image DATA UPLOADED SUCCESSFULY!')

# insert_Category()
# insert_RoomType()
# insert_Host()
# insert_Facility()
# insert_Room()
# insert_RoomFacility()
# insert_Image()
# insert_DetailImage()
