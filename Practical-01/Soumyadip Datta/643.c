double findMaxAverage(int* nums, int numsSize, int k) {
    long long window = 0;
    for (int i = 0; i < k; i++) {
        window += nums[i];
    }

    long long best = window;
    for (int i = k; i < numsSize; i++) {
        window += nums[i] - nums[i - k];
        if (window > best) best = window;
    }

    return (double)best / k;
}