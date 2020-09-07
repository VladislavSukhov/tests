import pytest
import os
import app.mod as m
import collections

class TestMain:
    
    def setup(self):
        print("method setup")
    
    
    def teardown(self):
        print("method teardown")
      
        
    @pytest.mark.parametrize("test_input,expected", [("2207 876234", True), ("827456862", False)])
    def test_check_document_existance(self, test_input, expected):
        assert m.check_document_existance(test_input) == expected


    @pytest.mark.parametrize("test_input,expected", [("2207 876234", "Василий Гупкин")])
    def test_get_doc_owner_name(self, test_input, expected):
        assert m.get_doc_owner_name(test_input) == expected


    def test_get_all_doc_owners_names(self):
        assert collections.Counter(m.get_all_doc_owners_names()) == collections.Counter(["Василий Гупкин", "Геннадий Покемонов", "Аристарх Павлов"])


    def test_remove_doc_from_shelf(self):
        assert m.remove_doc_from_shelf("11-2") == ["2207 876234"]


    @pytest.mark.parametrize("test_input,expected", [("4", ("4", True)),("3", ("3", False))])
    def test_add_new_shelf(self, test_input, expected):
        assert m.add_new_shelf(test_input) == expected
    
    
    def test_append_doc_to_shelf(self):
        assert m.append_doc_to_shelf("505", "2") == ["10006", "505"]
        assert m.append_doc_to_shelf("606", "3") == ["606"]
        
        
    @pytest.mark.parametrize("test_input,expected", [("10006",("10006", True)), ("55555",None)])
    def test_delete_doc(self, test_input, expected):
        assert m.delete_doc(test_input) == expected
        

       


if __name__ == '__main__':
    pytest.main()