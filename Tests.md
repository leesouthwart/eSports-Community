# Testing

I did extensive manual testing on every aspect of the site that I can think of. I will list all tests I did below, including bugs I found that had to be fixed.

### Home page 

* Tested the navbar links worked and redirected to the correct url
* Tested the navbar worked as expected on smaller responsive screens
* Made sure the background image was an appropriate file size to aid with loading times
* Checked the links in the carosel/slider to see if they went to the right place.
* Checked the links in the footer redirected correctly and in new tabs.
* Tested the "if authenticated" statements worked.

### Timeline

* Checked the posts are displayed newest first.
* Checked pagination works when there are more than 10 posts on the timeline.
* Ensured clicking the post takes you to the correct id 
* Made sure responsive design looks good. 

### Database 

* Made sure the design and layout is fine
* checked the design and layout on responsive sizes
* Tested the data for the bug and content status charts is coming from the backend database.

### Issue Tracker

* Tested that the upvote and downvote system works.
* Tested the Stripe functionality works for buying upvotes for content suggestions
* Checked pagination when there is more than 5 bugs or content suggestions
* Checked pagination for when there is more than 5 comments on the specific bug or content
* Ensured responsive design worked well
* Made sure users can create new issues by clicking the 'new content'/'new bug' button
* Made sure that users can edit their own posts, or anyones posts if they are admin
* Checked that users cannot edit the url they are on to end up on someone elses issue, then edit it when its not their own.
* Tested deleting issues on the frontend

### Profile 

* Tested that profile images can be changed
* Tested that profile model and user model are linked properly
* Made sure editing profile doesnt break when leaving one field blank
* Made sure editing profile works when all fields are filled
* Tested posting and editing posts worked without issue
* Checked that users cannot edit the url to allow them to edit someone elses post 
* Checked the layout on responsive screen sizes

### Email and Password reset

* Checked layouts of all the password reset views on responsive screen sizes
* Made sure the emails were being sent and being recieved correctly


All tests were run on both an admin and a regular user 



