#!/usr/bin/env python3
import importlib.util,pathlib,unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]
def load(name,path):
    s=importlib.util.spec_from_file_location(name,ROOT/path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
counts=load('counts','gbr-render-stats/counts.py');dates=load('dates','project-setup/offset_date.py')
class Tools(unittest.TestCase):
    def test_counts(self):
        r=counts.measure('<g>A</g><b>BC</b><r>DEFG</r>');self.assertEqual(r['counts'],{'green':1,'blue':2,'red':4});self.assertEqual(r['total'],7);self.assertAlmostEqual(sum(r['percentages'].values()),100)
    def test_spaces_punctuation(self):self.assertEqual(counts.measure('<g>A, </g>')['total'],3)
    def test_wrappers_and_entity(self):self.assertEqual(counts.measure('<L1><g>&amp;</g></L1>\n<b>🤝é</b>')['counts'],{'green':1,'blue':3,'red':0})
    def test_invalid_tags(self):
        for text in ['<g>X','<g>A<b>B</b></g>','<x>A</x>','word<g>A</g>','<g a="1">A</g>','<g></g>','<!DOCTYPE g><g>A</g>','<!--note--><g>A</g>']:
            with self.subTest(text=text),self.assertRaises(ValueError):counts.measure(text)
    def test_reference_invalid(self):
        for reference in [(1,2,3),(-1,20,81),(float('nan'),20,5),(float('inf'),20,5)]:
            with self.subTest(reference=reference),self.assertRaises(ValueError):counts.measure('<g>A</g>',reference)
    def test_custom_reference(self):self.assertEqual(counts.measure('<g>A</g>',(100,0,0))['delta_percentage_points']['green'],0)
    def test_positive_before(self):self.assertEqual(dates.derive('2026-11-20',7),'2026-11-13')
    def test_negative_after(self):self.assertEqual(dates.derive('2026-11-20',-3),'2026-11-23')
    def test_date_invalid(self):
        for anchor,offset in [('bad',3),('2026-02-30',1),('2026-11-20',True)]:
            with self.subTest(anchor=anchor,offset=offset),self.assertRaises(ValueError):dates.derive(anchor,offset)
if __name__=='__main__':unittest.main()
