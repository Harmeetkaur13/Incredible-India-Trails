# Incredible-India-Trails

## Overview
Incredible India Trails is a web application designed to showcase the beauty and diversity of travel destinations across India. The platform allows users to explore various destinations, read reviews, and share their own travel experiences. It provides full CRUD functionality, enabling users to create, read, update, and delete Reviews efficiently. The primary goal of the project is to provide a comprehensive and user-friendly platform for travelers to discover new places, share their adventures and experiences  with others.
![ screenshot of the project](static/images/myprject.webp)
-The website was deployed to Heroku and can be found [here](https://incredibleindiatrails-c2197d02c6c5.herokuapp.com/).

## UX Design Process
- **Link to User Stories in GitHub Projects:**
  - #### Agile methodology
  - Agile methodology is "a set of methods and practices where solutions evolve through collaboration between self-organizing,   cross-functional teams" ([reference](https://www.agilealliance.org/agile-essentials/)).
  - A project board was set-up to keep track of user stories. Each user story was assigned a 'MoSCoW' prioritisation (must have, should have, could have, won't have) tag. The board can be found
  - [\[Link to the GitHub Projects kanban board.\]](https://github.com/users/Harmeetkaur13/projects/15)
- **Wireframes:**
  - Home Page- 
  - ![ screenshot of the wireframe home](static/images/wireframeHomepage.webp)
  - View Destinaion Page
  - ![ screenshot of wireframe of View Destination page](static/images/wireframeViewdestination.webp)
- **Design Rationale:**
  - The layout emphasises simplicity and readability, with Bootstrap 5 providing a responsive design. The colour scheme adheres to WCAG guidelines for contrast, and the typography uses accessible fonts for clarity.
  - Accessibility considerations include keyboard navigation and screen reader support, ensuring usability for users with diverse needs.
- **Typography**
  - Google fonts were used to source the font styles.
  - Sans-serif is considered the best type of font to read for those who have dyslexia or  autism so only sans-serif type fonts were chosen.
  - Since the website is for travelers and contributed to by travelers, a handwritten style of font was used for the title to signify that this is a more casual, user-friendly website. The "Lato" font was chosen for its clean and modern feel.
  - For the content of the website, "Roboto" was chosen as a cleaner font which is easier to read, while still being slightly softer on the eye. 
  **Color Palette:**
  - These are some colors I have used for this project, color picked by https://imagecolorpicker.com/?utm_content=cmp-true
  - ![ color palette](static/images/colorpalette.webp)
- **Reasoning For Any Final Changes:**
  - Added the collapse option for the description on view destination page. The reason behind this ws on mobile screens this was affecting the performace on lighthouse  due to its large layout. This change really enhanced the performance.
  - Added pagination for the search and category filter. 

## Key Features
1. Admin Interface:
- Description: Admins have a customized interface to manage destinations, reviews, and user feedback.
- Value: Simplifies the management of content and user interactions on the platform.
- ![ Click to see](static/images/featureAdmin.webp)

2. Search and Filter:
- Description: Users can search for destinations and filter them by categories.
- Value: Makes it easy for users to find specific destinations based on their preferences.
- ![ Click to see search feature](static/images/featureFilterbySearch.webp)
- ![ Click to see Category feature](static/images/featureFilterbyCategoty.webp)

3. User Authentication and notify:
- Description: Users can sign up, log in, and log out securely.
- Value: Ensures that only registered users can add reviews and destinations, enhancing security and user accountability.
- ![ Click to see SignUp feature](static/images/featureSignup.webp)
- ![ Click to see Conforming SignIn feature](static/images/featureSignIn.webp)
- ![ Click to see Conforming SignOut feature](static/images/featureSignout.webp)

4. Review System:
- Description: Users can leave reviews for destinations, including ratings and comments.
- Value: Allows users to share their experiences and helps others make informed decisions.
- ![ Click to see login Required feature](static/images/featureLoginRequiredToAddReview.webp)
- ![ Click to see Add Review feature](static/images/featureAddReview.webp)
- ![ Click to see Edit/Delete Review feature](static/images/featureEditdeleteReview.webp)

5. Image Carousel:
- Description: Each destination page features an image carousel to showcase multiple images.
- Value: Enhances the visual appeal and provides a better user experience by displaying multiple images.
- ![ Click to see Add Carousel feature](static/images/featureCarousel.webp)

6. Contact Form:
- Description: Users can submit feedback or inquiries through a contact form.
- Value: Provides a way for users to communicate with the site administrators.
- ![ Click to see Contact feature](static/images/featureContactForm.webp)
- ![ Click to see Confirmation feature](static/images/featureConfirmSubmission.webp)


7. Add Destination:
- Description: Users can add destination they know through 'Share your Find' link.
- Value: Provides a way for logged-in users to share the places they know with everyone.
- ![ Click to see LoginRequired feature](static/images/featureLoginToAddDestination.webp)
- ![ Click to see Add Destination feature](static/images/FeatureaddDEstination.webp)
- ![ Click to see Confirmation feature](static/images/featureConfirmDesinationAdded.webp)

8. Pagination:
- Description: PREV and NEXT buttons are shown at the bottom of the page if there are more than 6 destinations on the home page. The PREV button does not show on the first page, and the NEXT button does not show on the last page.
- Value: Enhances navigation by allowing users to easily browse through multiple pages of destinations.
- ![ Click to see Pagination feature](static/images/featurePagination.webp)

- Inclusivity Notes:
  - Features include ARIA labels, inert and alt attributes on images for screen readers.

## Database
- I used Code Institute's PostgreSQL database.

### Database planning
- I used an Entity Relationship Diagram generated through http://dbdiagram.io/ to plan my database.
- ![ERD diagram](static/images/ERD.webp)

### Creating a database
1. Navigate to [PostgreSQL](https://dbs.ci-dbs.net/) from Code Institute.
2. Enter your student email address in the input field provided.
3. Click Submit.
4. Wait while the database is created.
5. Check your email.
6. You now have a URL you can use to connect your app to your database.
7. Add this url in DATABASE_URL key in env and heroku config vars.

## Deployment
- **Platform:**  : Heroku
- **High-Level Deployment Steps:** 
  * Heroku is a cloud platform that lets developers create, deploy, monitor and manage apps.
- You will need a Heroku log-in to be able to deploy a website to Heroku.
- Once you have logged into Heroku:
1. Click 'New' > 'Create new app'
2. Choose a unique name, choose your region and press 'Create app'
3. Click on 'Settings' and then 'Reveal Config Vars'
4. Add a key of 'DISABLE_COLLECTSTATIC' with a value of '1'.
5. Add a key of 'DATABASE_URL' - the value will be the URL you were emailed when creating your database.
6. Add a key of 'SECRET_KEY' - the value will be any random secret key 
7. In your terminal, type the code you will need to install project requirements:
* pip3 install gunicorn~=20.1
* pip3 install -r requirements.txt
* pip3 freeze --local > requirements.txt
8. Create an 'env.py' file at the root directory which contains the following:
    - import os
    - os.environ["DATABASE_URL"]='CI database URL'
    - os.environ["SECRET_KEY"]="Your secret key"
    - os.environ["CLOUDINARY_URL"]= "Your CLOUDINARY_URL"
  * add: ?secure=true  at the end of CLOUDINARY_URL to Force Cloudinary Images to Use HTTPS in Django

8. Create a file at the root directory called Procfile. In this file enter: 
* "web: gunicorn my_project.wsgi" (without the quotes)
9. In settings.py, set DEBUG to False. 
* YOU SHOULD ALWAYS SET DEBUG TO FALSE BEFORE DEPLOYING FOR SECURITY
10. Add ",'.herokuapp.com' " (without the double quotes) to the ALLOWED_HOSTS list in settings.py
11. Add, commit and push your code.
12. Go back to Heroku, click on the 'Deploy' tab.
13. Connect your project to GitHub.
14. Scroll to the bottom and click 'Deploy Branch' and your project will be deployed!
- **Verification and Validation:**
  - Tested the deployed application against the development environment for consistent functionality and design.
  - Verified accessibility using tools such as Lighthouse and manual testing.
- **Security Measures:**
  - Sensitive data is stored in environment variables.
  - Secret keys and all sensitive data is saved directly to Config Vars in Heroku.
  - DEBUG mode is disabled in the production environment to enhance security.

## AI Implementation and Orchestration

### Use Cases and Reflections:
Throughout the development of the **Incredible India Trails** project, I made extensive use of AI tools, particularly Copilot and ChatGPT, to streamline development and testing. This was my first time integrating AI this deeply into a project, and it turned out to be an incredibly helpful collaborator throughout the process.

  - **Code Creation:** 
    - Reflection: At first, I was uncertain about how much I could rely on AI for generating critical parts of the code, but I soon recognized its ability to quickly generate Django models, views, and even HTML structures. Using reverse prompts and multi-step interactions gave me the flexibility to experiment with different solutions and refine the code to fit the project’s goals. AI suggested ways to optimize database queries and improve code readability, which saved significant time and enhanced the final result.
     - Highlight: The back-and-forth collaboration with AI felt like working with an experienced pair programmer. The clearer I made my prompts, the more accurate and useful the results were, allowing me to focus on higher-level tasks while AI handled repetitive tasks efficiently.
    - Examples: 
      - Generated Django models for destinations, user reviews, and superuser approval workflows.
      - Created views and URL patterns to handle user authentication and CRUD operations.
      - Assisted in structuring HTML templates using Bootstrap for responsive design.
      - Assisted to ensure all fields in the DestinationForm and ImageForm were required and added custom validation to the form.
  
  - **Debugging & Error Resolution:** 
    - Reflection: Debugging with AI was a learning experience. The tool didn’t just spot errors; it often provided insightful suggestions that helped me rethink the structure of my code. For example, I was able to simplify some of the logic, making it more accessible to others who might work on the project in the future. This process also helped me improve my problem-solving skills by encouraging me to think about different ways to approach issues.
    - Examples:
      - Fixed issues with user authentication and permissions (ensuring superusers can approve reviews).
      - EnsuredFixed the issue of Pop-Up not showing by assisting to ensure the messages(PopUp) framework was set up correctly, updated the template to include the necessary elements for displaying the pop-up message, and verified the JavaScript code for displaying and closing the pop-up.

  - **Performance and UX Optimization:** 
    - Reflection: A standout moment in the project was when I used AI to improve the UI responsiveness and overall performance. I’m not particularly confident in front-end design, but AI offered helpful suggestions on improving the Bootstrap layout, such as optimizing image loading and refining button placements. These small changes had a big impact, ensuring the website was responsive across devices without sacrificing performance.

  - Highlight: I particularly appreciated how AI encouraged me to think about mobile-first design and user accessibility, making it a more inclusive and user-friendly experience. These insights helped the project feel polished and professional.
    - Examples:
      - Optimized PostgreSQL queries for retrieving and sorting large datasets.
      - Recommended Bootstrap-based enhancements for a better mobile-friendly UI.
      - Provided insights on lazy loading images to improve site performance.
      - Suggested to remove the aria-hidden attribute and used the inert attribute instead, updating the JavaScript code to handle the inert attribute when showing and hiding the modal.

- **Overall Impact:**
  - AI tools streamlined repetitive tasks, enabling focus on high-level development.
  - Efficiency gains included faster debugging, comprehensive testing, and improved code quality.
  - Challenges included contextual adjustments to AI-generated outputs, which were resolved effectively, enhancing inclusivity.

  Working with AI had a transformative effect on my development process. It allowed me to focus on more complex aspects of the project while it handled repetitive and time-consuming tasks. That said, not all suggestions were perfect—some required fine-tuning to better fit the project’s context. These moments served as valuable reminders that AI is not a replacement for my skills but a tool that enhances them.
  Reflecting on the experience, I feel that my technical abilities have improved significantly. I’ve become more efficient in debugging, testing, and implementing features. Moreover, I’ve learned how to use AI to enhance inclusivity and accessibility in software development. Above all, this experience taught me the importance of viewing new technologies as collaborators in the creative process.

## Testing 
- **Manual Testing:**
- Please see [TESTING.md](TESTING.md) file for all testing.

### Cloning
- To clone a GitHub repository:
1. On GitHub.com, navigate to [the repository you want to clone.](https://github.com/Harmeetkaur13/Incredible-India-Trails)
2. Click the "Code" button (found above the list of files).
3. Copy the URL for the repository.
4. Open Git Bash or your chosen terminal.
5. Navigate to the directory where you want to clone the repository.
6. Type: git clone https://github.com/Harmeetkaur13/Incredible-India-Trails.git
7. Press Enter to create your local clone.

## Technologies used
- HTML was used to structure the content of the website.
- CSS were used to design the layout of the website.
- Bootstrap was used as a CSS framework to provide a grid structure and improve responsiveness.
- Python and Django were used to build the backend review framework.
- VSCode was used as the code editor for development.
- GitHub was used to host the repository and version control.
- Heroku was the hosting platform.

## Future Enhancements
- To improve performance, in the future I will render only 2 or 3 destination cards on the Home page for small screens.
- For better UX, I will reduce the area taken up by the "added by" and "location" rows and use a different way to display them so that the main focus is on the destination images (carousel).
- For further support to willing visitors, I want to add links so they can see the prices of tours to the destination.
- For visitors, I want to provide travel and accommodation booking facilities so they can easily plan a trip to their dream destination.
- On the basis of feedback from user, if there is any issue regarding UX design or Accessibility, I would love to enhance the website accordingly.

## Acknowledgements
- Our Facilitator, Emma Lamont, for being helpful like always, encouraging at every single step, and concerned about our health during the project. Especially for providing responsive screenshots, walkthroughs, and useful feedback.
- Coding coaches Roo and Spencer for solving issues during development.
- Charles Tach for the impressive feedback that really helped me improve the website.
- AI Copilot and ChatGPT for helping me throughout my project.

## Credits
- I used the "I Think Therefore I Blog" walkthrough from the course content as a basis for my project to help me understand the Django. I customised the models, views and templates to create my own unique website. 
- Balsamiq was used to create the design wireframe.
- [Google Fonts](https://fonts.google.com/) were used to source the font styles.
- Images are downloaded from https://www.pexels.com/ https://unsplash.com/ . 
- [dbdiagram.io](http://dbdiagram.io/) was used to create the ERD image.
- https://favicon.io/logo-generator/ was used to create favicon.
