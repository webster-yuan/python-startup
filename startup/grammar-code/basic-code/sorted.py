def sorted_main():
    rows = [{'name': 'A', 'score': 88},
            {'name': 'B', 'score': 77},
            {'name': 'C', 'score': 95}]
    ranked = sorted(rows, key=lambda x: x['score'], reverse=True)
    # [{'name': 'C', 'score': 95}, {'name': 'A', 'score': 88}, {'name': 'B', 'score': 77}]
    print(ranked)


sorted_main()
