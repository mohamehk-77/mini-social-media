# mini-social-media website

## Description

- [x] User registration and login (with email verification)
- [ ] Add a profile page for each user with their posts, comments, likes etc.
- [ ] Allow users to create new posts from the homepage or their profile page
- [ ] Implement markdown support in post content
- [ ] Show rendered HTML below the markdown input field
- [ ] Use a library like marked.js for this
- [ ] Make sure it's securely embedded into your app
- [ ] Only allow trusted users/admins to use the renderer
- [ ] Research how other platforms handle this security concern
- [ ] Look at OWASP recommendations on Markdown usage
- [ ] Consider using something like Remarkable instead of Marked if you need more control over parsing rules
- [ ] Commenting system where users can comment on posts
- [ ] Notify the author of a post when someone replies to them
- [ ] Limit number of characters per comment to X
- [ ] Liking system for posts
- [ ] Display number of likes next to each post
- [ ] Let users 'like' multiple times if they change their mind
- [ ] If a user deletes their account, remove all associated likes
- [ ] Dashboard for admins to manage the site:
- [ ] View list of registered users
- [ ] Filter by username, email, date joined
- [ ] Moderate user accounts
- [ ] Ban/delete users who are spamming/behaving badly
- [ ] Send notifications to users about being banned/deleted
- [ ] Manage posts
- [ ] Approve/reject pending posts
- [ ] Delete posts that violate community guidelines
- [ ] Provide feedback to authors of rejected posts

# backend Application

- [x] Set up Express server using python Flask framework
- [x] Create database schema using SQLAlchemy ORM  
- [x] Implement authentication middleware to protect routes
- [x] Implement password hashing using Bcrypt
- [x] Configure session management with cookies and Redis
- [x] Write tests for models and views using pytest
- [x] Deploy application

# frontend Application  

- [x] Build static files using Webpack (html &CSS & JavaScript)
- [x] Implement ReactJS as the main client side library
- [x] Design components using React Components  
- [x] Connect React components to Redux store using Redux
- [x] Implement routing using React Router v4
- [x] Style application using CSS modules
- [x] Use markdown rendering in textareas for easy content creation
- [x] Implement image upload feature using Cloudinary or similar service
