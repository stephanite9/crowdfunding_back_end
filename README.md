# Crowdfunding Back End
{{ Stephanie Chan }}

## Planning:
### Concept/Name
{{ Name Ideas - Relauncher, The Show Must Go On, Take Two, A crowdfunding app to bring back cancelled TV shows and movie franchises from the dead. }}

### Intended Audience/User Stories
{{ Varied audience - creatives looking for funds to make stories and get their ideas off the ground, producers looking for funding for projects that are already fleshed out, fans who want to support beloved media that ended too soon. }}

### Front End Pages/Functionality
- {{ Home Page }}
    - {{ Featured fundraisers }}
    - {{ Successful fundraisers }}
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
| /fundraisers |             |                       |              |                                |                              |
|              |
| /pledges/    |             | Fetch all the pledges | GET          | N/A (no body)                  | 200                          |
| /pledges/    |             | Create a new pledge   | POST         | JSON payload {"fundraiser_id"} | 201                          | Logged in user |

### DB Schema
![]( {{ ./relative/path/to/your/schema/image.png }} )