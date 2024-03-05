class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        """
        1. spli the integer by space, store the count stor the domain
        2. spli the domain by . join the domains and them to the dictionary
        3. Run a key value iteration and return the list
        """
        map_dict = {}
        for domains in cpdomains:
            domain = domains.split(' ')
            dom = domain[1].split('.')
            for i in range(len(dom)):
                key = '.'.join(dom[i:])
                if key not in map_dict:
                    map_dict[key] = int(domain[0])
                else:
                    map_dict[key] += int(domain[0])

        return [str(value) + ' ' + key for key, value in map_dict.items()]