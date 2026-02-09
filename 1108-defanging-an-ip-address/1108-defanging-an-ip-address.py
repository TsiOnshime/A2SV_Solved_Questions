class Solution:
    def defangIPaddr(self, address: str) -> str:
        address=("[.]").join(address.split('.'))

        return address