class Solution:
    def countValidWords(self, sentence: str) -> int:
        punctuation = {"!", ".", ","}
        result = 0

        for word in sentence.split():
            valid = True
            hyphens = 0

            for i, char in enumerate(word):
                if char.isdigit():
                    valid = False
                    break

                if char == "-":
                    hyphens += 1
                    if (
                        hyphens > 1
                        or i == 0
                        or i == len(word) - 1
                        or not word[i - 1].islower()
                        or not word[i + 1].islower()
                    ):
                        valid = False
                        break

                if char in punctuation and i != len(word) - 1:
                    valid = False
                    break

            if valid:
                result += 1

        return result