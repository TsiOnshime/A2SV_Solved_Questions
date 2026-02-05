class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        base_dict = {}

        for i in paths:
            parts = i.split()
            directory = parts[0]
            file_entries = parts[1:]

            for file_entry in file_entries:
                file_content = file_entry.split("(")
                filename = file_content[0]
                content = file_content[1][:-1]

                full_path = directory + "/" + filename

                # Only one check and append per content
                if content not in base_dict:
                    base_dict[content] = []
                base_dict[content].append(full_path)

        # Only return lists with more than one path
        result = []
        for paths in base_dict.values():
            if len(paths) > 1:
                result.append(paths)

        return result
