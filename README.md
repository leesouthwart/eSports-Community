# eSportsCommunity

A mock social media site for gamers. The main component of this site is the 'Issue Tracker', that allows users to post, edit, and pay for bug fixes and content suggestions. The not-quite-developed 'social media' site is
not the focus of the project, the issue tracker is. However it does have basic functionality like user profiles, posts and commenting.

#### Note for Graders

To test the site you can log in using this account (please note it is case sensitive):

test - test123




## UX/UI

The idea of the mock-up site is that it is a social media site for gamers to find other people to team with. The main focus of this project is actually the 'issue tracker', the mockup site that is built around it is just for a bit of fun and to make it look more like a complete project instead of just an empty site with an issue tracker added onto it.

#### User Stories

* A new user comes to the site. They can use the register links found in the navbar or on the main home page to sign up with his email address. After this they will have full access to the site with a default profile.
* Once registered, users can change their profile to set a unique profile picture and bio. They can also change their location, and a 'available to team' field, to let others know if they want to be contacted about teaming.
* Logged in users can browser the Timeline, a page where all users posts can be found, and the issue tracker where they can check out other peoples bug reports and content suggestions. Users can comment on all of these. They can upvote/downvote bugs, and upvote content suggestions by paying £1 via a one time stripe payment.

##### Design

The design for the issue tracker was kept as simple as possible, as I wanted the page to be an informative page, I didn't want to add any images or design that would be confusing in anyway. They layout of the issue tracker pages are logical and straightfoward to allow for easy navigation.

## Features

* Login/Authentication - Users can register to the site and login/out. Being logged in is needed to post onto the issue tracker, and to make blog posts to their own profile.
* Profiles - Each user has a unique profile that they can edit to be unique for themselves. They can edit a bio, a location and a profile picture. They can also create blog posts which will be posted onto the timeline.
* Timeline - A page displaying all users posts, displaying newer posts first. 
* Database page - Graphs displaying the amount of issues in the database that are in each of the statuses('backlog', 'in progress', 'completed'). The amount of issues tackled per day/week/month is mock data but the graphs displaying the current amount of issues in the database has data taken from the sqlite database. The graphs are created using googles javascript charts.

###### Issue Tracker

The issue tracker is the main feature of this site and is the focus of the project. The tracker is split into two sections, namely Bug Reports and Content Suggestions.

Content Suggestions can be posted by anyone who is logged in. Users can pay a £1 single payment to upvote a content suggestion. This uses Stripe checkout to take payments. Users can leave comments on each content suggestion.

Bug Reports can also be posted by logged in users. They work the same as content suggestions except it is free to upvote them, and users can downvote too.

The issues can be sorted by 3 metrics, upvotes, views, and by newest posts. They can also be filtered by their current status, for example if it is in the backlog, or completed. Users can also search, which will search for a match within the issues title or content with whatever is inputted.

## Technologies used

* Python/Django - The main fullstack framework used to create this site.
* Javascript/Jquery - For some DOM manipulation, specifically changing classes on click and for the home page carosel.
* Slick - Jquery plugin for the carosel on the home page.
* Google Charts - Javascript charts for the graphs page.
* whitenoise - serving css/js files to heroku.
* AWS S3 - image storage and serving to heroku.
* HTML/CSS - basic layout/styling
* Bootstrap - Easy responsive design
* sqlite - Database for saving the models/objects
* Heroku - Website hosting.

## Testing

I chose to manually test the functionality of the site to ensure that everything worked as expected.

I performed extensive manual tests which I documented in the Tests.md file.

## Deployment

The site is deployed on Heroku and can be found at https://esports-community.herokuapp.com/

There are a few differences between the deployed and local version. Firstly, on the local version the code to allow Whitenoise to store static files has been commented out (line 57 and line 145 in esportsCommunity/settings.py). On the deployed version, the 'import env' in settings.py (line 14) has been commented out, as the env variables have been set in the heroku config vars.

The following vars are set as config vars on the heroku dashboard

* AWS_ACCESS_KEY_ID
* AWS_SECRET_ACCESS_KEY
* AWS_STORAGE_BUCKET_NAME
* DISABLE_COLLECTSTATIC: 1
* EMAIL_HOST_PASSWORD
* EMAIL_HOST_USER
* SECRET_KEY
* STRIPE_PUBLISHABLE
* STRIPE_SECRET

