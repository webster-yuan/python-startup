def zip_main():
    names = ['tom', 'jerry', 'spike']
    ages = [12, 23, 34]
    d = dict(zip(names, ages))
    print(d)  # {'tom': 12, 'jerry': 23, 'spike': 34}


if __name__ == '__main__':
    zip_main()
