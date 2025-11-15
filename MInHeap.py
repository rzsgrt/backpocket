class MinHeapExplanation:
    def __init__(self):
        self.data = list()  # Create empty list

    def remove_min_value(self):
        if not self.data:
            return None
        if len(self.data) == 1:
            return self.data.pop()  # just give what inside
        min_value = self.data[0]  # Always at zero
        self.data[0] = (
            self.data.pop()
        )  # Do not change tree structure just use last value in list
        self._bubble_down(0)  # Check tree structure again
        return min_value

    def _bubble_down(self, index):
        # in here parent means index and index means parent
        size = len(self.data)
        smallest = index
        while True:
            left = 2 * index + 1  # we need to step 2 times + 1 for left node
            right = 2 * index + 2  # + 2 for right node
            if left < size and self.data[left] < self.data[smallest]:
                # Smallest one in the left
                smallest = left
            if right < size and self.data[right] < self.data[smallest]:
                # Smallest one in the right
                smallest = right
            # We compare three value, index, left node and right node.
            # we switch parent (index) to whoever
            # have smallest value (either lett or right)

            if smallest == index:
                # parent already smallest
                break

            # Enough playing with index, now change actual value
            self.data[smallest], self.data[index] = (
                self.data[index],
                self.data[smallest],
            )

            index = smallest

    def insert(self, value):
        self.data.append(value)  # always add new value to last index
        self._bubble_up()  # Fixing new value

    def _bubble_up(self):
        index = len(self.data) - 1
        while index > 0:
            parent = (index - 1) // 2  # this is how to get parent
            if (
                self.data[index] < self.data[parent]
            ):  # Check if parent is bigger
                self.data[index], self.data[parent] = (
                    self.data[parent],
                    self.data[index],
                )
                index = parent
            else:
                break
