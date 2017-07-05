class call(object):
    def __init__(self, id, caller, number, time, reason):
        self.id = id
        self.caller = caller
        self.number = number
        self.time = time
        self.reason = reason
    def display_call(self):
        print "Call ID: {} | Caller Name: {} | Phone Number: {} | Time of Call: {} | Reason for Call: {}".format(self.id, self.caller, self.number, self.time, self.reason)

class call_center(object):
    def __init__(self, calls):
        self.calls = calls
        self.queue = len(calls)
    def add_call(self, call):
        self.calls.append(call)
        self.queue += 1
        return self
    def remove_first_call(self):
        del self.calls[0]
        self.queue -= 1
        return self
    def remove_by_number(self, num):
        for some_call in self.calls:
            if some_call.number == num:
                self.calls.remove(some_call)
                self.queue -= 1
        return self
    def display_info(self):
        print "Call Center Log\nQueue Length: {}".format(self.queue)
        for i in range(self.queue):
            print "{}. Caller Name: {} | Phone Number: {}".format( i+1, self.calls[i].caller, self.calls[i].number )
        return self

call1 = call(101, "Sam Zoeller", 3035032738, "4:30 PM", "Lunch Delivery")
call2 = call(102, "Harry Kioko", 9173456789, "1:45 AM", "Late Night Snack")
call3 = call(103, "Corinne Riley", 4576982741, "8:04 AM", "Breakfast Delivery")
grubhub = call_center([call1,call2,call3])

grubhub.display_info().remove_first_call().display_info().add_call(call1).display_info().remove_by_number(4576982741).display_info()
#call1.display_call()

