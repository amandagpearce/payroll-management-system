# implementing new feature of performance tracking
class PerformanceManager:
    def track(self, employees, hours):
        print("Tracking Employee Performance")
        print("==============================")
        for employee in employees:
            # employee.work(hours)
            status = employee.work(hours)
            print(f"{employee.name} : {status}")
            print("------------------------")


class ManagerRole:
    def work(self, hours):
        print(
            f"{self.name} Manager is overseeing the project for {hours} hours"
        )


class DeveloperRole:
    def work(self, hours):
        print(
            f"""{self.name} Developer is working on the project for {hours}
            hours"""
        )


class SalesRole:
    def work(self, hours):
        print(
            f"""{self.name} Salesperson is handling client calls for {hours}
            hours"""
        )


class WorkerRole:
    def work(self, hours):
        print(f"{self.name} Intern has completed their tasks in {hours} hours")
