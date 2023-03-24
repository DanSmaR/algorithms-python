def study_schedule(permanence_period, target_time):
    if not isinstance(target_time, int):
        return None
    target_frequency = 0
    for start_period, final_period in permanence_period:
        if not isinstance(start_period, int) or not isinstance(
            final_period, int
        ):
            return None
        if start_period <= target_time <= final_period:
            target_frequency += 1
    return target_frequency
