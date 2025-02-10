from unittest.mock import patch, MagicMock
from app.services import admin_service
import uuid
from bson import ObjectId

class TestAdminService:
    @patch('app.extensions.mongodb.mongo_con.getDb')
    def test_get_list(self, mock_db):
        mock_admin_users = MagicMock()
        mock_admin_list = [{"_id" : "1"}, {"_id" : "2"}]
        mock_admin_users.find.return_value = mock_admin_list
        mock_db.return_value.admin_users = mock_admin_users
        admin_list = admin_service.get_list()
        assert len(admin_list) == 2
        assert admin_list == mock_admin_list
        
    @patch('app.extensions.mongodb.mongo_con.getDb')
    def test_create_admin(self, mock_db):
        mock_admin_users = MagicMock()
        mock_admin_data = {"_id" : 1, "name" : "rahul"}
        mock_admin_users.insert_one = MagicMock()
        mock_db.return_value.admin_users = mock_admin_users
        admin_service.create_admin(mock_admin_data)
        mock_db.return_value.admin_users.insert_one.assert_called_with(mock_admin_data)
        assert mock_db.return_value.admin_users.insert_one.call_count == 1

    @patch('app.extensions.mongodb.mongo_con.getDb')
    def test_check_admin_by_email(self, mock_db):
        mock_admin_users = MagicMock()
        mock_admin_users.count_documents = MagicMock()
        mock_admin_users.count_documents.return_value = 5
        mock_db.return_value.admin_users = mock_admin_users
        test_email = "test@mail.com"
        result_true = admin_service.check_admin_by_email(test_email)
        mock_db.return_value.admin_users.count_documents.assert_called_with({"email" : test_email})
        assert mock_db.return_value.admin_users.count_documents.call_count == 1
        assert result_true == True

        mock_admin_users.count_documents.return_value = 0
        result_false = admin_service.check_admin_by_email(test_email)
        mock_db.return_value.admin_users.count_documents.assert_called_with({"email" : test_email})
        assert mock_db.return_value.admin_users.count_documents.call_count == 2
        assert result_false == False

    @patch('app.extensions.mongodb.mongo_con.getDb')
    def test_get_admin_by_id(self, mock_db):
        mock_admin_users = MagicMock()
        mock_admin_users.find_one.return_value = {"_id" : "1"}
        mock_db.return_value.admin_users = mock_admin_users
        admin_id = str(uuid.uuid4().hex[:24])
        admin_info = admin_service.get_admin_by_id(admin_id)
        assert admin_info ==  {"_id" : "1"}
        mock_db.return_value.admin_users.find_one.assert_called_with({"_id" : ObjectId(admin_id)})


        






