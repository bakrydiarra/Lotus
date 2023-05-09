# TESTING

---

## Table of CONTENTS


* [W3C Validator](#w3c-validator)
* [Python Linter](#python-linter)
* [Lighthouse](#lighthouse)
* [MANUAL TESTING](#manual-testing)
* [BUGS](#bugs)


---

##  W3C Validator

All HTML pages were run through the W3C HTML Validator. See results in below table.

| Page                           | Logged Out | Logged In |
|--------------------------------|------------|-----------|
| Home                           | No Errors  | No Errors |
| Products                       | No Errors  | No Errors |
| Product Detail                 | No Errors  | No Errors |
| Add Product                    | N/A        |No Errors  |
| Edit Product                   | N/A        | No Errors |
| Bag                            | No Errors  | No Errors |
| Checkout                       | No Errors  | No Errors |
| Checkout Success               | No Errors  | No Errors |
| Profile                        | N/A        | No Errors |
| Order History                  | N/A        | No Errors |
| FAQs                           | No Errors  | No Errors |
| Add FAQ.                       | N/A        | No Errors |
| Edit FAQ.                      | N/A        | No Errors |
| Delete FAQ                     | N/A        | No Errors |
| Reviews                        | No Errors  | No Errors |
| Add Review                     | N/A        | No Errors |
| Edit Review.                   | N/A        | No Errors |
| Delete Review.                 | N/A        | No Errors |
| Contact                        | 10 Erros   | 10 Errors |
| Received msg                   | No Errors  | No Errors |
| Thank Review                   | No Errors  | No Errors |
| Sign In                        | No Errors  | N/A       |
| Sign Up                        | No Errors  | N/A       |
| Log Out                        | N/A        | No Errors |
| Password Reset                 | No Errors  | N/A       |
| 400.html                       | No errors  | No errors |
| 403.html                       | N/A        | No errors |
| 404.html                       | No errors  | No errors |
| 500.html                       | No errors  | No errors |


There was few minor markup errors present on the contact page, it does not significantly impact the user experience. These errors are located within the Django Summernote library and is outwidth my control to edit/correct them.

![HTML Error](docs/readme_images/contact_html_errors.png)


---

 #### **CSS Validation**

No errors were detected when passing my CSS files through the official W3C CSS Validator

 <details>
<summary>base.css</summary>
<img src="docs/readme_images/base_css.png">
</details>

---

 <details>
<summary>checkout.css</summary>
<img src="docs/readme_images/checkout_css.png">
</details>

---

 <details>
<summary>profile.css</summary>
<img src="docs/readme_images/profile_css.png">
</details>

---

## Python Linter

<details>
<summary>XX</summary>
<img src="">
</details>

---

## Lighthouse

<details>
<summary>Home Page</summary>
<img src="docs/readme_images/lighthouse_home.png">
</details>

<details>
<summary>Product list Page</summary>
<img src="docs/readme_images/lighthouse_products.png">
</details>

<details>
<summary>Product Details Page</summary>
<img src="docs/readme_images/lighthouse_product_details.png">
</details>

<details>
<summary> Add Product</summary>
<img src="docs/readme_images/lighthouse_add_product.png">
</details>

<details>
<summary> Edit Product</summary>
<img src="docs/readme_images/">
</details>

<details>
<summary>Reviews Page</summary>
<img src="">
</details>

<details>
<summary> Edit Review Page</summary>
<img src="">
</details>

<details>
<summary> Add Review age</summary>
<img src="docs/readme_images/lighthouse_add_review.png">
</details>

<details>
<summary> Delete Review Page</summary>
<img src="">
</details>

<details>
<summary>Checkout Page</summary>
<img src="">
</details>

<details>
<summary>Contact Us Page</summary>
<img src="docs/readme_images/lighthouse_contact.png">
</details>

<details>
<summary>Bag Page</summary>
<img src="docs/readme_images/lighthouse_shopping_bag.png">
</details>

<details>
<summary>Profile Page</summary>
<img src="docs/readme_images/lighthouse_profile.png">
</details>

<details>
<summary>About us Page</summary>
<img src="docs/readme_images/lighthouse_about_us.png">
</details>

<details>
<summary>Thank you Page</summary>
<img src="docs/readme_images/lighthouse_thank_you.png">
</details>

<details>
<summary>Signup Page</summary>
<img src="docs/readme_images/lighthouse_signup.png">
</details>

<details>
<summary>Signin Page</summary>
<img src="docs/readme_images/lighthouse_signin.png">
</details>

<details>
<summary>Logout Page</summary>
<img src="docs/readme_images/lighthouse_signout.png">
</details>

<details>
<summary>Rest password Page</summary>
<img src="docs/readme_images/lighthouse_rest_password.png">
</details>



## MANUAL TESTING

### Browser Compatibility
  - Testing has been carried out on the following browsers :
  - Safari on macOS Ventura (Safari  Version 13.0.1)
  - Chrome Version Version  Version 108.0.5359.124 
### Test Cases and Results
 - Chrome Developer tools and Mozilla Firefox Web Developer Tools were used throughout the development of the site to test functionality, responsive 
    behaviour, alignment correctness etc:
     - BakckBerry z30
     - BlackBerry PlayBook
     - iPhone SE
     - iPhone XR
     - iPad Air
     - Surface Duo
     - Nest Hub
     - Nest Hub Max
#### Responsive Design
 - The display of the site has been made responsive to allow it to adapt for instance the grid structure layout to a single column.

<details>
<summary>Demo</summary>
<img src="">
</details
---

## Testing the user experience

### Viewing and Navigation

1. As a site user, I want to be able to intuitively navigate around the site so that I can find content.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|   |  |   |  |


| Element                 | Action                        | Expected Result                                                          | Pass/Fail |  
| ----------------------- | ----------------------------- | ------------------------------------------------------------------------ | --------- |  
| NavBar                  |                               |                                                                          |           |  
| Site Name/Logo          | Click                         | Redirect to home                                                         | Pass      |  
| Search Box Function     | Enter Text and Click Search   | Search both the product's title and description for a match.             | Pass      |  
| My Account Dropdown     | Click                         | Open profile dropdown                                                    | Pass      |  
| Sign Up Link            | Click                         | Redirect to Sign Up page (Not visible if user in session)                | Pass      |  
| login Link              | Click                         | Redirect to login page (Not visible if user in session)                  | Pass      |  
| Product Management Link | Click                         | Redirect to add_product page (Only visible if superuser in session)      | Pass      |  
| FAQ Management Link     | Click                         | Redirect to add_faq page (Only visible if superuser in session)          | Pass      |  
| My Profile Link         | Click                         | Redirect to user profile page (Only visible if user in session)          | Pass      |  
| Logout Link             | Click                         | Redirect to logout confirm page (Only visible if user in session)        | Pass      |  
| Bag Link                | Click                         | Redirect to bag page                                                     | Pass      |  
| Mobile Top Header       |                               |                                                                          |           |  
| Search Icon Button      | Click                         | Open up search box                                                       | Pass      |  
| Search Box Function     | Enter Text and Click Search   | Search both the product's title and description for a match.             | Pass      |  
| My Account Dropdown     | Click                         | Open profile dropdown                                                    | Pass      |  
| Sign Up Link            | Click                         | Redirect to Sign Up page (Not visible if user in session)                | Pass      |  
| login Link              | Click                         | Redirect to login page (Not visible if user in session)                  | Pass      |  
| Product Management Link | Click                         | Redirect to add_product page (Only visible if superuser in session)      | Pass      |  
| FAQ Management Link     | Click                         | Redirect to add_faq page (Only visible if superuser in session)          | Pass      |  
| My Profile Link         | Click                         | Redirect to user profile page (Only visible if user in session)          | Pass      |  
| Logout Link             | Click                         | Redirect to logout confirm page (Only visible if user in session)        | Pass      |  
| Bag Link                | Click                         | Redirect to bag page                                                     | Pass      |  
| Main Nav                |                               |                                                                          |           |  
| All Products            | Click                         | Redirect all products page                                               | Pass      |  
| Clitoral Vibrator Link  | Click                         | Redirect to prints page filtered to Clitoral Vibrator                    | Pass      |  
| G-spot Vibrator Link    | Click                         | Redirect to prints page filtered to G-spot Vibrator                      | Pass      |  
| Rabbit Vibrator Link    | Click                         | Redirect to prints page filtered to Rabbit Vibrator                      | Pass      |  
| About Us                | Click                         | Redirect to About US Page                                                | Pass      |  
| Contact Link            | Click                         | Open Contact Page                                                        | Pass      |  
| Home Link               | Click                         | Redirect to home (Only displays when screen size reduces to medium size) | Pass      |  
| Reviews Link            | Click                         | Redirect to reviews page                                                 | Pass      |  
| Hamburger Menu          | Responsive                    | Display when screen size reduces to medium size                          | Pass      |  
| Footer                  |                               |                                                                          |           |  
| Social Media Icon Links | Click                         | Open correct location in new tab                                         | Pass      |  
| Newsletter Email field  | Insert incorrect/empty format | On submit: form won't submit                                             | Pass      |  
| Newsletter Email field  | Insert incorrect/empty format | Error message displays                                                   | Pass      |  
| Subscribe Button        | Click                         | Form submit                                                              | Pass      |  
| Subscribe Button        | Click                         | Message appears saying Thank You for subscribing!                        | Pass      |  
| Privacy Policy Link     | Click                         | Open Privacy Policy Page in new tab                                      | Pass      |

<details>
<summary>Demo</summary>
<img src="">
</details>

---

2. As a site user, I want to be able to view a list of products so that I can select a product to view.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|   |  |   |  |


<details>
<summary>Demo</summary>
<img src="">
</details>

---

3. As a shopper, I want to be able to click on a product so that I can read the full product details.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|   |  |   |  |


| Element                  | Action                   | Expected Result                                                                              | Pass/Fail |
| ------------------------ | ------------------------ | -------------------------------------------------------------------------------------------- | --------- |
| Product Content          | Display                  | Display correct product image, excerpt, price, product details and dispatch time frame       | Pass      |
| Qty control buttons      | Click                    | Increase/decrease quantity                                                                   | Pass      |
| Qty control buttons      | Click                    | Minus button disabled if quantity is 1                                                       | Pass      |
| Qty control buttons      | Click                    | Plus button disabled if quantity is 99                                                       | Pass      |
| Qty control buttons      | Manually Input <1 or >99 | If quantity >99 or <1 manually entered, error message appears when Add to Bag button clicked | Pass      |
| Keep Shopping button     | Click                    | Redirect to home decor page                                                                  | Pass      |
| Add to bag button        | Click                    | Add item to bag                                                                              | Pass      |
| Add to bag button        | Click                    | Toast Success appears                                                                        | Pass      |
| Add to bag button        | Click                    | Product and quantity visible in toast success                                                | Pass      |
| If Superuser in session: |                          |                                                                                              |           |
| Edit product link        | Click                    | Redirect to edit product page                                                                | Pass      |
| Delete product link      | Click                    | Open delete confirmation page                                                                | Pass      |

<details>
<summary>Demo</summary>
<img src="">
</details>

---

4. As a shopper, I want to be able to view a specific category of products so that I can browse the type of products I'm interested in.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|   |  |   |  |


<details>
<summary>Demo</summary>
<img src="">
</details>

---

5. As a shopper, I want to be able to search all products so that I can find what I am looking for.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|   |  |   |  |


<details>
<summary>Demo</summary>
<img src="">
</details>

---

6. As a shopper, I want to be able to sort all products so that I can view products based on price or title.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|   |  |   |  |


<details>
<summary>Demo</summary>
<img src="">
</details>

---

7. As a site user, I want to be able to read reviews left by other customers so that I can have feedback insights from custommers.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|   |  |   |  |


<details>
<summary>Demo</summary>
<img src="">
</details>

---




### Registration and User Accounts

8. As a site user, I want to be able to register an account so that I can have a personal account and see my profile.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|   |  |   |  |


| Element                         | Action                                    | Expected Result                             | Pass/Fail |
| ------------------------------- | ----------------------------------------- | ------------------------------------------- | --------- |
| Sign Up                         |                                           |                                             |           |
| Sign in link                    | Click                                     | Redirect to sign in page                    | Pass      |
| Email field                     | Insert incorrect format                   | On submit: form won't submit                | Pass      |
| Email field                     | Insert incorrect format                   | Error message displays                      | Pass      |
| Email field                     | Insert correct format                     | On submit: form submit                      | Pass      |
| Email field                     | Leave empty                               | On submit: form won't submit                | Pass      |
| Email field                     | Insert duplicate email                    | On submit: form won't submit                | Pass      |
| Email field                     | Insert duplicate email                    | Error message displays                      | Pass      |
| Email Confirmation field        | Insert different email                    | On submit: form won't submit                | Pass      |
| Email Confirmation field        | Insert different email                    | Error message displays                      | Pass      |
| Username field                  | Leave empty/incorrect format              | On submit: form won't submit                | Pass      |
| Username field                  | Leave empty/incorrect format              | Error message displays                      | Pass      |
| Username field                  | Insert correct format                     | On submit: form submit                      | Pass      |
| Username field                  | Insert duplicate username                 | On submit: form won't submit                | Pass      |
| Username field                  | Insert duplicate username                 | Error message displays                      | Pass      |
| Password field                  | Insert incorrect format/length            | On submit: form won't submit                | Pass      |
| Password field                  | Insert incorrect format/length            | Error message displays                      | Pass      |
| Password field                  | Passwords don't match                     | On submit: form won't submit                | Pass      |
| Password field                  | Passwords don't match                     | Error message displays                      | Pass      |
| Password field                  | Insert correct format and passwords match | On submit: form submit                      | Pass      |
| Sign Up button(form valid)      | Click                                     | Form submit                                 | Pass      |
| Sign Up button(form valid)      | Click                                     | Redirect to Verify Email Address page       | Pass      |
| Sign Up button(form valid)      | Click                                     | Alert message confirming email sent appears | Pass      |
| Confirmation Email Confirm Link | Click                                     | Open Confirm Email Address Page             | Pass      |
| Confirm Button                  | Click                                     | Success message confirming new user appears | Pass      |
| Confirm Button                  | Click                                     | Redirect to sign in page                    | Pass      |

<details>
<summary>Demo</summary>
<img src="">
</details>

---

9. As a site user, I want to be able to login or logout so that I can access my personal info/keep my account secure.


| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|   |  |   |  |


| Element                         | Action                                    | Expected Result                             | Pass/Fail |
| ------------------------------- | ----------------------------------------- | ------------------------------------------- | --------- |
| Log in                          |                                           |                                             |           |
| Sign up link                    | Click                                     | Redirect to sign up page                    | Pass      |
| Username field                  | Leave empty                               | On submit: form won't submit                | Pass      |
| Username field                  | Leave empty                               | Error message displays                      | Pass      |
| Username field                  | Insert wrong username                     | On submit: form won't submit                | Pass      |
| Username field                  | Insert wrong username                     | Error message displays                      | Pass      |
| Password field                  | Leave empty                               | On submit: form won't submit                | Pass      |
| Password field                  | Leave empty                               | Error message displays                      | Pass      |
| Password field                  | Insert wrong password                     | On submit: form won't submit                | Pass      |
| Password field                  | Insert wrong password                     | Error message displays                      | Pass      |
| Login button(form valid)        | Click                                     | Form submit                                 | Pass      |
| Login button(form valid)        | Click                                     | Redirect to home page                       | Pass      |
| Login button(form valid)        | Click                                     | Success message confirming login appears    | Pass      |
| Forgot Password Link            | Click                                     | Redirect to Password Reset page             | Pass      |
| Email field                     | Leave empty/incorrect format              | On submit: form submit                      | Pass      |
| Reset My Password Button        | Click                                     | Confirmation message that email sent        | Pass      |
| Password Reset Email Link       | Click                                     | Open Change Password Page                   | Pass      |
| Change Password Button          | Click                                     | Success message confirming Password Changed | Pass      |
|                                 |                                           |                                             |           |
| Sign Out Confirmation           |                                           |                                             |           |
| Sign Out button                 | Click                                     | Redirect to homepage                        | Pass      |
| Sign Out button                 | Click                                     | Success message confirming Sign Out appears | Pass      |

<details>
<summary>Demo</summary>
<img src="">
</details>

---

10. As a site user, I want to be able to see my login status so that I can know if I'm logged in or out.


| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|   |  |   |  |


<details>
<summary>Demo</summary>
<img src="">
</details>

---

11. As a site user, I want to be able to save my personal details in my user profile so that I can spare the time to fill them out for future orders.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|   |  |   |  |


<details>
<summary>Demo</summary>
<img src="">
</details>

---

12. As a site user, I want to be able to have a personalised user profile so that I can with my personal order history and be able to update my default billing address.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|   |  |   |  |


<details>
<summary>Demo</summary>
<img src="">
</details>

---

13. As a site user, I want to be able to view my order history so that I can remember what purchases I've made.


| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|   |  |   |  |


<details>
<summary>Demo</summary>
<img src="">
</details>

---

14. As a site user, I want to be able to recover my password in case I forget so that I can recover access to my account.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|   |  |   |  |


<details>
<summary>Demo</summary>
<img src="">
</details>

---



### Purchasing and Checkout

15. As a shopper, I want to be able to add a number of products in different quantities to my shopping bag so that I can purchase them all at once.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|   |  |   |  |


<details>
<summary>Demo</summary>
<img src="">
</details>

---

16. As a shopper, I want to be able to view a running total of my shopping bag so that I can see how much it costs in total.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|   |  |   |  |


<details>
<summary>Demo</summary>
<img src="">
</details>

---

17. As a shopper, I want to be able to view the contents of my shopping bag at any time so that I can see what is included and the total cost.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|   |  |   |  |


<details>
<summary>Demo</summary>
<img src="">
</details>

---

18. As a shopper, I want to be able to adjust the quantity of individual products in my bag so that I can make changes before I purchase.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|   |  |   |  |


<details>
<summary>Demo</summary>
<img src="">
</details>

---

19. As a shopper, I want to be able to see a summary of my shopping cart when I checkout so that I can know what products are included and the total cost before I commit to purchasing.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|   |  |   |  |


<details>
<summary>Demo</summary>
<img src="">
</details>

---

20. As a shopper, I want to be able to enter my payment information securely so that I can purchase my chosen products quickly with no issues.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|   |  |   |  |


<details>
<summary>Demo</summary>
<img src="">
</details>

---

21. As a shopper, I want to be able to checkout as a guest so that I can avoid to sign up for an account.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|   |  |   |  |


<details>
<summary>Demo</summary>
<img src="">
</details>

---

22. As a shopper, I want to be able to view an order confirmation after checkout so that I can know my purchase was successful.


| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|   |  |   |  |


<details>
<summary>Demo</summary>
<img src="">
</details>

---

23. As a shopper, I want to be able to receive an email confirmation of my order so that I can have a record of my purchase.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|   |  |   |  |


<details>
<summary>Demo</summary>
<img src="">
</details>



---

### Admin & Store Management

24. As a site owner, I want to be able to add/edit/delete products through an easy-to-use interface so that I can can manage the store's contents.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|   |  |   |  |

| Element                         | Action                | Expected Result                                                                                                            | Pass/Fail |
| ------------------------------- | --------------------- | -------------------------------------------------------------------------------------------------------------------------- | --------- |
| Add Product                     | Access                | If a user tries to add a product (by changing the url) without being signed in they are redirected to the login page       | Pass      |
| Add Product                     | Access                | If a user tries to add a product (by changing the url) without being superuser they are redirected to a custom 403 page    | Pass      |
| Form Text Input (if required)   | Leave blank           | On Submit: Warning appears, form won't submit                                                                              | Pass      |
| Form Text Input (if required)   | Just input whitespace | On Submit: Form won't submit                                                                                               | Pass      |
| SKU                             | Duplicate Entry       | On Submit: Warning appears, form won't submit                                                                              | Pass      |
| Form image select button        | Click                 | Open device storage                                                                                                        | Pass      |
| Form image select button        | Display               | Chosen image name displayed once selected                                                                                  | Pass      |
| Form image select button        | Display               | Default image is used if no image is selected                                                                              | Pass      |
| Cancel button                   | Click                 | Redirect to Home page                                                                                                      | Pass      |
| Add Product button(form valid)  | Click                 | Form submit                                                                                                                | Pass      |
| Add Product button(form valid)  | Click                 | Redirect to Product detail page for new product with all information displaying correctly                                  | Pass      |
| Add Product button(form valid)  | Click                 | Success message appears informing the superuser that the product has been added                                            | Pass      |
|                                 |                       |                                                                                                                            |           |
|                                 |                       |                                                                                                                            |           |
| Edit Product                    |                       |                                                                                                                            |           |
| Element                         | Action                | Expected Result                                                                                                            | Pass/Fail |
| Edit Product                    | Access                | If a user tries to add a product (by changing the url) without being signed in they are redirected to the login page       | Pass      |
| Edit Product                    | Access                | If a user tries to add a product (by changing the url) without being superuser they are redirected to a custom 403 page    | Pass      |
| Edit Product Form               | Display               | Form has all the fields filled out with the original content                                                               | Pass      |
| Edit Product Form               | Image Field           | Thumbnail of original image is shown                                                                                       | Pass      |
| Form Text Input (if required)   | Leave blank           | On Submit: Warning appears, form won't submit                                                                              | Pass      |
| Form Text Input (if required)   | Just input whitespace | On Submit: Form won't submit                                                                                               | Pass      |
| Cancel button                   | Click                 | Redirect to Home page                                                                                                      | Pass      |
| Submit button(form valid)       | Click                 | Form submit                                                                                                                | Pass      |
| Edit Product button(form valid) | Click                 | Redirect to Product detail page for new product with all information displaying correctly                                  | Pass      |
| Edit Product button(form valid) | Click                 | Success message appears informing the superuser that the product has been updated                                          | Pass      |
|                                 |                       |                                                                                                                            |           |
| Confirm Delete Product          | Action                | Expected Result                                                                                                            | Pass/Fail |
| Delete Product                  | Access                | If a user tries to Delete a product (by changing the url) without being signed in they are redirected to the login page    | Pass      |
| Delete Product                  | Access                | If a user tries to Delete a product (by changing the url) without being superuser they are redirected to a custom 403 page | Pass      |
| Delete                          | Click                 | Redirect to home dpage                                                                                                     | Pass      |

<details>
<summary>Demo</summary>
<img src="">
</details>

---

### Contact

25. As a site user, I want to be able to submit an enquiry form so that I can report a personal matter

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|   |  |   |  |


| Element                       | Action                | Expected Result                                                                     | Pass/Fail |
| ----------------------------- | --------------------- | ----------------------------------------------------------------------------------- | --------- |
| Form Text Input (if required) | Leave blank           | On Submit: Warning appears, form won't submit                                       | Pass      |
| Form Text Input (if required) | Just input whitespace | On Submit: Warning appears Form won't submit                                        | Pass      |
| Email Input                   | User Logged In        | Email Field pre populated with user email address                                   | Pass      |
| Email Input                   | Incorrect Format      | On Submit: Warning appears, form won't submit                                       | Pass      |
| Enquiry Type Dropdown         | Click                 | Display all Enquiry Types in Database                                               | Pass      |
| Cancel button                 | Click                 | Redirect to Home page                                                               | Pass      |
| Submit button(form valid)     | Click                 | Form submit                                                                         | Pass      |
| Submit button(form valid)     | Click                 | Redirect to home Page                                                               | Pass      |
| Submit button(form valid)     | Click                 | Success message appears informing the superuser that the enquiry has been submitted | Pass      |
| Submit button(form valid)     | Click                 | User receives confirmation email about their enquiry                                | Pass      |

<details>
<summary>Demo</summary>
<img src="">
</details>

---

### Review

26. As a site user, I want to be able to add / edit / delete a review regarding one of the products in the site so that I can give my feedback.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|   |  |   |  |


<details>
<summary>Demo</summary>
<img src="">
</details>

---

### Newsletter

27. As a site user, I want to be able to sign up for the website's newsletter so that I can keep myself informed about new products and promotions from the site.


| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|   |  |   |  |


<details>
<summary>Demo</summary>
<img src="">
</details>

---



## BUGS

to come

| Bug           | Fix           |
| ------------- | ------------- |
|  |  |
|  |  |
|  | |
| |  |
|    |  |
| | |


[Back to README.md](README.md)