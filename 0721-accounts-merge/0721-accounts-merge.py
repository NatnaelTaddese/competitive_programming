class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """

        # owners = defaultdict(list)
        owners = dict()
        visited = set()

        def find(self, x):
            if x == self.root[x]:
                return x
            self.root[x] = self.find(self.root[x])
            return self.root[x]
        
        adj_list = defaultdict(set)

        for account in accounts:
            name = account[0]
            first_email = account[1]

            for i in range(1, len(account)):
                email = account[i]
                owners[email] = name

                if i > 1:
                    adj_list[email].add(account[i - 1])
                    adj_list[account[i - 1]].add(email)
        
        # print(adj_list)

        # def dfs(email,emails):
        #     emails.append(email)
        #     visited.add(email)

        #     for neighbor in adj_list[email]:
        #         if neighbor not in visited:
        #             dfs(neighbor, emails)
        
        def dfs(email, emails):
            emails.append(email)
            visited.add(email)
            
            for neighbor in adj_list[email]:
                if neighbor not in visited:
                    dfs(neighbor, emails)
        
        result = []
        
        # for email in owners:
        #     if email not in visited:
        #         emails = []

        #         dfs(email, emails)
        #         result.append([owners[email]] + sorted(emails))
        
        for email in owners:
            if email not in visited:
                emails = []
                dfs(email, emails)
                result.append([owners[email]] + sorted(emails))
        
        return result

        """
        {
            3 : [a,b] + [f, g, h] + [z , x, y]
            2 : [c]

            4 : [d]

        }
        {
            john : [(a,b)0 p:3,(a,f,g,h)1 ,(c)2,(z,x,y,a)3] -> () ()
            mary : (d)
        }

        {
            a : [b , f, y]
            b : [a]
            f : [a, g]
            g : [f, h]
            h : [g]

            c : []

            z : [x]
            x : [z, y]
            y : [x, a]

        }
        
        """