# Lotus

## Project Portfolio 5 - Full Stack Development/Specialization E-commerce


![amiresponsive](docs/readme_images/amiresponsive.png) 


## Live Project


[Here]()

---

## Site info

 
 - Lotus  is built using Django full-stack framework and uses a Relational Database. Technologies used include HTML, CSS, Javascript, Python, and Stripe payments.

 - Lotus is an application that envourages sex-positivity and self-pleasure. 
 - It's an online sexshop that proposes high quality silicone hygiene safe adult toys.
 - The site offers a great spectrum of vibrators and entertains a luxury and playfull aesthetic touch.

Key features include:

 - Filters: Users can apply filters to quickly and easily find some products (Search or sort by)
 - Bag & Stripe Checkout: Users can add multiple items to their bag and proceed to checkout with Stripe. See Stripe's testing card details to place an order on the website
 - Authentication: Users can create an account to save their contact information and view their order history
 - Reviews: Registered users can create, read, update and delete reviews
 - Contact form: Visitors can send enquiries
 - FAQs: Users can consult the FAQs in order to find some precise information

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
  * [Wireframes](#wireframes)
  * [Structure](#structure)
  * [Security](#security)

* [Features](#features)
  * [Header](#header)
  * [Footer](#footer)
  * [Home Page](#home-page)
  * [About Us Page](#about-us-page)
  * [User Account Pages](#user-account-pages)
  * [Profile](#profile)
  * [Vibrator (Products)](vibrator--products)
  * [Product Details](#product-details)
  * [Product Management](#product-management)
  * [Bag](#bag)
  * [Checkout](#checkout)
  * [FAQs](#faqs)
  * [Reviews](#reviews)
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

- People who are curious to discover self-pleasure with sex toys
- People who care about hight quality body safe product
- People who are sex positivity supporters

User 1: The typical site user would be a person who has an interest in self care and self pleasure in his sexuality.
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
| 7                              | site user  | read reviews left by other customers                                   | have feedback insights from customers.                                            |
| 7b                             | site user  | read FAQs left by owner.                                               | get more precise information.                                                     |
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
<img src="docs/readme_images/dashboard_1.png">
<img src="docs/readme_images/dashboard_2.png">
<img src="docs/readme_images/dashboard_3.png">
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

  #### Faq

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

## Security

### User Authentication

Authentication was implemented using Django's built-in authentication system:
 - to create a custom user model that allows users to sign up and log in to the website.
 - to create a custom admin model that allows admin users to log in to the admin site.
 - Django's LoginRequiredMixin is used to make sure that any requests to access secure pages by non-authenticated users are redirected to login page.
 - Django's UserPassesTestMixin is used to limit access based on certain permissions i.e. add a FAQ which is restricted onyl to the superuser.

 ### Methods

 ### Form Validation

 ### Database Security

---

## Features

### Header

- The header is present on all pages of the website.

<details>
<summary>Header image</summary>
<img src="docs/readme_images/header.png">
</details>

---

- Text logo: redirects the user to the home page.

<details>
<summary>Logo image</summary>
<img src="docs/readme_images/logo.png">
</details>

---

- Search bar: allows the user to search for name by name or description.

<details>
<summary>Search Bar image</summary>
<img src="docs/readme_images/search_bar.png">
</details>

---

- User icon: allows to access a dropdown menu with Sign up and login links
- User icon: registered users displayed their name next to the icon with dropdown menu logout and my profile links
- User icon: registered superuser acces under the icon a dropdown menu with the options Faqs Management and Product Management links

<details>
<summary> User Icon images</summary>
<img src="docs/readme_images/icon_user.png">
<img src="docs/readme_images/icon_user_logged.png">
<img src="docs/readme_images/icon_name.png">
</details>

---

- Bag icon: allows the user to visualize once a product added the quatity of itemes selected.
- Bag icon: allows the user to visualize once a product added a toast message that displays the content of the shopping bag.

<details>
<summary>Bag icon images</summary>
<img src="docs/readme_images/bag.png">
<img src="docs/readme_images/bag_counter.png">
</details>

---

- Main navbar: is present on all pages and allows the user to navigate the site through few links (Product, Reviews, About Us, Contact us).

<details>
<summary>Navbar images</summary>
<img src="docs/readme_images/navbar.png">
</details>

---

### Footer

- The footer is present on all pages of the website.

<details>
<summary>Footer images</summary>
<img src="docs/readme_images/footer.png">
</details>

---

- footer: allows to navigate the site through different links (Products, Reviews, Faqs, Contact Us, Privacy policy).

<details>
<summary>Footer link image</summary>
<img src="docs/readme_images/links_footer.png">
</details>

---

- footer: allows the user to visit Lotus' social pages (Facebook, Insta, Youtube) through social media icons.

<details>
<summary>Social media icons image</summary>
<img src="docs/readme_images/social_media.png">
</details>

---

- footer: allows users to subscribe to the website's newslette through Mailchimp subscription form.

<details>
<summary>Mailchimp subscription for image</summary>
<img src="docs/readme_images/mailchimp_footer.png">
</details>

---

### Home Page

- Home page: contains two calls for action (shop now, About Us)
- Home page: contains a Motto/Info about Lotus
- Home page : contains two images which illustrate Lotus' scale of products

<details>
<summary>Home Page images</summary>
<img src="docs/readme_images/home_page_1.png">
<img src="docs/readme_images/home_page_2.png">
</details>

---

### User Account Pages

- Sign up page: allows new users to create account - the process requires a confirmation email with confirmation link belo

<details>
<summary>Sign up image</summary>
<img src="docs/readme_images/sign_up.png">
</details>

---

- Login page: existing users to log into their account - including a "remember me" and "Fogot Password" option.Success messages inform the user if they have logged in successfully.

<details>
<summary>Login page images</summary>
<img src="docs/readme_images/logged_in.png">
</details>

---

- Logout page: allows authenticated users to securely log out of their account. Success messages inform the user if they have logged out successfully.

<details>
<summary>Logout page images</summary>
<img src="docs/readme_images/logout_page.png">
</details>

---

### Profile

- Delivery details: stores the user's delivery address and phone number.
- Order History: displays a list of every order the user has made with order number, date and order total. Each order is available once it has been clicked.


<details>
<summary>Delivery details images</summary>
<img src="docs/readme_images/profile.png">
<img src="docs/readme_images/past_order.png">
</details>

---


### Vibrators (Products List)

- Products list: accessible by clicking the link 'Product' in Navbar which will display a dropdown menu with different links. For instance, 'All' link displays all products. The other links are categories which display the products according their category.
- Products list: is displayed in product cards.Each product card shows an image of the product, its title, excerpt and price. If the user is a superuser, edit and delete buttons will appear at the bottom of the product card.
- A  sort by feature is located on the products page where users can sort all products by price in ascending or descending order and by title (A-Z) or (Z-A) .

<details>
<summary>Vibrators (Products) images</summary>
<img src="docs/readme_images/product_search_result.png">
<img src="docs/readme_images/product_search_empty.png">
<img src="docs/readme_images/product_list.png">
</details>

---

### Product (Details)

- Product details page: contains product image, titte, excerpt, description and price.
- Product details page: contains quantity input, keep Shopping button and ass to bag button
- Product details page: contains edit and delete option for authorised users for each product


<details>
<summary>Product (Detailss) images</summary>
<img src="">
<img src="">
</details>

---

### Product Management

- Add product page is accessible by clicking product Management link under the user icon when the superuser is authenticated.
- Add product page: contains form fields, a cancel button and a add product button

<details>
<summary>Add product page images</summary>
<img src="docs/readme_images/add_product.png">
</details>

---

### Edit Product page

- Edit product page is accessible by clicking edit link in each card product
- Edit product page: contains form fields, a cancel button and a edit product button

<details>
<summary>Edit product page images</summary>
<img src="docs/readme_images/edit_product_1.png">
<img src="docs/readme_images/edit_product_2.png">
</details>

---

### Delete Product page

- Delete product page is accessible by clicking delete link in each card product
- Edit product page: a cancel button and a delete button

<details>
<summary>Edit product page images</summary>
<img src="">
<img src="">
</details>

---

### Bag

- Bag Page is accessible when the user clicks to the shopping bag icon.
- Bag Page contains quantity adjustment option, product removal option and uptdate option
- Bag Page displays subtotal, delivery cost and grand total
- bag Page contains keep shopping button and go to secure checkout button


<details>
<summary>Bag images</summary>
<img src="docs/readme_images/shopping_bag_empty.png">
<img src="docs/readme_images/shopping_bag_item.png">
</details>

---

### Checkout

- Checkout page contains a form, including sections for personal info, contact details and card details
- Checkout page contains options to save details to profile for authenticated users. If the user is a guest, a link to create an account or login will be present.
- Checkout page contains current ordres summary
- Checkout page contains an adjust bag button and a complete order button

<details>
<summary>Checkout images</summary>
<img src="docs/readme_images/checkout.png">
</details>

---

### Checkout Success page

- Checkout Success page contains confirmation order and informs user that an email was sent to his registered email.
- Checkout Success page displays order details, contact and billing info
- Checkout Success page contains and Keep shopping button

<details>
<summary>Checkout Success images</summary>
<img src="docs/readme_images/success_checkout.png">
<img src="docs/readme_images/payment.png">
</details>

---

### FAQs

- FAQs: allows to display the frequently asked questions.
- FAQs Management link: available in dropdown menu under the user icon when owner logged in, redirect to add FAQs page
- Add FAQs page : allows the owner to add new question and answer
- Edit FAQs page: accessible through edit btn in each pair question/answer. This allows the owner to edit content.
- Faqs Delete btn: allows the owner to delete a pair question/answer
- FAQs page: allows the user to visualize FAQs

<details>
<summary>FAQs images</summary>
<img src="docs/readme_images/faqs_1.png">
<img src="docs/readme_images/faqs_2.png">
<img src="docs/readme_images/add_faq.png">
</details>

---

### Reviews

- Add review page is accessible by clicking add review button
- Add review page contains a form
- Add review page contains a cancel button and a add review button


<details>
<summary> Add Review images</summary>
<img src="docs/readme_images/add_review.png">
</details>

---

### Reviews

- Reviews page is accessible by clicking the link reviews in the navbar.
- Reviews page contains reviews made by users and a button add review if user is authenticated, otherwise a msg to invite him to register in order to post a review

<details>
<summary>Reviews images</summary>
<img src="docs/readme_images/reviews_1.png">
<img src="docs/readme_images/reviews_2.png">
</details>

---

### Edit Review

- Edit Review page is accessible by clicking the edit button, only displayed for the user who owns the reviews - must be authenticated.
- Edit Review page contains a form pre-populated with the existing review text
- Edut review page contains edit button and cancel button

<details>
<summary>Edit review images</summary>
<img src="">
<img src="">
</details>

---

### Delete Review

- Delete review page contains a delete button and a cancel button

<details>
<summary>Delete review images</summary>
<img src="">
<img src="">
</details>

---

### Contact Form

- Contact form: allows the user to enter their name, email, subject and message.
- Submit button: sends the message to the database.
- Cancel button: redirect the user to the home page.
- If the user is logged in, the email field is prepopulated with the user's email address.

<details>
<summary>Contact Form images</summary>
<img src="docs/readme_images/contact.png">
</details>

---

### Received Msg Page

- Received Msg Page: allows the user to receive a confirmation that his message was well properly sent.
- FAq button: redirect the user to the FAQs

<details>
<summary>Received msg image</summary>
<img src="">
<img src="">
</details>

---

### Thank you Page

- Thank you Page: allows the user to receive a confirmation that his review was well properly published.
- Home button: redirect the user to the home page.


<details>
<summary>Thank you image</summary>
<img src="">
<img src="">
</details>

---

### About Us Page

- About us page is accessible by clicking the link about us in the navbar
- About us page contains a text about Lotus and a button home


<details>
<summary>About Us images</summary>
<img src="docs/readme_images/about_us_1.png">
<img src="docs/readme_images/about_us_2.png">
</details>

---

### Error Pages

- Error message: displays the error message.
- Home button: redirects the user to the home page.
- Logout button: allows the user to log out 

<details>
<summary>Error Pages images</summary>
<img src="docs/readme_images/error_page.png">
</details>

---

### Toast messsage Pages

- 

<details>
<summary>Toast success add item page image</summary>
<img src="docs/readme_images/success_add_item.png">
<img src="docs/readme_images/success_remove.png">
<img src="docs/readme_images/success_loggedin.png">
<img src="docs/readme_images/toast_alert_edit.png">
<img src="docs/readme_images/success_deleted.png">
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
- [Bootstrap 4](https://getbootstrap.com/docs/4.6/getting-started/introduction/) - Used to develop the layout of the site.
- [django-summernote](https://github.com/summernote/django-summernote) (WYSIWYG HTML editor)
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

### Creating a Gitpod Workspace

<details>
<summary>Steps</summary>

1. Log in to GitHub and go to the [Code Institute student template for Gitpod](https://github.com/Code-Institute-Org/gitpod-full-template)
2. Click 'Use this Template' next to the Green Gitpod button.
3. Add a repository name and click 'Create reposiory from template'.
4. This will create a copy of the template in your own repository. Now you can click the green 'Gitpod' button to open a workspace in Gitpod.

</details>

---

### Installing support libraries and Django

<details>
<summary>Steps</summary>

```
$ pip3 install 'django<4' gunicorn
$ pip3 install dj_database_url psycopg2
$ pip3 install boto3
$ pip3 install django-storages
$ pip3 install django-crispy-forms  
$ pip3 install crispy-bootstrap5
$ pipe install django-summernote
```

</details>

---

### Create requirements file

<details>
<summary>Step</summary>

```
$ pip3 freeze --local > requirements.txt
```

</details>

---

### Create a project

<details>
<summary>Step</summary>

```
$ django-admin startproject lotus .
```

</details>

---
### Create apps and add them to settings.py

<details>
<summary>Steps</summary>

```
$ python3 manage.py startapp bag
$ python3 manage.py startapp checkout
$ python3 manage.py startapp contact
$ python3 manage.py startapp faq
$ python3 manage.py startapp home
$ python3 manage.py startapp product
$ python3 manage.py startapp profiles
$ python3 manage.py startapp reviews
INSTALLED_APPS = [
   'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'home',
    'product',
    'bag',
    'checkout',
    'contact',
    'profiles',
    'reviews',
    'faq',
    'crispy_forms',
    'django_summernote',
    'storages',
]
```

</details>

---

### Migrate changes

<details>
<summary>Steps</summary>

```
$ python manage.py makemigrations
$ python manage.py migrate
```

</details>

---

### Creating a database

<details>
<summary>Steps</summary>

1. Go to [ElephantSQL.com](https://elephantsql.com/) and select to create a database
2. Select the free database plan
3. Select “Log in with GitHub” and authorise with GitHub
4. Create new team form. You can use your name, read and agree to the T&C's, select yes for GDPR, provide your email address and click Create Team. Your account will be created 
5. From your dashboard, click “Create New Instance”
6. Set up your plan. Give it the same name as your project, select the free plan. Select "select region" and select a region close to you.
7. Click review, and if the details are correct, click create instance.
8. Return to the ElephantSQL dashboard and click on the database instance name for this project
9. In the URL section, clicking the copy icon will copy the database URL to your clipboard

```
import os
import dj_database_url
if os.path.isfile('env.py'):
  import env
```

```
if 'DATABASE_URL' in os.environ:
        DATABASES = {
            'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
        }
    else:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
            }
    }

```

</details>

---

### Creating AWS account

<details>
<summary>Steps</summary>

1. Find and access S3 as a service and create a new bucket:

    Under Object Ownership, check "ACLs enabled"

    Uncheck "Block all public access" and acknowledge (required for public access to static files)

2. Configur bucket settings:

    Under **Properties**, enable Static Website Hosting

    Under **Permissions**, copy the following code into CORS section:

    ```
    [
        {
            "AllowedHeaders": [
                "Authorization"
            ],
            "AllowedMethods": [
                "GET"
            ],
            "AllowedOrigins": [
                "*"
            ],
            "ExposeHeaders": []
        }
    ]
    ```
    This is required to set up the access between the Heroku app and the S3 bucket.

    Under **Bucket policy**, go to Policy generator.

    Bucket Type = S3 Bucket Policy

    Principal = * (allows all principles)

    Actions = GetObject

    Paste in ARN from bucket settings tab.

    Click Add Statement, then Generate Policy.

    Copy policy in paste into bucket policy editor. Also add ``/*`` onto the end of the resource key.

    Click Save.

    Under **Access control list (ACL)**, check "List" checkbox for "Everyone (public access)"

3. Create user to access bucket with IAM (Identity and Access Management)

    In IAM, got to User Groups (sidebar left).

    There create a group for a user, create an access policy giving the group access to the S3 bucket and assign the user to the group so it can use the policy to access all files. 

4. Connect Django to S3

    Configure settings.py accordingly, including necessary AWS variables.

    ```
    if 'USE_AWS' in os.environ:
    # Cache control
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }

    # Bucket Config
    AWS_STORAGE_BUCKET_NAME = 'mylotus'
    AWS_S3_REGION_NAME = 'eu-north-1'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

    # Static and media files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    # Override static and media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'

    ```


  

    Create ``custom_storages.py`` file.

    ```
     from django.conf import settings
     from storages.backends.s3boto3 import S3Boto3Storage

     class StaticStorage(S3Boto3Storage):
        location = settings.STATICFILES_LOCATION

      class MediaStorage(S3Boto3Storage):
        location = settings.MEDIAFILES_LOCATION

    ```
5. Create folder in your bucket S3
   Name the folder 'media' and click 'Save'.
   Inside the folder, click 'Upload', 'Add files', and then select all the images that you are using for your site.
   Then under 'Permissions' select the option 'Grant public-read access' and click upload.
   The static files and media files should be automatically linked from django to your S3 bucket.

   
    


</details>

---

### Creating env.py

<details>
<summary>Steps</summary>

1. place env.py to the project root directory
2. add env.py to git.ignore to avoid pushing this file to GitHub
3. Add the following entries into the file

```
import os
os.environ["DATABASE_URL"] = "XXXX"
os.environ["SECRET_KEY"]= "XXXX"
os.environ["STRIPE_PUBLIC_KEY"]= "XXXX"
os.environ["STRIPE_SECRET_KEY"] = "XXXX"
os.environ["STRIPE_WH_SECRET"] = "XXXX"
os.environ["AWS_ACCESS_KEY_ID"] = "XXXX"
os.environ["AWS_SECRET_ACCESS_KEY"] = "XXXX"
```

</details>

---

### Creating an application with Heroku

<details>
<summary>Steps</summary>


1. Create a Heroku account and log in.
2. Create a new app. When you do so, select the closest region to you and give it an appropriate name. Note Heroku names must be unique
3. Add the following Config Vars in Heroku:

|     Variable name     |                           Value/where to find value                           |
|:---------------------:|:-----------------------------------------------------------------------------:|
| AWS_ACCESS_KEY_ID     | AWS CSV file(instructions below)                                               |
| AWS_SECRET_ACCESS_KEY | AWS CSV file(instructions below)                                               |
| DATABASE_URL          | Postgres generated (as per step above)                                        |
| EMAIL_HOST_PASS       | Password from email client                                                    |
| EMAIL_HOST_USER       | Site's email address                                                          |
| SECRET_KEY            | Random key generated as above                                                 |
| STRIPE_PUBLIC_KEY     | Stripe Dashboard > Developers tab > API Keys > Publishable key                |
| STRIPE_SECRET_KEY     | Stripe Dashboard > Developers tab > API Keys > Secret key                     |
| STRIPE_WH_SECRET      | Stripe Dashboard > Developers tab > Webhooks > site endpoint > Signing secret |
| USE_AWS               | True (when AWS set up - instructions below)                                   |


4. Connect Heroku to github repository
5. Deploy from branch manually (before final deployment: the debug setting in settings.py was set to false for security, X_FRAME_OPTIONS = 'SAMEORIGIN' was added and  the DISABLE_COLLECTSTATIC config var in Heroku has to be removed)

```
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
```

</details>

---

### Forking the GitHub Repository

<details>
<summary>Steps</summary>

Forks are used to propose changes to someone else's project or to use someone else's project as a starting point for your own idea. By forking the GitHub Repository you make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository.

To Fork a Github Repository:

1. Log in to GitHub and go to the [GitHub Repository](https://github.com/XXX)
2. Locate the Fork button in the top-right corner of the page, click Fork.
3. You should now have a copy of the original repository in your GitHub account.

</details>

---

### Making a Local Clone

<details>
<summary>Steps</summary>

You will now have a fork of the repository, but you don't have the files in that repository locally on your computer.

To make a local clone:

1. Log in to GitHub and go to the [GitHub Repository](https://github.com/XXX)
2. Above the list of files, click  Code.
3. To clone the repository using HTTPS, under "Clone with HTTPS", click the 'Copy' icon. To clone the repository using an SSH key, including a certificate issued by your organization's SSH certificate authority, click Use SSH, then click the 'Copy' icon. To clone a repository using GitHub CLI, click Use GitHub CLI, then click the 'Copy' icon.
4. Open Git Bash.
5. Change the current working directory to the location where you want the cloned directory.
6. Type git clone, and then paste the URL you copied earlier. It will look like this, with your GitHub AE username instead of YOUR-USERNAME:

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```

7. Press Enter. Your local clone will be created.

</details>

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