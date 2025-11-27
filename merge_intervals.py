
def merger_intervals(intervals):
    intervals.sort(key=lambda x: x[0]) # Sort intervals based on start time
    merged = []

    for interval in intervals:
        if not merged or interval[0] > merged[-1][1]: #No overlap
            merged.append(interval) # Add interval to merged list
        else: # Overlap
            merged[-1][1] = max(merged[-1][1], interval[1]) # Merge intervals
    return merged

# Example usage
intervals = [[1,3],[2,4],[5,7],[10,15],[6,8]]
print(merger_intervals(intervals))  # Output: [[1,4],[5,8]]

# Here’s a beginner-friendly explanation of this line:
#
# intervals.sort(key=lambda x: x[0])
#
# 🟦 What is intervals?
#
# It’s a list of intervals, like:
#
# intervals = [[1,3], [8,10], [2,6], [15,18]]
#
#
# Each interval is a list:
#
# [start, end]
#
# 🟦 Goal: Sort the intervals by their START time
#
# We want to arrange them in this order:
#
# [1,3]
# [2,6]
# [8,10]
# [15,18]
#
#
# so that merging becomes easy.
#
# 🟦 Why do we sort?
#
# Because merging overlapping intervals only works correctly when they’re in order of their start times.
#
# 🟦 What does key=lambda x: x[0] mean?
#
# Let’s break it down:
#
# ✔ x
#
# is each interval while sorting.
#
# Example:
#
# First: x = [1,3]
#
# Next: x = [8,10]
#
# Next: x = [2,6]
#
# ✔ x[0]
#
# means:
#
# “Take the START value of the interval.”
#
# So:
#
# Interval x	x[0]
# [1,3]	1
# [8,10]	8
# [2,6]	2
# [15,18]	15
#
# Python uses these start values to sort.
#
# 🧒 Explain Like a Kid
#
# Imagine each interval is a card:
#
# [8,10]
# [1,3]
# [15,18]
# [2,6]
#
#
# Sorting with key=lambda x: x[0] means:
#
# “Look at the FIRST number of each card and arrange them in order.”
#
# So:
#
# First look at 8
#
# Then 1
#
# Then 15
#
# Then 2
#
# Sort these: 1, 2, 8, 15
#
# So intervals reorder to:
#
# [1,3], [2,6], [8,10], [15,18]
#
# 🟦 Simple Visual
#
# Sorting by x[0]:
#
# [1,3]   # 1
# [2,6]   # 2
# [8,10]  # 8
# [15,18] # 15
#
# ⭐ SUPER SHORT SUMMARY
#
# intervals.sort(key=lambda x: x[0]) means:
#
# 👉 “Sort the list by the first number of each interval.”
#
# This ensures intervals are in correct order before merged

# for interval in intervals:
#     if not merged or interval[0] > merged[-1][1]:
#         merged.append(interval)
#     else:
#         merged[-1][1] = max(merged[-1][1], interval[1])
# Assume intervals are already sorted by their start time.
#
# 🟦 First line: for interval in intervals:
# We are going through each interval one by one.
#
# If:
#
# python
# Copy code
# intervals = [[1,3], [2,6], [8,10], [15,18]]
# Then interval will be:
#
# First loop → [1,3]
#
# Second loop → [2,6]
#
# Third loop → [8,10]
#
# Fourth loop → [15,18]
#
# 🟦 Second line: if not merged or interval[0] > merged[-1][1]:
# This line decides:
#
# “Should I start a new interval, or merge with the previous one?”
#
# Let’s break this condition into two parts:
#
# 🔹 Part 1: if not merged
# This means:
#
# “Is merged list empty?”
#
# At the very beginning, merged = [], so not merged is True.
#
# That means for the very first interval, we always just add it.
#
# 🔹 Part 2: interval[0] > merged[-1][1]
# interval[0] → start of current interval
#
# merged[-1] → last interval we added into merged
#
# merged[-1][1] → end of last merged interval
#
# So this checks:
#
# “Is the current start > last end?”
#
# If yes → they do NOT overlap → start a new separate interval.
#
# ✅ So full if condition means:
# python
# Copy code
# if merged is empty
#    OR
#    current interval does NOT overlap with last merged interval:
#        add it as new interval
# 🟦 Third line: merged.append(interval)
# If condition is True, we do:
#
# “Add this interval as it is. No merging needed.”
#
# Example:
#
# merged = [[1,6]]
#
# interval = [8,10]
#
# Is 8 > 6? → Yes → no overlap
#
# So:
#
# python
# Copy code
# merged.append([8,10])
# Now:
#
# python
# Copy code
# merged = [[1,6], [8,10]]
# 🟦 Else part: overlapping case
# python
# Copy code
# else:
#     merged[-1][1] = max(merged[-1][1], interval[1])
# We come here when:
#
# python
# Copy code
# interval[0] <= merged[-1][1]
# That means:
#
# Current interval overlaps with the last one.
#
# So we need to merge.
#
# 🔹 merged[-1][1]
# This is the end of the last merged interval.
#
# 🔹 interval[1]
# This is the end of the current interval.
#
# We do:
#
# python
# Copy code
# merged[-1][1] = max(merged[-1][1], interval[1])
# Meaning:
#
# “Set the last interval’s end to the larger of the two ends.”
#
# Because merging [1,3] and [2,6] gives [1,6], so we take the bigger end (6).
#
# 🟦 Full Dry Run (with comments)
# Take:
#
# python
# Copy code
# intervals = [[1,3],[2,6],[8,10],[15,18]]
# merged = []
# 🔹 Loop 1: interval = [1,3]
# merged is empty → not merged is True
#
# So we append:
#
# python
# Copy code
# merged = [[1,3]]
# 🔹 Loop 2: interval = [2,6]
# Check condition:
#
# not merged? → False (merged has one item)
#
# interval[0] > merged[-1][1] → 2 > 3? → False
#
# So condition is False → go to else:
#
# python
# Copy code
# merged[-1][1] = max(3, 6)  # 6
# So:
#
# python
# Copy code
# merged = [[1,6]]
# We merged [1,3] and [2,6] into [1,6].
#
# 🔹 Loop 3: interval = [8,10]
# Check:
#
# not merged? → False
#
# interval[0] > merged[-1][1] → 8 > 6? → True
#
# So we append:
#
# python
# Copy code
# merged.append([8,10])
# merged = [[1,6], [8,10]]
# No merge, separate range.
#
# 🔹 Loop 4: interval = [15,18]
# Check:
#
# interval[0] > merged[-1][1] → 15 > 10? → True
#
# So:
#
# python
# Copy code
# merged.append([15,18])
# merged = [[1,6], [8,10], [15,18]]
# Done ✅
#
# 🟦 Super Short Summary (for your brain)
# If merged is empty → just add interval.
#
# If current start > last end → no overlap → add as new interval.
#
# Else → overlap → update last interval’s end to max(last_end, current_end).
#
# Once this clicks, Merge Intervals becomes very easy for you.

# 🟦 TIME COMPLEXITY
#
# Sorting → O(n log n)
# One loop → O(n)
#
# Total:
#
# O(n log n)
#
# Space:
#
# O(n)