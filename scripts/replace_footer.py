import os
from bs4 import BeautifulSoup

# Define your new footer content as an HTML string
new_footer_content = '''
<footer class="site-footer" id="colophon">
        <div class="top-footer">
          <div class="footer-overlay"></div>
          <div class="container">
            <div class="row">
              <div class="col-lg-3 col-md-6">
                <aside class="widget widget_text img-textwidget">
                  <div class="footer-logo">
                    <a href="index.html"
                      ><img alt="logo" src="assets/img/logo.png"
                    /></a>
                  </div>
                  <div class="textwidget widget-text">
                    Aenean maecenas, ridiculus quam bibendum quidem suspendisse
                    a, accusamus.
                  </div>
                  <ul class="footer-contact-info">
                    <li>
                      <a href="tel:+252 65 390 0373">
                        <i aria-hidden="true" class="icon icon-phone1"></i>
                        +252 65 390 0373
                      </a>
                    </li>
                    <li>
                      <a href="mailto:Info@Hornpetroleum.Com">
                        <i aria-hidden="true" class="icon icon-envelope3"></i>
                        Info@Hornpetroleum.Com
                      </a>
                    </li>
                  </ul>
                </aside>
                <div class="footer-social-links">
                  <ul>
                    <li>
                      <a
                        href="https://www.facebook.com/HornPetroleumGroup"
                        target="_blank"
                      >
                        <i aria-hidden="true" class="fab fa-facebook-f"></i>
                      </a>
                    </li>
                    <li>
                      <a href="https://x.com/horn_petroleum" target="_blank">
                        <i aria-hidden="true" class="fab fa-twitter"></i>
                      </a>
                    </li>
                    <li>
                      <a
                        href="https://www.instagram.com/horn_petroleum/?igshid=M2RkZGJiMzhjOQ%3D%3D"
                        target="_blank"
                      >
                        <i aria-hidden="true" class="fab fa-instagram"></i>
                      </a>
                    </li>
                    <!-- <li>
                      <a href="https://www.youtube.com/" target="_blank">
                        <i aria-hidden="true" class="fab fa-youtube"></i>
                      </a>
                    </li> -->
                  </ul>
                </div>
              </div>
              <div class="col-lg-3 col-md-6">
                <aside class="widget">
                  <h5 class="title-divider-right">Our Services</h5>
                  <ul>
                    <li>
                      <a href="car_wash.html">Car Wash</a>
                    </li>
                    <li>
                      <a href="oil_change.html">Oil Change</a>
                    </li>
                    <li>
                      <a href="#">24/7 Support</a>
                    </li>
                    <li>
                      <a href="#">Fuel Stations</a>
                    </li>
                    <li>
                      <a href="service-detail.html">Gas Delivery</a>
                    </li>
                    <!-- <li>
                      <a href="service-detail.html">Building Services</a>
                    </li> -->
                  </ul>
                </aside>
              </div>
              <div class="col-lg-3 col-md-6">
                <aside class="widget">
                  <h5 class="title-divider-right">Useful Links</h5>
                  <ul>
                    <li>
                      <a href="index.html">Home Page</a>
                    </li>
                    <li>
                      <a href="index.html">Building Technology</a>
                    </li>
                    <li>
                      <a href="about.html">About Us</a>
                    </li>
                    <li>
                      <a href="index.html">Station service</a>
                    </li>
                    <li>
                      <a href="contact.html">Contact us</a>
                    </li>
                    <!-- <li>
                      <a href="contact.html">24 Hour Support</a>
                    </li> -->
                  </ul>
                </aside>
              </div>
              <div class="col-lg-3 col-md-6">
                <aside class="widget widget_text">
                  <h5 class="title-divider-right">Newsletter Sign Up</h5>
                  <div class="textwidget widget-text">
                    Sign Up To Get Exclusive Offers And News From Our Favorite
                    Brands !
                  </div>
                  <form class="footer-form">
                    <div class="form-group">
                      <input
                        name="emal"
                        placeholder="Your email address.."
                        type="email"
                      />
                    </div>
                    <button class="button-round-gradient">SUBSCRIBE NOW</button>
                  </form>
                </aside>
              </div>
            </div>
          </div>
        </div>
        <div class="bottom-footer">
          <div class="copy-right text-center">
            Copyright © 2023 E-Vehicle. All rights reserved.
          </div>
        </div>
      </footer>
'''

# Function to replace the footer in a given HTML file
def replace_footer_in_html(file_path):
    try:
        # Open the file and read its content
        with open(file_path, 'r', encoding='utf-8') as file:
            html_content = file.read()

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')

        # Find the existing <footer> tag
        footer = soup.find('footer')

        if footer:
            # Replace the existing footer with the new footer
            footer.replace_with(BeautifulSoup(new_footer_content, 'html.parser'))

            # Save the modified HTML back to the file
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(str(soup))

            print(f"Footer replaced successfully in {file_path}")
        else:
            print(f"No <footer> tag found in {file_path}.")
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

# Function to replace footer in all HTML files in a directory
def replace_footer_in_directory(directory_path):
    # Walk through the directory
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.html'):  # Check if it's an HTML file
                file_path = os.path.join(root, file)
                replace_footer_in_html(file_path)

# Example usage
directory_path = 'C:\\Users\\lenovo\\Desktop\\evehicle\\evehicle'  # Replace with your directory path
replace_footer_in_directory(directory_path)
