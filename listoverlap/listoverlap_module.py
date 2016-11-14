def listoverlap(list1, list2):
    result = []
    result_overlap = [i for i in set(list1) if i in list2]
    for element in result_overlap:
      if element not in result:
        result.append(element)
    return result

def main():
    return

if __name__ == '__main__':
    main()
