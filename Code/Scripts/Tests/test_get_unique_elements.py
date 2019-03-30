import unittest
from Code.Scripts.GetUnique import get_unique_elements


class Test_get_unique_elements(unittest.TestCase):

    def test_get_unique_elements(self):
        element_id, created_at, text = "id", "created_id", "text"
        param = text
        before_dict = [
            {
                element_id: "1000000",
                created_at: "Thu Feb 28 14:51:59 +0000 2019",
                text: "pm narendra modi explains the relevance of communication at national youth parliament festival awards 2019"
            },
            {
                element_id: "1000001",
                created_at: "Sat Mar 02 06:50:39 +0000 2019",
                text: "under prime minister narendra modi s ambitious scheme  national health protection  scheme  10 crore poor families will be given a cover of rs  5 lakh per family annually  bjpvijaysankalpbikerally"
            },
            {
                element_id: "1000002",
                created_at: "Sun Mar 03 17:19:49 +0000 2019",
                text: "pm narendra modi explains the relevance of communication at national youth parliament festival awards 2019"
            }

        ]
        expected_result = [{
            element_id: "1000000",
            created_at: "Thu Feb 28 14:51:59 +0000 2019",
            text: "pm narendra modi explains the relevance of communication at national youth parliament festival awards 2019"
        },
            {
                element_id: "1000001",
                created_at: "Sat Mar 02 06:50:39 +0000 2019",
                text: "under prime minister narendra modi s ambitious scheme  national health protection  scheme  10 crore poor families will be given a cover of rs  5 lakh per family annually  bjpvijaysankalpbikerally"
            }
        ]
        result = get_unique_elements(before_dict, param)
        print(result)
        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    unittest.main()
