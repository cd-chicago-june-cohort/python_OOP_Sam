class patient(object):
    def __init__(self, name, patient_id, allergies):
        self.patient_id = patient_id
        self.name = name
        self.allergies = allergies
        self.bednum = None
    
class hospital(object):
    def __init__(self, name, capacity, patients):
        self.name = name
        self.capacity = capacity
        self.patients = patients
        self.beds = []
    def admit(self, patient):
        if len(self.patients) == self.capacity:
            print "Sorry. The hospital is full."
        else:
            self.beds.append(patient)
            patient.bednum = self.beds.index(patient) + 1
            print "{} has been admitted".format(patient.name)
            self.patients.append(patient)
        return self
    def discharge(self, patient):
        self.patients.remove(patient)
        self.beds.remove(patient)
        patient.bednum = None
        for item in self.patients:
            item.bednum = self.beds.index(item) + 1
        print "{} has been discharged".format(patient.name)
        return self
    def hospital_log(self):
        for p in self.patients:
            print p.name, p.bednum
        return self

patient1 = patient("Adam Smith", 15, "ibuprofen")
patient2 = patient("Jane Doe", 16, "peanuts")
patient3 = patient("John McDonald", 17, "latex")
hospital1 = hospital("The Hospital", 3, [])

hospital1.admit(patient2).admit(patient3).admit(patient1).hospital_log().discharge(patient3).hospital_log()

    