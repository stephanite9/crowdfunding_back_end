# Crowdfunding Back End
Stephanie Chan

## Planning:
### Concept/Name
Name Ideas - Relauncher, The Show Must Go On, Take Two, a crowdfunding app to bring back cancelled TV shows and movie franchises from the dead.

### Intended Audience/User Stories
{{ Varied audience - creatives looking for funds to make stories and get their ideas off the ground, producers looking for funding for projects that are already fleshed out, fans who want to support beloved media that ended too soon. }}

### Front End Pages/Functionality
- {{ Home Page }}
    - {{ Featured fundraisers }}
    - {{ Latest successful fundraisers }}
    - {{ Discover fundraisers - search by media type, location }}
- {{ Create New Fundraiser }}
    - {{ Form for fundraiser details }}
    - {{ Submit }}
    - {{ Validation error pages }}
- Display Fundaiser
  - Show all info about fundraiser
  - Show all current pledges
- Search specific fundraisers

### API Spec
{{ Fill out the table below to define your endpoints. An example of what this might look like is shown at the bottom of the page. 

It might look messy here in the PDF, but once it's rendered it looks very neat! 

It can be helpful to keep the markdown preview open in VS Code so that you can see what you're typing more easily. }}

| URL          | HTTP Method | Purpose               | Request Body | Success Response Code          | Authentication/Authorisation |
| ------------ | ----------- | --------------------- | ------------ | ------------------------------ | ---------------------------- |
| /fundraisers/ | GET|  Fetch all fundraisers  | JSON payload|  200  |
| /fundraisers/<pk>| GET | Fetch specific fundraiser| JSON payload |200
|/fundraisers/| POST | Create new fundraiser| JSON payload |201|Logged in user
|/fundraisers/<pk>| PUT | Update specific fundraiser| JSON payload |201|Logged in user
| /pledges/    |  GET | Fetch all the pledges | N/A (no body)  | 200     |
| /pledges/<pk>| GET | Fetch specific pledge| JSON payload |200
| /pledges/    |  POST | Create a new pledge | JSON payload | 201     | Logged in user |
| /pledges/<pk>  |  POST | Update a pledge | JSON payload | 201     | Logged in user |

### DB Schema
![]( {{ ./relative/path/to/your/schema/image.png }} )
