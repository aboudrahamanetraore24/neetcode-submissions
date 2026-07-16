class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        seen = dict()

        for x in nums:
            seen[x] = seen.get(x, 0)+1

        buckets = [[] for _ in range(n+1)]
        for key,val in seen.items():
            buckets[val].append(key)
        out = []
        for bucket in reversed(buckets):
            if bucket:
                for x in bucket:
                    out.append(x)
                    if len(out) == k:
                        return out
        return out