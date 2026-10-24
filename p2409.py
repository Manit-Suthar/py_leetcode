class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days = 0 
        month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        alice_arrive = int(arriveAlice[:2])
        alice_leave = int (leaveAlice[:2])
        bob_arrive = int(arriveBob[:2])
        bob_leave = int (leaveBob[:2])

        alice_arriveDay = int(arriveAlice[3:])+sum(month[:alice_arrive-1])
        alice_leaveDay = int(leaveAlice[3:])+sum(month[:alice_leave-1])
        bob_arriveDay = int(arriveBob[3:])+sum(month[:bob_arrive-1])
        bob_leaveDay = int(leaveBob[3:])+sum(month[:bob_leave-1])

       
        start = max(alice_arriveDay,bob_arriveDay)
        end = min(alice_leaveDay,bob_leaveDay)
        days = end-start+1
        return max(0,days)

print(Solution().countDaysTogether("10-20", "12-22", "06-21", "07-05"))