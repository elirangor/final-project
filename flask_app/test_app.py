import pytest
from app import app, client, db, collection
from bson.objectid import ObjectId

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()

    # Clean up and setup test database
    with app.app_context():
        db.drop_collection('mycollectiontest')
        collection.insert_one({'field1': 'test1', 'field2': 'test2'})

    yield client

    # Teardown test database
    with app.app_context():
        db.drop_collection('mycollectiontest')

def test_index(client):
    """Test the index page."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to the Flask MongoDB App" in response.data

def test_add_document(client):
    """Test adding a document."""
    response = client.post('/add', data={'field1': 'new_field1', 'field2': 'new_field2'})
    assert response.status_code == 302  # Redirect after POST
    assert collection.find_one({'field1': 'new_field1'}) is not None

def test_update_document(client):
    """Test updating a document."""
    document = collection.find_one({'field1': 'test1'})
    response = client.post('/update', data={'id': str(document['_id']), 'field1': 'updated_field1', 'field2': 'updated_field2'})
    assert response.status_code == 302  # Redirect after POST
    updated_document = collection.find_one({'_id': document['_id']})
    assert updated_document['field1'] == 'updated_field1'

def test_delete_document(client):
    """Test deleting a document."""
    document = collection.find_one({'field1': 'test1'})
    response = client.post('/delete', data={'id': str(document['_id'])})
    assert response.status_code == 302  # Redirect after POST
    assert collection.find_one({'_id': document['_id']}) is None
