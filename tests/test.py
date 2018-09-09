import unittest






class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.orders = {}
        self.order = {}


    def test_get_all_orders(self):
        response = requests.get('/api/v1/orders')
        self.assertEqual(response.status_code, 200)


    def test_get_one_order(self):
        res = requests.get('/api/v1/orders/<string:id>')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res.json()['order']), 1)


    def test_post_an_order(self):
         pos = requests.post('/api/v1/orders', self.orders)
         self.assertEqual(pos.status_code, 201)


    def test_update_order(self):
        up = requests.put('/api/v1/orders/<string:id>', self.order)
        self.assertEquals(up.status_code, 202)



if __name__ == '__main__':
        unittest.main()
