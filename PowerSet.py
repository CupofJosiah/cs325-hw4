def powerset(inputSet):
    subsets = []

    def generate_subsets(inputSet, index, current_subset):
        if index == len(inputSet):
            subsets.append(current_subset)
            return
        generate_subsets(inputSet, index + 1,
                         current_subset + [inputSet[index]])
        generate_subsets(inputSet, index + 1, current_subset)

    generate_subsets(inputSet, 0, [])

    return subsets


print(powerset([1, 2, 3]))
