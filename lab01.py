def main():
    cost_per_item = 19.99
    quantity = 5 

    # YOUR CODE TO CALCULATE THE TOTALS GOES HERE 
    #calculating subtotal
    subtotal_cost = cost_per_item*quantity   

    #calculating tax
    tax = subtotal_cost*.13

    #calculating total cost
    total_cost = subtotal_cost+tax

    print(f'cost_per_item = ${cost_per_item:0.2f}') # a sample for you to use for the other prices

    # YOUR CODE TO PRINT THE TOTALS GOES HERE
    print(f'quantity = {quantity}')
    print(f'subtotal_cost = ${subtotal_cost:0.2f}')
    print(f'tax = ${tax:0.2f}')
    print(f'total_cost = ${total_cost:0.2f}')

if __name__ == "__main__":
    main()
