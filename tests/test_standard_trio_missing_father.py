#!/usr/bin/env python
# encoding: utf-8
"""
test_standard_trio_missing_father.py

Test the family parser with a missing father.

FAM file looks like:

#Standard trio
#FamilyID       SampleID        Father  Mother  Sex     Phenotype
healthyParentsAffectedSon       proband father  mother  1       2
healthyParentsAffectedSon       mother  0       0       2       1

Should raise exception since father is not in family.

Created by Måns Magnusson on 2014-05-08.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

import sys
import os
from tempfile import NamedTemporaryFile
import pytest
from ped_parser import parser
from ped_parser.exceptions import PedigreeError


class TestTrio(object):
    """Test class for testing how the individual class behave"""
    
    def setup_class(self):
        """Setup a standard trio with extra column in the 'proband' row."""
        trio_lines = ['#Standard trio\n', 
                    '#FamilyID\tSampleID\tFather\tMother\tSex\tPhenotype\n', 
                    'healthyParentsAffectedSon\tproband\tfather\tmother\t1\t2\n',
                    'healthyParentsAffectedSon\tmother\t0\t0\t2\t1\n', 
                    ]
        self.trio_file = NamedTemporaryFile(mode='w+t', delete=False, suffix='.vcf')
        self.trio_file.writelines(trio_lines)
        self.trio_file.seek(0)
        self.trio_file.close()
        
    
    def test_standard_trio_missing_father(self):
        """Test if the file is parsed in a correct way."""
        with pytest.raises(PedigreeError):
            family_parser = parser.FamilyParser(open(self.trio_file.name, 'r'))


def main():
    pass


if __name__ == '__main__':
    main()

