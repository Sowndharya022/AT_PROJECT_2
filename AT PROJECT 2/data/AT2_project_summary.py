# AT Project 2
# System Description
# The OrangeHRM System is a web based manages employee photos. Employees can add or change their own photos and Human Resources can add or change everyone's photos. The system produces lists of photos by different selection criteria. Its photos will be used by many other systems in the company. The photos are stored in a configurable file structure and the photo location is pointed to by a file system. This release only includes employee photos and name and address and social security information and not any of the other information planned for later.
# Test Cases dealing the with login (CREATE ALL POSITIVE AND NEGATIVE SCENARIOS)
#
# Test case ID: TC_PIM_01
# Test objective:
# Forgot Password link validation on login page
# URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
# Precondition:
# 1. Launch URL
# 2. Orange HRM 3.0 site is launched on a compatible browser
# 3. Click on "Forgot Password" link.
# Steps:
# 1. Username textbox is visible.
# 2. Provide your username.
# 3. Click on Reset Password
# Expected Result:
# The user should be able to see the username box and get a successful message saying "Reset Password link sent successfully".


# Test cave ID: TC_PIM_02
# Test objective:
# Header Validation on Admin Page
# Precondition:
# 1. Launch URL and Login as "Admin".
# 2. Orange HRM 3.0 site is launched on a compatible browser
# Steps:
# 1. Go to Admin page and Validate "Title" of the page as "OrangeHRM".
# 2. Validate the below options are displaying on Admin page:
# a) User Management
# b) Job
# c) Organization
# d) Qualifications
# e) Nationalities
# f) Corporate Banking
# g) Configuration
# Expected Result:
# The user should be able to see the above mentioned Admin Page Headers on Admin Page

# Test cave ID: TC_PIM_02
# Test objective:
# Header Validation on Admin Page
# Precondition:
# 1. Launch URL and Login as "Admin".
# 2. Orange HRM 3.0 site is launched on a compatible browser
# Steps:
# 1. Go to Admin page and Validate "Title" of the page as "OrangeHRM".
# 2. Validate the below options are displaying on Admin page:
# a) User Management
# b) Job
# c) Organization
# d) Qualifications
# e) Nationalities
# f) Corporate Banking
# g) Configuration
# Expected Result:
# The user should be able to see the above mentioned Admin Page Headers on Admin Page

