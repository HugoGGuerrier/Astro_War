import collections


class Timeline:
    """
    This class represent a timeline with a variate parameter
    """

    # ----- Constructor -----

    def __init__(self, duration: float = 0.0):
        """
        Create a new timeline with the wanted duration

        params :
            - duration: int = The timeline duration in milliseconds
        """

        self._duration: float = duration
        self._time: float = 0.0
        self._time_points: collections.OrderedDict = collections.OrderedDict()
        self._loop: bool = False
        self._running: bool = False

        self._initial_value: float = 0.0
        self._coef: float = 0.0
        self._previous_value: float = 0.0

        self._update_callback = None
        self._end_callback = None

    # ----- Timeline controlling methods -----

    def set_duration(self, duration: float) -> None:
        """
        Set the timeline duration

        params :
            - duration: int = The timeline duration in milliseconds
        """

        self._duration = duration

    def set_initial_value(self, value: float) -> None:
        """
        Set the timeline initial value

        params :
            - value: int = The initial value
        """

        self._initial_value = value
        self._previous_value = value

    def set_coef(self, coef: float) -> None:
        """
        Set the timeline coef

        params :
            - coef: int = The new coef
        """

        self._coef = coef

    def set_loop(self, loop: bool):
        """
        Set if the timeline has to loop

        params :
            - loop: bool = True if you want the timeline to loop
        """

        self._loop = loop

    def set_update_callback(self, callback) -> None:
        """
        Define the timeline callback function that will be called with the value

        params :
            - callback = The callback function that will be called
        """

        self._update_callback = callback

    def set_end_callback(self, callback) -> None:
        """
        Set the timeline end callback

        params :
            - callback = The function to call when the timeline is finish
        """

        self._end_callback = callback

    def add_time_point(self, time: float, value: float) -> None:
        """
        Add a new time point to the timeline

        params :
            - time: int = The time you want to add the point
            - value: int = The value to put at the time
        """

        self._time_points[time] = value
        self._time_points = collections.OrderedDict(sorted(self._time_points.items()))

    def get_value(self) -> float:
        """
        Get the timeline value at its current state

        return -> float = The current value
        """

        # Prepare the previous vars for the loop
        prev_time = 0
        prev_val = self._initial_value

        # Iterate over all time points and find the good one to calculate the value
        for time, val in self._time_points.items():
            if time >= self._time:
                time_coef = (self._time - prev_time) / (time - prev_time)
                return (time_coef * (val - prev_val)) + prev_val
            else:
                prev_time = time
                prev_val = val

        # Return the default value
        return prev_val

    def is_running(self) -> bool:
        """
        Get if the timeline is currently running
        """

        return self._running

    def is_finish(self) -> bool:
        """
        Get if the Timeline is finish
        """

        return self._time >= self._duration

    def start(self) -> None:
        """
        Start the timeline
        """

        self._running = True

    def pause(self) -> None:
        """
        Pause the timeline
        """

        self._running = False

    def reset(self) -> None:
        """
        Reset the timeline
        """

        self._time = 0.0
        self._running = False

    def update(self, dt: float) -> None:
        """
        Update the timeline with the delta time

        params :
            - dt: int = The delta time
        """

        # Verify the timeline is running
        if self._running:

            # Increase the time counter
            self._time += dt

            # Verify that the timeline is not finished
            if self._time > self._duration:
                if self._loop:
                    self._time = self._time % self._duration
                else:
                    self._time = self._duration
                    self.pause()
                    if self._end_callback is not None:
                        self._end_callback()

            # Get the current value and update the callback if needed
            if self._update_callback is not None:
                cur_val = self.get_value()
                if cur_val != self._previous_value:
                    self._previous_value = cur_val
                    self._update_callback(cur_val * self._coef)
