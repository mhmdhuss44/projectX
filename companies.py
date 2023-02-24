from collections import namedtuple
from enum import Enum


class Companies(namedtuple("Companies", ["company_name", "company_number"]), Enum):
    """
  
    """

    BMC = "BMC", "69733"

    @staticmethod
    def get_company_name_by_key(company_number: str) -> Enum:
        """
      
        """
        company = next((result for result in Companies if result.company_number == company_number), None)
        if company is None:
            raise Exception(f"No company found with key [{company_number}].")
        return company