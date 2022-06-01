class Meeting(object):
    def __init__(self, _id, start, end):
        self._id = _id
        self.start = start
        self.end = end
        
class Room(object):
    def __init__(self, _id):
        self._id = _id
        
    def __repr__(self):
        return str(self._id)

# constants; END before START for sorting purposes        
END = 0
START = 1

# input: meetings = list((int, int))
# output: num_rooms, dict(meeting_index -> room_id)
def schedule_meetings(meetings):
    # sort by start time
    num_rooms = 1
    meeting_assignments = {}
    # list((meeting_id, time, event)) where event is 'Start' or 'End'
    meeting_events = []
    for m in meetings:
        meeting_events.append((m.start, START, m._id))
        meeting_events.append((m.end, END, m._id))
    
    # should always do ends before starts
    sorted_meeting_events = sorted(meeting_events)
    rooms = set([Room(1)])
    
    for meeting_event in sorted_meeting_events:
        (_, time_type, meeting_id) = meeting_event
        if time_type == START:
            if len(rooms) == 0:
                num_rooms += 1
                rooms.add(Room(num_rooms))
            next_room = rooms.pop()  # should never error
            meeting_assignments[meeting_id] = next_room 
        elif time_type == END:
            used_room = meeting_assignments[meeting_id]
            rooms.add(used_room)
        else:
            print "ERROR: unexpected time_type", time_type
    
    return num_rooms, meeting_assignments

def show_schedule(meetings, assignments):
    for m in meetings:
        room = assignments[m._id]
        print "Meeting(start=%d, end=%d) -> Room(%d)" % (m.start, m.end, room._id)

# input: list(Meeting)
# Meeting(start_time, end_time)
# start_time, end_time in integer interval [0, inf)
# output: meeting -> room
# room cannot take two simultaneous meetings
# use fewest rooms possible.
# all rooms are identifical

meetings = [
    Meeting(1, 8, 20),    
    Meeting(2, 0, 5),    
    Meeting(3, 1, 3),    
    Meeting(4, 3, 7),    
    Meeting(5, 4, 6),
]

num_rooms, meeting_assignments = schedule_meetings(meetings)
print "Rooms", num_rooms
show_schedule(meetings, meeting_assignments)
# print "Assignments", meeting_assignments
