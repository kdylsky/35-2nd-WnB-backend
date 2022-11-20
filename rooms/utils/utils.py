from django.db.models import Q

def rooms_filter(filter_value):
    q = Q()        
    if filter_value["min_price"] and filter_value["max_price"]:
        q &= Q(price__gte = filter_value["min_price"], price__lte = filter_value["max_price"])

    if filter_value["address"]:
        q &= Q(address__icontains = filter_value["address"])

    if filter_value["room_type_ids"]:
        q &= Q(room_type__id__in = filter_value["room_type_ids"])

    if filter_value["bed"]:
        q &= Q(bed__gte = filter_value["bed"])

    if filter_value["bedroom"]:
        q &= Q(bedroom__gte = filter_value["bedroom"])

    if filter_value["bathroom"]:
        q &= Q(bathroom__gte = filter_value["bathroom"])

    if filter_value["category"] :
        q &= Q(category_id = filter_value["category"])

    if filter_value["facility_ids"]:
        q &= Q(roomfacility__room_facility_id__in = filter_value["facility_ids"])

    if filter_value["maximum_occupancy"]:
        q &= Q(maximum_occupancy__gte = filter_value["maximum_occupancy"])

    return q