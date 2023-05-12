# implementing new feature of performance tracking
class PerformanceManager:
    def track(self, employees, hours):
        print("Tracking Employee Performance")
        print("==============================")
        for employee in employees:
            employee.work(hours)
            print("------------------------")
