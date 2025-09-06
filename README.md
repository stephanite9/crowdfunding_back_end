# Crowdfunding Back End
Stephanie Chan

## Planning:
### Concept/Name
The Show Must Go On, a crowdfunding app to bring back cancelled TV shows and movie franchises from the dead.

show-goes-on-app on Heroku

### Intended Audience/User Stories
Varied audience;
- creatives looking for funds to make stories and get their ideas off the ground
- producers looking for funding for projects that are already fleshed out
- fans who want to support beloved media that ended too soon

### Front End Pages/Functionality
- Home Page
    - Latest successful fundraisers (5 newest created fundraisers)
    - Trending fundraisers (Top 5 fundraisers with the most pledges)
    - Discover fundraisers - search by media type, location (TBA)
- Sign in page
    - Create new user account
- Create New Fundraiser
    - Form for fundraiser details
    - Submit
    - Validation error pages
- Display Fundaiser
  - Show all info about fundraiser
  - Show all current pledges
- Search specific fundraisers

### API Spec
Fill out the table below to define your endpoints. An example of what this might look like is shown at the bottom of the page. 

It might look messy here in the PDF, but once it's rendered it looks very neat! 

It can be helpful to keep the markdown preview open in VS Code so that you can see what you're typing more easily. 



| URL               | HTTP Method | Purpose                   | Request Body  | Success Response Code | Authentication/Authorisation |
| ----------------- | ----------- | ------------------------- | ------------- | --------------------- | ---------------------------- |
| /fundraisers/     | GET         | Fetch all fundraisers     | N/A (no body) | 200                   | Anyone                       |
| /fundraisers/<pk> | GET         | Fetch specific fundraiser | N/A (no body) | 200                   | Anyone                       |
| /fundraisers/     | POST        | Create new fundraiser     | JSON payload  |
| "title":          |
"description":
"goal":
"location":
"media":
"image":
"is_open":    | 201|Logged in user |
| /fundraisers/<pk>     | PUT         | Update specific fundraiser                    | JSON payload | 201                   |Logged in user, owner
| /fundraisers/latest   | GET         | Fetch top 5 newest fundarisers created        | N/A (no body) | 200                   | Anyone                       |
| /fundraisers/trending | GET         | Fetch top 5 fundraisers with the most pledges | N/A (no body) | 200             |Anyone
| /pledges/             | GET         | Fetch all the pledges                         | N/A (no body) | 200                   | Logged in user
| /pledges/<pk>         | GET         | Fetch specific pledge                         | N/A (no body) | 200                   | Logged in user
| /pledges/             | POST        | Create a new pledge                           | JSON payload 
"amount":
"comment":
"anonymous":
"fundraiser":  | 201                   | Logged in user               |
| /pledges/<pk>         | POST        | Update a pledge                               | JSON payload  | 201                   | Logged in user, owner               |
| /users/               | GET         | Fetch all users                               | N/A (no body) | 200                   | Logged in user
| /users/<pk>           | GET         | Fetch 1 user with id <pk>                     | N/A (no body) | 200                   | Logged in user
| /users/|POST|Create new user|JSON payload
"first_name": 
"last_name": 
"email": 
"password": 
"username": | 201|Anyone

### DB Schema
![]( database.drawio.svg )

### How To Register a New User and create a new fundraiser in Insomnia
1) To register a new user, POST to https://show-goes-on-app-c8366a7107fe.herokuapp.com/users/ where JSON payload body is:
  {
  "first_name": "<>",
  "last_name": "<>",
  "email": "<>",
  "password": "<>",
  "username": "<>"
  }

2) Generate auth token using POST to https://show-goes-on-app-c8366a7107fe.herokuapp.com/api-token-auth/ where JSON payload is:
  {
  "username": "<>",
	"password": "<>"
  }

3) To create a new fundraiser, use the generated auth token to "login" via the Auth tab. 
4) POST to https://show-goes-on-app-c8366a7107fe.herokuapp.com/fundraisers/ where the JSON payload is:
  {
  "title": "<>",
  "description":  "<>",
  "goal": "<>",
  "location": "<>",
  "media": "<>",
  "image": "<>",
  "is_open": "<>"
  }

### Screenshots
1) GET crowdfunding\img\GET_AllFundraisers_Success.JPG
2) POST crowdfunding\img\POST_NewFundraiser_Success.JPG
3) TOKEN crowdfunding\img\AuthToken_Success.JPG