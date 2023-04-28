# Lotus

## Project Portfolio 5 - Full Stack Development/Specialization E-commerce


![amiresponsive]() 


## Live Project


[Here]()

---

## Site info

 - Lotus is an application that envourages sex-positivity amongst women. 
 - It's an online sexshop that proposes high quality silicone hygiene safe adult toys.
 - The site offers a great spectrum of vibrators and entertains a luxury and playfull aesthetic touch.

---

## Table of CONTENTS

* [Project Goals](#project-goals)
  * [User Goals](#user-goals)
  * [Site Owner Goals](#site-owner-goals)

* [User Experience](#user-experience-ux)
  * [Target Audience](#target-audience)
  * [User Requirements and Expectations](#user-requirements-ans-expectations)
  * [User Stories](#user-stories)

* [Technical Design](#technical-design)
  * [Agile Methodology](#agile-methodology)
  * [CRUD Functionality](#crud-functionality)
  * [Database Model](#database-model)
  * [Colour Scheme](#colour-scheme)
  * [Typography](#typography)
  * [Structure](#structure)
  * [Wireframes](#wireframes)

* [Features](#features)
  * [Header](#header)
  * [Footer](#footer)
  * [Home Page](#home-page)
  * [User Account Pages](#user-account-pages)
  * [Profile](#profile)
  * [Vibrator (Products)](vibrator--products)
  * [Product Detail](#product-detail)
  * [Product Management](#product-management)
  * [Bag](#bag)
  * [Checkout](#checkout)
  * [About Us](#about-us)
  * [Reviewss](#reviews)
  * [Contact Form](#contact-form)
  * [Error Pages](#error-pages)
  * [Future Implementations](#future-implementations)

* [Marketing Strategy](#marketing-strategy)
  * [SEO](#seo)
  * [Content marketing](#content-marketing)
  * [Social Media Marketing](#social-media-marketing)
  * [Email Marketing](#email-marketing)

* [Technologies Used](#technologies-used)
  * [Languages Used](#languages-used)
  * [Frameworks, Libraries](#frameworks-libraries)
  * [Storage & Hosting](#storage--hosting)
  * [IDE & Version Control](#ide--version-control)
  * [Other tools](#other-tools)

* [Deployment](#deployment)

* [Testing](#testing)

* [Credits](#credits)
  * [Ressources Used](#ressources-used)
  * [Code Used](#code-used)
  * [Content](#content)
  * [Media](#media)
  * [Acknowledgments](#acknowledgments)

---


## Project Goals

### User Goals

- To be able to purchase hight quality sex toys
- To be able to leave a review about one of the products
- To be able to use CRUD functionality whilst logged onto the site regarding reviews.

### Site Owner Goals

- To provide a platform in which users can discover our collection of vibrators
- To provide an enjoyable user experience which would make users wish to return to the site to purchase 
- To have the ability to be given feedback via a contact form
- To provide users with products that meet their expectations
- To allow users to view, read and comment reviews that may help to other users to make a choice or simply to share their joyful experience with one of the vibrator.
- To allow users to checkout quickly and easily
- To allow users to create a profile to view past orders and update profile information

---


## User Experience (UX)

### Target Audience

- Women who are curious to discover self-pleasure with sex toys
- Women who care about hight quality body safe product
- Women who are sex positivity supporters

User 1: The typical site user would be a female who has an interest in self care and self pleasure in her sexuality.
User 2: Additional site users could be partner of user 1 and may be browsing the site to purchase gifts.


### User Requirements ans Expectations

- A site which provides a good level of interactiveness between users
- Links and functions to act as expected
- Notification to provide feedback on expected function outcomes
- Simple content that a user can easily digest
- Responsiveness to allow pleasant use across devices of different screen sizes

### User Stories


| User Story ID                  | As a/an    | I want to be able to...                                                | So that I can...                                                                  |
| ------------------------------ | ---------- | ---------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| Viewing and Navigation         |            |                                                                        |                                                                                   |
| 1                              | site user  | intuitively navigate around the site                                   | find content.                                                                     |
| 2                              | site user  | view a list of products                                                | select a product to view.                                                         |
| 3                              | shopper    | click on a product                                                     | read the full product details.                                                    |
| 4                              | shopper    | view a specific category of products                                   | browse the type of products I'm interested in.                                    |
| 5                              | shopper    | search all products                                                    | find what I am looking for.                                                       |
| 6                              | shopper    | sort all products                                                      | view products based on price or title.                                            |
| 7                              | site user  | read reviews left by other customers                                   | have feedback insights from customers.                                            |
| Registration and User Accounts |            |                                                                        |                                                                                   |
| 8                              | site user  | register an account                                                    | have a personal account and see my profile.                                       |
| 9                              | site user  | login or logout                                                        | access my personal info/keep my account secure.                                   |
| 10                             | site user  | see my login status                                                    | know if I'm logged in or out.                                                     |
| 11                             | site user  | save my personal details in my user profile                            | spare the time to fill them out for future orders.                                |
| 12                             | site user  | have a personalised user profile                                       | with my personal order history and be able to update my default billing address   |
| 13                             | site user  | view my order history                                                  | remember what purchases I've made                                                 |
| 14                             | site user  | recover my password in case I forget                                   | recover access to my account.                                                     |
| Purchasing and Checkout        |            |                                                                        |                                                                                   |
| 15                             | shopper    | add a number of products in different quantities to my shopping bag    | purchase them all at once.                                                        |
| 16                             | shopper    | view a running total of my shopping bag                                | see how much it costs in total.                                                   |
| 17                             | shopper    | view the contents of my shopping bag at any time                       | see what is included and the total cost.                                          |
| 18                             | shopper    | adjust the quantity of individual products in my bag                   | make changes before I purchase.                                                   |
| 19                             | shopper    | see a summary of my shopping cart when I checkout                      | know what products are included and the total cost before I commit to purchasing. |
| 20                             | shopper    | enter my payment information securely                                  | purchase my chosen products quickly with no issues.                               |
| 21                             | shopper    | checkout as a guest                                                    | avoid to sign up for an account.                                                  |
| 22                             | shopper    | view an order confirmation after checkout                              | know my purchase was successful.                                                  |
| 23                             | shopper    | receive an email confirmation of my order                              | have a record of my purchase                                                      |
| Admin & Store Management       |            |                                                                        |                                                                                   |
| 24                             | site owner | add/edit/delete products through an easy-to-use interface              | can manage the store's contents.                                                  |
| Contact                        |            |                                                                        |                                                                                   |
| 25                             | site user  | submit an enquiry form                                                 | report a personal matter                                                          |
| Review                           |            |                                                                        |                                                                                   |
| 26                             | site user  | add / edit / delete a review regarding one of the products in the site | give my feedback.                                                                 |
| Newsletter                     |            |                                                                        |                                                                                   |
| 27                             | site user  | sign up for the website's newsletter                                   | keep myself informed about new products and promotions from the site.             |

---


## Technical Design

### Agile Methodology

- Throughout this project, an agile approach has been applied in order to develop the website. Each activity was broken down into manageable actions from initially  11 milestones/Epic moments, which were then broken down into smaller units : issues. Each issue was labeled to identify their main topics. For instance, the label User Story represents the user experience, the label MPV stands for the Minimum Viable Product which often are associated with the label Must Have.

- Each issue has different acceptance criteria and series of tasks. GitHub's project was used to track these user stories, implement ideas, and monitor the workflow. Indeed, the kanban board allowed the workflow to focus first on the essential features, work in small iteration, adding extra features in case the time allowed it.

- When I was working on the project, I chose one issue to work on from the "Todo" column of the Dashboard Wall of Shame and moved it into the "In Progress" column.
After I finished the issue by fulfilling all the acceptance criteria and the  tasks attached to them, I closed the issue which moved it automatically into the "Done" Column.
The issues that I couldn’t tackle from the "Todo" column ended in the “Won’t do” column.

<details>
<summary>Issue Samples</summary>
<img src="">
<img src="">
<img src="">
<img src="">
<img src="">
</details>

---

### CRUD Functionality

 Lotus handles data with full CRUD Functionality. User's prerogatives are :

 #### Review

 | Create | Read | Update | Delete |
 | ------------- | ------------- | -------------    | ------------- |
 |  Yes  | Yes  | Yes | Yes |


 #### Contact

  | Create | Read | Update | Delete |
  | ------------- | ------------- | -------------    | ------------- |
  |  Yes  | No  | No | No |


   #### Product

  | Create | Read | Update | Delete |
  | ------------- | ------------- | -------------    | ------------- |
  |  Yes  | No  | No | No |


  Superser's prerogatives are :

  #### Product

  | Create | Read | Update | Delete |
  | ------------- | ------------- | -------------    | ------------- |
  |  Yes  | Yes  | Yes | Yes |


### Database Model

A backend database was  built with the Django framework and the use of ElephantSQL Postgres for the deployed site.

<details>
<summary>Database Schema</summary>
<img src="docs/readme_images/database_er_diagram_lotus.png">
</details>

---

### Colour Scheme

- The Three dominant colors of the website were chosen from pictures of three products:

<details>
 <summary>Colour Palette</summary>
 <img src="docs/readme_images/color_1.png">
 <img src="docs/readme_images/color_1_bis.png">
 <img src="docs/readme_images/color_2.png">
 <img src="docs/readme_images/color_2_bis.png">
 <img src="docs/readme_images/color_3.png">
 <img src="docs/readme_images/color_3_bis.png">
 </details> 

---

### Typography

- Fonts were imported using Google Fonts. Kurale and Lato were used thoughout with a backup of sans-serif.


### Wireframes

- Due to time constraints and decisions made during the project, there might be some differences between the live site and my initial wireframes.

<details>
<summary>Home Page</summary>
<img src="docs/wireframes/home_page.png">
</details>


<details>
<summary>Product List</summary>
<img src="docs/wireframes/product_list.png">
</details>

<details>
<summary>Product Detail</summary>
<img src="docs/wireframes/product_details.png">
</details>

<details>
<summary>Reviews</summary>
<img src="docs/wireframes/reviews.png">
</details>

<details>
<summary>Profile</summary>
<img src="docs/wireframes/profile.png">
</details>

<details>
<summary>Product Management</summary>
<img src="docs/wireframes/product_management.png">
</details>

<details>
<summary>Edit Review</summary>
<img src="docs/wireframes/edit_review.png">
</details>

<details>
<summary>Order Confirmation</summary>
<img src="docs/wireframes/order_confirmation.png">
</details>

<details>
<summary>Contact Us</summary>
<img src="docs/wireframes/contact_us.png">
</details>

<details>
<summary>Bag</summary>
<img src="docs/wireframes/bag.png">
</details>

<details>
<summary>Checkout</summary>
<img src="docs/wireframes/checkout.png">
</details>

---

### Structure

User journey diagram

<details>
<summary>Functional Structure</summary>
<img src="docs/readme_images/information_structure.png">
</details>

---

## Features

### Header

<details>
<summary>Navbar images</summary>
<img src="">
<img src="">
</details>

---

### Footer

<details>
<summary>Footer images</summary>
<img src="">
<img src="">
</details>

---

### Home Page

<details>
<summary>Home Page images</summary>
<img src="">
<img src="">
</details>

---

### User Account Pages

<details>
<summary>User Account Pages images</summary>
<img src="">
<img src="">
</details>

---

### Profile

<details>
<summary>Profile images</summary>
<img src="">
<img src="">
</details>

---

### Vibrators (Products)

<details>
<summary>Vibrators (Products) images</summary>
<img src="">
<img src="">
</details>

---

### Product (Details)

<details>
<summary>Product (Detailss) images</summary>
<img src="">
<img src="">
</details>

---

### Product Management

<details>
<summary>Product Management images</summary>
<img src="">
<img src="">
</details>

---

### Bag

<details>
<summary>Bag images</summary>
<img src="">
<img src="">
</details>

---

### Checkout

<details>
<summary>Checkout images</summary>
<img src="">
<img src="">
</details>

---

### About Us

<details>
<summary>About Us</summary>
<img src="">
<img src="">
</details>

---

### Reviews

<details>
<summary>Reviews images</summary>
<img src="">
<img src="">
</details>

---

### Contact Form

<details>
<summary>Contact Form images</summary>
<img src="">
<img src="">
</details>

---

### Error Pages

<details>
<summary>Error Pages images</summary>
<img src="">
<img src="">
</details>

---

### Future Implementations


## Marketing Strategy

- Lotus has been promoted through various marketing strategies such as SEO, content marketing, social media marketing, and email marketing. 
- Each of these strategies has been elaborated upon separately in the following sections.

### SEO

- After finalizing the business model as an adult female product store, the next step was to devise a marketing strategy and determine the relevant keywords to target. 
- To boost the website's visibility in search engine results, a number of SEO techniques were implemented.

**Keywords:** 

- Both short-tail and long-tail keywords were meticulously evaluated for the website. 
- In-depth keyword research was conducted, which involved examining Google search results, analyzing competitor's keywords, and using wordtracker.com.

- The most pertinent keywords were incorporated into the website's meta-keywords and meta-description. 
- In addition, these keywords were thoughtfully integrated into page titles, headings, site content, <strong></strong> tags, image alt attributes, and anchor tag links throughout the website.
- Below is a sample list of topics and keywords that were generated. After careful evaluation of their relevance and authority, the list was further refined.



| Short Tail Keywords         | Long Tail Keywords           |
| ------------- | ------------- |
| Sex | Women's sex toys |
|  Masturbation| Female pleasure products |
| Pleasure  | Vibrators for women |
| Orgasm| Clitoral stimulators |
|  Masturbate | G-spot stimulators  |
| satisfaction |Remote control vibrators for couples |
| dildo |Rechargeable vibrators for eco-friendly pleasure |
| vibrator |Dual-stimulating vibrators for intense orgasms |
| sextoys |Luxury vibrators for pleasure|

**Building Trust:**

- In order to build brand trust, a reviews page for our product has been included in the site.
- About Us Page inform our clientèle from our ehtic regarding our product and sex positivity awareness
- The page footer also includes links to the privacy policy to inform users about how their data is being collected and processed.

**Sitemap and robots.txt**


- I made a list of important page URLs in a sitemap file, so search engines can easily understand the site's structure and navigate through it. 
- I used xml-sitemaps.com to make it.
- I made a robots.txt file to tell search engines where they can't go on the website. 
- This improves SEO by increasing the quality of the site.


### Content marketing 

- The site showcases high quality images of our vibrators in order to attract potential new clients. 
- The photos allow the business to present a line of products in a simple and playful way. 
- Our aesthetic  demarcates our brand from our concurrents, anchoring our line in a trendy accessoires vibe. 

### Social Media Marketing

IN PROGRESS

### Email Marketing

- Users can sign up for the site's newsletter even if they don't have an account. 
- The signup box is at the bottom of the website. 
- The business can use this to share news, new products, and special offers with customers and potential customers.
- Mailchimp was used to create this service.


---


## Technologies Used


### Languages Used

- [HTML5](https://en.wikipedia.org/wiki/HTML5)

- [CSS3](https://en.wikipedia.org/wiki/CSS)

- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)

- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))


### Frameworks, Libraries

- [Django 3.2.16](https://www.djangoproject.com/) - Used to rapidly develop the site.
- [Gunicorn](https://gunicorn.org/) - Used for being a pure-Python HTTP server for WSGI applications
- [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) - Used to format forms.
- [Psycopg2](https://pypi.org/project/psycopg2/) - Used as a PostgreSQL adaptor
- [Django allauth](https://django-allauth.readthedocs.io/en/latest/index.html)  - Used to implement account authorisation and providing associated templates
- [jquery library](https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js) - Used to fade out alert messages
- [dj_database_url](https://pypi.org/project/dj-database-url/) - Used to allow database urls to connect to the postgres db
- [Bootstrap 5](https://getbootstrap.com/docs/5.0/getting-started/introduction/) - Used to develop the layout of the site.
- [Font Awesome](https://fontawesome.com/) - Used to produce icons on the site.
- [Google Fonts](https://fonts.google.com/) - Used to import the site's font family.

### Storage & Hosting

- [Github](https://github.com/) - Used to create and store the project repository.
- [Heroku Platform](https://id.heroku.com/) - Used to deploy the live project.
- [ElephantSQL](https://www.elephantsql.com/) - Used to host the website's PostgreSQL database.
- [AWS](https://aws.amazon.com/?nc2=h_lg) - Used for file storage.

### IDE & Version Control

- [Gitpod](https://gitpod.io/) - Used to create files and write code.
- [Git](https://git-scm.com/) - Used for version control.

### Other Tools

- [Balsamiq](https://balsamiq.com/) - Used to create Wireframes for the project.
- [Lucid](https://lucid.app/users/login#/login) - for creating a Model ER.
- [Unsplash](https://unsplash.com/) - for content pictures
- [Pexels](https://www.pexels.com/) - for content pictures
- [amiresponsive](https://ui.dev/amiresponsive) - test responsive website.
- [W3 Schools](https://www.w3schools.com/) - for HTML, CSS, Django tips.
- [Tables Generator](https://www.tablesgenerator.com/markdown_tables) - Used to convert excel testing tables to markdown 
- [Sitemap Generator](www.xml-sitemaps.com) - Used to create sitemap.xml 
- [Mailchimp](https://mailchimp.com/?currency=EUR) - Used to create the newsletter signup functionality.
- [Stripe](https://stripe.com/ie) - Used for the payments system.
- [Privacy Policy Generator](https://www.privacypolicygenerator.info/) - Used to create the site's privacy policy
- [LearnDjango](https://learndjango.com/) - for understanding the logic of Django
- [Django Docummentation](https://docs.djangoproject.com/en/3.2/) - to research and learn specific utilisation of Django framework
- [WC3 Validator](https://validator.w3.org/) - Used to validate the HTML code of the site.
- [Jigsaw W3 Validator](https://jigsaw.w3.org/css-validator/)- Used to validate the CSS of the site.
- [Jshint](https://jshint.com/) - Used to validate the Javascript of the site.
- [Python Linter](https://pep8ci.herokuapp.com/) - Used to validate the Python of the site.
- [Chrome dev tools (Lighthouse)](https://developer.chrome.com/docs/lighthouse/overview/) - Used to measure site performance, SEO and accessibility.
- [LICECap](https://www.cockos.com/licecap/) - Used to screen-record manual testing.

---

## Deployment 

---

## Testing

[here](testing.md)

---

# Credits

### Ressources Used

- [W3Schools](https://www.w3schools.com/)
- [BOUTIQUE ADO](https://github.com/Code-Institute-Solutions/boutique_ado_v1/tree/250e2c2b8e43cccb56b4721cd8a8bd4de6686546) - Django walkthrough project "Boutique Ado" used as an inspiration and an orientation to my project
- [Medium.com](https://medium.com/@ksarthak4ever/django-class-based-views-vs-function-based-view-e74b47b2e41b) - for understanding difference between Class Based Views vs Function Based Views
- [Exploring Python Classes with Ben Kavanagh](https://www.youtube.com/watch?v=opOK_1g1rsw&list=PL_7334VduOHvzZYlgy_0kZLcic2NINCUt&index=7) - for understanding difference between Class Based Views vs Function Based Views
- [LearnDjango](https://learndjango.com/tutorials/) - for understanding the use of Django Framework
- [Summernote](https://summernote.org/) - for understanding use of Summernote
- [Valentinog](https://www.valentinog.com/blog/get-context-data/) - for understanding how to add extra context data to a CreateView
- [Stackoverflow](https://stackoverflow.com/questions/49376371/python-decorators-args-and-kwargs) - for understanding pyhton decorators
- [Stackoverflow](https://stackoverflow.com/questions/65285154/django-decorators-to-handle-admin-users-redirection) - for understanding pyhton decorators


### Code Used

IN PROGRESS


### Content

IN PROGRESS 

###  Media

Images were all open source and free to use from [Pexels](https://www.pexels.com/) and [Unsplash](https://unsplash.com/) :

- pexels-anna-shvets-5187571.jpg
- pexels-anna-shvets-5187573.jpg
- pexels-cottonbro-studio-6769000.jpg
- pexels-anna-shvets-5187577.jpg
- pexels-cottonbro-studio-6763676.jpg
- ifonnx-toys-8-7EeeAM-RA-unsplash.jpg
- pexels-anna-shvets-5187304.jpg
- pexels-cottonbro-studio-6768984.jpg
- ifonnx-toys-BBe9HSHIEiw-unsplash.jpg
- pexels-anna-shvets-5187303.jpg
- pexels-anna-shvets-5187360.jpg
- pexels-cottonbro-studio-6768324.jpg


###  Acknowledgments

 - Many thanks to my Mentor Antonio Rodriguez for helpful feedback, industry insights and recommended tools.
 - Many thanks to my friends (Marjorie and Louise) and family for helping me testing the website and for their precious feedbacks.