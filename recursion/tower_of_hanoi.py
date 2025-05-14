"""
The Tower of Hanoi is classic recursion problem where the goal was to move n disks from a source rods using an auxillary rod. following these rules:
1. Only one disk can be moved at a time.
2. A disk can only be placed on top of a larger disk.
3. All disks start on the source rod

The recursion solution breaks the problem into smaller subpronlems:
1. Move the top n-1 disks from the source rod to the auxillary rod.
2. Move the largest disk (nth) directly from the source rod to the target rod.
3. Move the n-1 disks from the auxillary rod to the target rod.
"""

# Tower of Hanoi implementation
def tower_of_hanoi(num_disks, source, target, auxillary):
    # Base case: If there's only one disk. move it from source to target
    if num_disks == 1:
        print(f"Move disks from {source} to {target}")
        return
    # step1: Move n-1 disks from the source rod to the auxillary rod
    tower_of_hanoi(num_disks-1, source, auxillary, target)
    # step 2: Move the nth disk from source to target
    print(f"Move disk {num_disks} from {source} to {target}")
    # step 3:  Move the n-1 disks from the auxiliary to target using source as a helper
    tower_of_hanoi(num_disks-1, auxillary, target, source)


tower_of_hanoi(3, 'A', 'C', 'B')
