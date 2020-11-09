def finder(files, queries):
    result = []
    zed = {}
    for file in files:
        xfiles = file.split("/")
        yes = xfiles[-1]
        if yes not in zed:
            zed[yes] = []
        zed[yes].append(file)
    for query in queries:
        if query in zed:
            result.extend(zed[query])
    return result

if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
