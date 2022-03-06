class Solution:

    def filter_local_name(self, local_name):
        local = local_name.replace(".", "")
        filtered = []
        for char in local:
            if char == "+":
                break
            else:
                filtered.append(char)

        return "".join(filtered)

    def numUniqueEmails(self, emails) -> int:
        addresses = set()

        for email in emails:
            local_name, domain_name = email.split("@")
            filtered_local_name = self.filter_local_name(local_name)
            final_email = filtered_local_name + "@" + domain_name
            addresses.add(final_email)

        return len(addresses)
