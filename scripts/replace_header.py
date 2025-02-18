import os
from bs4 import BeautifulSoup

# Define your new header content as an HTML string
new_header_content = '''
<header class="site-header site-header-transparent">
        <!-- header html start -->
        <div class="upper-header">
          <div class="container">
            <div class="row align-items-center">
              <div
                class="col-lg-6 d-flex align-items-center header-banner-info justify-content-lg-start justify-content-around"
              >
                <p>Get started with us, You will need a good plan !</p>
                <span class="start-btn">
                  <a href="contact.html">GET STARTED</a>
                </span>
              </div>
              <div
                class="col-lg-6 d-flex justify-content-lg-end justify-content-center align-items-center header-location"
              >
                <i class="fas fa-map-marker-alt"></i> Hargeisa,Damal Bussiness
                Center 2nd Floor.
              </div>
            </div>
          </div>
        </div>
        <div class="top-header">
          <div class="container">
            <div class="row align-items-center justify-content-lg-start">
              <div class="site-identity col-lg-3 col-sm-12 col-6">
                <p class="site-title">
                  <a href="index.html">
                    <img alt="logo" src="assets/img/logo.png" />
                  </a>
                </p>
              </div>
              <div
                class="col-lg-9 col-sm-12 col-6 d-flex justify-content-lg-end justify-content-sm-around justify-content-end"
              >
                <div class="header-contact-info">
                  <ul>
                    <li>
                      <a href="tel:+252 65 390 0373">
                        <span class="icon">
                          <i aria-hidden="true" class="icon icon-phone"></i>
                        </span>
                        <div class="details-content">
                          <span class="content-title">Call us now :</span>
                          <h6>+252 65 390 0373</h6>
                        </div>
                      </a>
                    </li>
                    <li>
                      <a href="mailto:Info@Hornpetroleum.Com">
                        <span class="icon">
                          <i aria-hidden="true" class="icon icon-envelope3"></i>
                        </span>
                        <div class="details-content">
                          <span class="content-title">Email us now :</span>
                          <h6>Info@Hornpetroleum.Com</h6>
                        </div>
                      </a>
                    </li>
                  </ul>
                </div>
                <div class="header-social social-links">
                  <ul>
                    <li>
                      <a
                        href="https://www.facebook.com/HornPetroleumGroup"
                        target="_blank"
                      >
                        <i aria-hidden="true" class="fab fa-facebook"></i>
                      </a>
                    </li>
                    <li>
                      <a href="https://x.com/horn_petroleum" target="_blank">
                        <i aria-hidden="true" class="fab fa-twitter"></i>
                      </a>
                    </li>
                    <!-- <li>
                      <a href="https://www.youtube.com" target="_blank">
                        <i aria-hidden="true" class="fab fa-youtube"></i>
                      </a>
                    </li> -->
                    <li>
                      <a
                        href="https://www.instagram.com/horn_petroleum/?igshid=M2RkZGJiMzhjOQ%3D%3D"
                        target="_blank"
                      >
                        <i aria-hidden="true" class="fab fa-instagram"></i>
                      </a>
                    </li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="bottom-header" id="masthead">
          <div class="container">
            <div
              class="hb-group d-flex align-items-center justify-content-between"
            >
              <div class="main-navigation col-lg-9 d-flex align-items-center">
                <div class="logo-bottom-header">
                  <a href="index.html">
                    <img alt="logo" src="assets/img/logo.png" />
                  </a>
                </div>
                <nav
                  class="navigation d-none d-lg-inline-block"
                  id="navigation"
                >
                  <ul>
                    <li class="current-menu-item">
                      <a href="index.html">Home</a>
                    </li>
                    <li>
                      <a href="product-archive.html">Products</a>
                    </li>
                    <li>
                      <a href="Tracking-orders.html">Tracking orders</a>
                    </li>
                    <li>
                      <a href="about.html">About us</a>
                    </li>
                    <li>
                      <a href="contact.html">Contact us</a>
                    </li>
                  </ul>
                </nav>
              </div>
              <div
                class="col-lg-3 col-12 d-flex justify-content-lg-end justify-content-between"
              >
                <span class="header-search-icon">
                  <button class="search-icon">
                    <i class="fas fa-search"></i>
                  </button>
                </span>
                <div class="header-btn d-inline-block">
                  <a class="button-round-gradient" href="login.html"
                    >LOGIN/REGISTER</a
                  >
                </div>
                <div
                  class="align-items-center button-round-gradient cart-num d-flex ms-3 rounded-0 position-relative cart-num"
                >
                  <i class="fas fa-shopping-cart"></i>
                  <div class="num position-absolute"></div>
                </div>
              </div>
            </div>
          </div>
          <div class="mobile-menu-container"></div>
        </div>
      </header>
'''

# Function to replace the header in a given HTML file
def replace_header_in_html(file_path):
    try:
        # Open the file and read its content
        with open(file_path, 'r', encoding='utf-8') as file:
            html_content = file.read()

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')

        # Find the existing <header> tag
        header = soup.find('header')

        if header:
            # Replace the existing header with the new header
            header.replace_with(BeautifulSoup(new_header_content, 'html.parser'))

            # Save the modified HTML back to the file
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(str(soup))

            print(f"Header replaced successfully in {file_path}")
        else:
            print(f"No <header> tag found in {file_path}.")
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

# Function to replace header in all HTML files in a directory
def replace_header_in_directory(directory_path):
    # Walk through the directory
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.html'):  # Check if it's an HTML file
                file_path = os.path.join(root, file)
                replace_header_in_html(file_path)

# Example usage
directory_path = 'C:\\Users\\lenovo\\Desktop\\evehicle\\evehicle'  # Replace with your directory path
replace_header_in_directory(directory_path)
