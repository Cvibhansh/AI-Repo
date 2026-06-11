# metrics.py

def calculate_accuracy(correct, total):
    """
    Calculate accuracy percentage.
    """
    if total == 0:
        return 0.0

    return (correct / total) * 100


def calculate_average_latency(total_latency, total_requests):
    """
    Calculate average response time.
    """
    if total_requests == 0:
        return 0.0

    return total_latency / total_requests


def calculate_failure_count(correct, total):
    """
    Number of failed test cases.
    """
    return total - correct


def summarize_metrics(correct,
                      total,
                      total_latency):
    """
    Returns a dictionary containing all metrics.
    """

    accuracy = calculate_accuracy(
        correct,
        total
    )

    avg_latency = calculate_average_latency(
        total_latency,
        total
    )

    failures = calculate_failure_count(
        correct,
        total
    )

    return {
        "accuracy": accuracy,
        "avg_latency": avg_latency,
        "failures": failures
    }