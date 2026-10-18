import unittest
import medical_data_visualizer
import matplotlib as mpl

class DataVisualizerTestCase(unittest.TestCase):
    def setUp(self):
        self.fig = medical_data_visualizer.draw_cat_plot()
        self.ax = self.fig.axes[0]

    def test_cat_plot(self):
        self.assertEqual(type(self.fig), mpl.figure.Figure, "Expected draw_cat_plot to return a figure object.")
        actual = []
        for p in self.ax.patches:
            actual.append(round(p.get_height(), 2))
        expected = [25, 27, 21, 41, 5779, 4434, 467, 303, 5121, 4712, 412, 182]
        self.assertEqual(actual[:12], expected, "Expected bar chart values to be correct.")

    def test_heat_map(self):
        fig = medical_data_visualizer.draw_heat_map()
        self.assertEqual(type(fig), mpl.figure.Figure, "Expected draw_heat_map to return a figure object.")

if __name__ == "__main__":
    unittest.main()