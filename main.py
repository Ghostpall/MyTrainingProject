def main():
    practice_dictionary = ["Iemand die er niet bij hoord", {"Familie":{"Zus_1": "Eva", "Zus_2": "Tara"}}]
    practice_dictionary[1]["Familie"]["Moeder"] =  "Mariska"
    practice_dictionary.append("Vrienden")
    print (f'{practice_dictionary}' )


if __name__ == "__main__":
    main()