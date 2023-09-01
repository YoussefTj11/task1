def calculate_papers(amount):
    papers = [200, 100, 50, 20, 10, 5, 1]
    paper_counts = []

    for paper in papers:
        paper_count = amount // paper
        paper_counts.append(paper_count)
        amount %= paper

    return paper_counts

def print_papers(paper_counts):
    denominations = ['200 L.E.', '100 L.E.', '50 L.E.', '20 L.E.', '10 L.E.', '5 L.E.', '1 L.E.']
    output = []

    for i, count in enumerate(paper_counts):
        if count > 0:
            output.append(f"{count}x {denominations[i]}")

    print(" + ".join(output))

amount = int(input("Enter the amount in Egyptian Pounds: "))
paper_counts = calculate_papers(amount)

print("Papers needed:")
print_papers(paper_counts)
