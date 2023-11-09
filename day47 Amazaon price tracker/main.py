import requests
from bs4 import BeautifulSoup




def service():
    url = input("Copy and paste the amazon product url you want to track.")
    print("Searching...")
    #headers needed for amazon 
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9,ml;q=0.8",
        "Cookie": "PHPSESSID=b9ced46f1f89626c09777e26b0350b02; _ga=GA1.2.914121524.1698835683; _gid=GA1.2.553125194.1698835683; _ga_VL41109FEB=GS1.2.1698835683.1.0.1698835683.0.0.0"
    }
    response = requests.get(url, headers=headers)
    #some websites only work in lxml parser
    soup = BeautifulSoup(response.text, "lxml")

    product_name = soup.find(name="span", id="productTitle").getText().strip()
    price = soup.find(name="span", class_="a-price-whole").getText()
    print(f"The current price for '{product_name}' is Rs:", price)

    start_service = input("Do you want to track the product?(Y/n)")
    if start_service == "Y" or start_service == "y" or start_service == "yes" or start_service == "Yes":

        low_amount = float(input("\n\nEnter the price, below which you are willing to buy the product. You can use this website if you want to check for the lowest price \nhttps://pricehistoryapp.com/\n Enter the Price:"))
        email = input("\n\nenter your email address: ")
        confirm = input("\n\nenter your email address again to confirm: ")
        if email == confirm:
            params = {
                "sheet1": {
                    "email": email,
                    "url":url,
                    "price":low_amount,
                    "product":product_name
                }
            }
            response = requests.post("https://api.sheety.co/2685834fb03a94b5b5ace8da905168f4/amazonPrice/sheet1", json=params)
            print(response.status_code)
            print(f"\n\nSuccess! You will get an email if the price of the product goes below Rs. {low_amount}")
        elif start_service == "N" or start_service == "n" or start_service == "no" or start_service == "No":
            service()
        else:
            print("invalid. Try again")
            service()

service()