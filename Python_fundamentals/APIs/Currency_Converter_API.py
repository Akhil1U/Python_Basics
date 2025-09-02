import os
import requests
from dotenv import load_dotenv


def load_api_key(from_currency):
    load_dotenv()
    api_key = os.getenv("CURRENCY_API_KEY")
    if not api_key:
        raise ValueError("API key not found....")
    return f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{from_currency}"



def fetch_exchange(api_url):

    try:
        response = requests.get(api_url)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.HTTPError as errH:
        print("HTTPS Error", errH)
    except requests.exceptions.ConnectionError as errC:
        print("internet connection not found", errC)
    except requests.exceptions.Timeout as errT: 
        print("TimeOut Error", errT)
    except KeyError:
        print("Unexpected response format.")
    except Exception as e:
        print("Something alse! An error occurred:", e)


def currency_converter(data,from_currency,to_currency,amount):
        conversion_rate = data['conversion_rates'].get(to_currency)
        if conversion_rate:
            print(f"{amount} {from_currency} = {conversion_rate*amount} {to_currency}")
        else:
            print(f"{to_currency} not found in response.")


def main():

    Currency_list  = "USD, AED, AFN, ALL, AMD, ANG, AOA, ARS, AUD, AWG, AZN, BAM, BBD, BDT, BGN, BHD, BIF, BMD, BND, BOB, BRL, BSD, BTN, BWP, BYN, BZD, CAD, CDF, CHF, CLP, CNY, COP, CRC, CUP, CVE, CZK, DJF, DKK, DOP, DZD, EGP, ERN, ETB, EUR, FJD, FKP, FOK, GBP, GEL, GGP, GHS, GIP, GMD, GNF, GTQ, GYD, HKD, HNL, HRK, HTG, HUF, IDR, ILS, IMP, INR, IQD, IRR, ISK, JEP, JMD, JOD, JPY, KES, KGS, KHR, KID, KMF, KRW, KWD, KYD, KZT, LAK, LBP, LKR, LRD, LSL, LYD, MAD, MDL, MGA, MKD, MMK, MNT, MOP, MRU, MUR, MVR, MWK, MXN, MYR, MZN, NAD, NGN, NIO, NOK, NPR, NZD, OMR, PAB, PEN, PGK, PHP, PKR, PLN, PYG, QAR, RON, RSD, RUB, RWF, SAR, SBD, SCR, SDG, SEK, SGD, SHP, SLE, SLL, SOS, SRD, SSP, STN, SYP, SZL, THB, TJS, TMT, TND, TOP, TRY, TTD, TVD, TWD, TZS, UAH, UGX, UYU, UZS, VES, VND, VUV, WST, XAF, XCD, XCG, XDR, XOF, XPF, YER, ZAR, ZMW, ZWL"
    print(Currency_list)
    from_currency = input("Enter the base currency from list (e.g., USD): ").upper().strip()
    to_currency = input("Enter the target currency from list(e.g., EUR): ").upper().strip()
    
    try:
        amount = float(input("Enter the amount: "))
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")
        return


    api_url = load_api_key(from_currency)
    Exchange_data = fetch_exchange(api_url)
    if Exchange_data:
        currency_converter(Exchange_data,from_currency, to_currency,amount)

if __name__ == "__main__":
    main()
