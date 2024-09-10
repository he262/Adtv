Feature: Adtv data test

    Scenario Outline: Test the data for adtv
    Given the api url is <base_url>
    And I append the following parameters
        | param_name | param_value |
        | qadItems   | ADTV_3M_EUR |
        | date       | <Date>      |

    When I make an api request
    Then save api response in <CSV_File>
    When pivot api data at <CSV_File> and <after_pivot_data>

    Examples:
        | base_url                                                                    | Date       | CSV_File                                         | after_pivot_data                               |
        | http://brutus2.bat.ci.dom/sidwebapi/api/Security/getSecurityAttributeCSVETL | 2024-03-18 | Features\\Data\\Adtv_api_response_18_03_2024.csv | Features\\Data\\adtv_pivot_data18_03_2024.csv  |
        | http://brutus2.bat.ci.dom/sidwebapi/api/Security/getSecurityAttributeCSVETL | 2023-12-18 | Features\\Data\\Adtv_api_18_12_2023.csv          | Features\\Data\\adtv_pivot_data_18_12_2023.csv |

