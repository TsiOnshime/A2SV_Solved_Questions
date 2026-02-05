class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dictionary = {}

        for entry in cpdomains:
            count, domain = entry.split()
            count = int(count)
            subdomains = domain.split(".")
            
            for j in range(len(subdomains)):
                subdomain = ".".join(subdomains[j:])
                dictionary[subdomain] = dictionary.get(subdomain, 0) + count

        return [f"{v} {k}" for k, v in dictionary.items()]
