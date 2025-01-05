BASE_URL= "http://localhost:5000"
from app import app
from models import db, Contacts
from faker import Factory
from faker import Faker


fake = Faker()

def setup_module(module):
    pass


def teardown_module(module):
    pass


def test_get_contacts_is_list(client):
    response = client.get(BASE_URL + "/api/contacts")
    contacts = response.get_json()
    assert isinstance(contacts, list)


def test_get_contacts1(client):
    response = client.get(BASE_URL + "/api/contacts")
    assert response.status_code == 200


def test_delete_contact(client):
    # Create a contact before trying to delete it
    new_contact = {
        "name": "John",
        "surname": "Doe",
        "email": "john.doe@example.com",
        "phone": "123-456-7890"
    }
    create_response = client.post(BASE_URL + "/api/contacts", json=new_contact)
    created_contact = create_response.get_json()  # Get the response of the created contact
    contact_id = created_contact['id']  # Retrieve the ID of the newly created contact
    
    # Now delete the contact
    response = client.delete(BASE_URL + f"/api/contacts/{contact_id}")
    assert response.status_code == 204  



def test_post__create_contact(client):
    new_contact = {
        "name": fake.first_name(),
        "surname": fake.last_name(),
        "email": fake.email(),  # This ensures a unique email
        "phone": fake.phone_number()
    }
    
    response = client.post(BASE_URL + "/api/contacts", json=new_contact)
    
    assert response.status_code == 201  
    
    # Ensure the response contains the contact data
    created_contact = response.get_json()
    assert "id" in created_contact  
    assert created_contact["name"] == new_contact["name"]  
    assert created_contact["surname"] == new_contact["surname"]  
    assert created_contact["email"] == new_contact["email"]  
    assert created_contact["phone"] == new_contact["phone"]  


def test_get_posts_contains_title(client):
    response = client.get(f"{BASE_URL}/posts")
    posts = response.get_json()
    if posts:  # If posts is not empty
        assert 'title' in posts[0]

def test_get_posts_contains_body(client):
    response = client.get(f"{BASE_URL}/posts")
    posts = response.get_json()
    if posts:
        assert 'body' in posts[0]

        