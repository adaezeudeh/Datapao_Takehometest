import unittest
import os
from office_sess_analytics import  get_data,process_time_entries, calculate_average_and_rank, find_longest_work_session 



class TestMyFunctions(unittest.TestCase):
    def setUp(self):
        # Set up your data or any initial configurations
        file_path = 'Data/datapao_homework_2023.csv'
        data = get_data(file_path)
        self.processed_time = process_time_entries(data)
        self.ranked_data = calculate_average_and_rank(self.processed_time)
        self.longest_session_data = find_longest_work_session(data)
        pass

    def test_empty_dataset(self):
        # Test for an empty dataset
        empty_data_1 = []
        empty_data_2 = {}
        self.processed_time = process_time_entries(empty_data_1)
        self.ranked_data = calculate_average_and_rank(empty_data_2)
        self.longest_session_data = find_longest_work_session(empty_data_1)
        self.assertEqual(self.processed_time, {})  # Assert that processing empty data returns an empty dictionary
        self.assertEqual(self.ranked_data, [])  # Test that average rank result is an empty list
        self.assertIsNone(self.longest_session_data[0])  # Test that user_with_max_time is None for an empty dataset

    def test_process_time_entries(self):
        self.assertIsInstance(self.processed_time, dict) # Check if the result is a dictionary

        # Check if each user's data contains the expected keys
        expected_keys = {'time', 'days', 'last_action'}
        self.assertTrue(all(set(user_data.keys()) == expected_keys for user_data in self.processed_time.values()))

        # Check if 'time' values in the processed data are floats
        for user_data in self.processed_time.values():
            self.assertTrue(isinstance(user_data['time'], float))

    def test_calculate_average_and_rank(self):
        
        # Check if the result is a list of tuples
        self.assertIsInstance(self.ranked_data, list)
        self.assertTrue(all(isinstance(item, tuple) for item in self.ranked_data))

        # Check if each tuple contains expected information (user_id, time, days, average_per_day, rank)
        for item in self.ranked_data:
            self.assertEqual(len(item), 5)

        # Check if the 'days' attribute is a non-negative integer and 'average_per_day' is a float in the result
        for item in self.ranked_data:
            self.assertIsInstance(item[2], int)  
            self.assertIsInstance(item[3], float)  

    def test_find_longest_work_session(self):
        # Check if the returned user ID is a string and the time is a non-negative float or int
        result_user, result_time = self.longest_session_data
        self.assertIsInstance(result_user, str)
        self.assertIsInstance(result_time, (float, int))

    def test_csv_file_existence(self):
        # Check if the CSV files exist after running the main function
        self.assertTrue(os.path.isfile('output/first.csv'))
        self.assertTrue(os.path.isfile('output/second.csv'))



if __name__ == '__main__':
    unittest.main()
