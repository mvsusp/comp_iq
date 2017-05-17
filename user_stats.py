import scipy.stats as st
import math

class UserStats(object) :

    def __init__(self, users, firms) :
        self.firms = firms
        self.users_per_firm = {}
        for firm in firms :
            firm_id = firm["firm_id"]
            self.users_per_firm[firm_id] = { u["user_id"]: u for u in users if u["firm_id"] == firm_id }

    def similar_firm_ids(self, compiq_index):
        return [ firm["firm_id"] for firm in self.firms if math.fabs(compiq_index - firm["compiq_index"]) < 0.15 ]

    def get_another_users_data_from_firms(self, user_id, firm_ids, field):
        data = []
        for firm_id, users in self.users_per_firm.items():
            if firm_id in firm_ids:
                for id, user in users.items():
                    if id != user_id:
                        data.append(user[field])
        return data

    def calculate_stats(self, user) :
        """
Compute the percentile the user's base and bonus are at compared to the base and bonus records for *this user's title* across all "similar" firms as well as other users' records from this user's same firm, but not including the user's own record.
        """
        firm_id = user['firm_id']
        user_id = user['user_id']

        compiq_index = self.firms[user["firm_id"]]["compiq_index"]
        firm_ids = self.similar_firm_ids(compiq_index)


        bases = self.get_another_users_data_from_firms(user_id, firm_ids, "base")
        bonuses = self.get_another_users_data_from_firms(user_id, firm_ids, "bonus")

        user_data = self.users_per_firm[firm_id][user_id]

        percentile_base = st.percentileofscore(bases, user_data["base"])
        percentile_bonus = st.percentileofscore(bases, user_data["bonus"])

        return { "user_id": user_id, "user_base": user_data["base"], "user_bonus": user_data["bonus"], "percentile_base": percentile_base, "percentile_bonus": percentile_bonus }
