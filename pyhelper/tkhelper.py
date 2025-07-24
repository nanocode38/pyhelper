import os.path
import time
import tkinter as tk
from collections.abc import Iterable
from enum import Enum, Flag, auto
from tkinter import messagebox, ttk
from typing import List, Optional

DEBUG = os.path.exists("../DEBUG") or os.path.exists("/DEBUG")
if DEBUG:
    print("\033[91m[DEBUG] Running in debug mode")
    print("[DEBUG] Warning: DEBUG MODE!!!!\033[0m")

Direction, Seconds, px = str, int, int

__all__ = [
    "RetMode",
    "shake_window",
    "window_sleep",
    "password_window",
    "center_window",
    "setting_password_window",
    "Rect",
    "MessageboxMode",
    "show_messagebox",
    "pix_to_fontsize",
    "fontsize_to_pix",
]


class RetMode(Flag):
    """Result status flags for password window operations"""

    SUCCESS = auto()  # Password verification succeeded
    ABORTED = auto()  # Operation was canceled by user
    VIA_BUTTON = auto()  # Action initiated through button press
    VIA_WINDOW_CLOSE = auto()  # Action initiated through window closure

    # Predefined status combinations
    USER_CANCEL = VIA_BUTTON | ABORTED
    WINDOW_CLOSE = VIA_WINDOW_CLOSE | ABORTED


class MessageboxMode(Enum):
    """The mode of the messagebox"""

    INFO = auto()
    WARNING = auto()
    ERROR = auto()
    QUESTION = auto()
    YESNO = auto()
    YESNOCANCEL = auto()
    RETRYCANCEL = auto()


def shake_window(
    window, dire: Direction = "vertical", jitter_time: Seconds = 2, jitter_count: int = 50, amplitude: px = 1
) -> None:
    """
    Shake the Tkinter window

    Args:
        window: , needs to have winfo_x(), winfo_y(), update() and geometr() methods
        dire: Shaking Direction, can be 'vertical' or 'horizontal'
        jitter_time: Total duration of the shaking effect, in Seconds, integer
        jitter_count: Number of shakes, up and down count as two, integer
        amplitude: Amplitude of the shake, in pixels, integer

    Raises:
        ValueError: When dire is not 'vertical' or 'horizontal'
    """
    window.update()
    home_position = window.winfo_x(), window.winfo_y()
    for i in range(jitter_count):
        start_time = time.time()
        sign = -1 if i % 2 == 0 else 1
        if dire == "horizontal":
            window.geometry(f"+{home_position[0]}+{home_position[1] + sign * amplitude}")
        elif dire == "vertical":
            window.geometry(f"+{home_position[0] + sign * amplitude}+{home_position[1]}")
        else:
            raise ValueError("Direction must be vertical or horizontal")
        while time.time() - start_time < jitter_time / jitter_count:
            window.update()
    window.geometry(f"+{home_position[0]}+{home_position[1]}")
    window.update()


def center_window(window, dire: Direction = "all") -> None:
    """
    Center your Tkinter window


    Args:
        window: The Tkinter window to be centered
        dire: The Direction of centering, can be 'all', 'vertical' or 'horizontal'

    Raises:
        ValueError: When dire is not any one of 'all', 'vertical' or 'horizontal'
    """
    window.update()
    dire = dire.lower()
    screen_size = window.winfo_screenwidth(), window.winfo_screenheight()
    window_size = window.winfo_width(), window.winfo_height()
    x, y = (screen_size[0] - window_size[0]) // 2, (screen_size[1] - window_size[1]) // 2
    this_x, this_y = window.winfo_x(), window.winfo_y()
    if dire == "all":
        window.geometry(f"+{x}+{y}")
    elif dire == "vertical":
        window.geometry(f"+{x}+{this_y}")
    elif dire == "horizontal":
        window.geometry(f"+{this_x}+{y}")
    else:
        raise ValueError("Direction must be all, vertical or horizontal")
    window.update()


# LEGACY: The Old Version (Just take it from time to time, don’t delete it! There is an obvious bug, don’t use it!)
# def password_window(password: str, title: str="Password", text: str="Please input your Password", *, parent: None | tk.Wm = None, mask: None | str=None, error_message: None | str=None, topmost=False):
#     """
#     Create a password input window using Tkinter.
#
#     This function generates a window prompting the user to input a password.
#     It validates the entered password and performs actions based on the correctness of the input.
#
#     :param password: The correct password string that the user needs to input.
#     :param title: The title of the password window (default is "Password").
#     :param text: The prompt text displayed in the window (default is "Please input your Password").
#     :param mask: Optional character to mask the password input (e.g., '*' or None for no masking).
#     :param error_message: Optional custom error message when the password is incorrect.
#                           If not provided, the window will shake to indicate an error.
#     :param topmost: Boolean indicating whether the window should stay on top of others (default is False).
#
#     :return: Returns 1 if the correct password is entered and the window is closed successfully, otherwise returns 0.
#
#     Functionality:
#     - Displays a Tkinter window with a label, an entry field for password input, and two buttons ("OK" and "Cancel").
#     - Validates the entered password against the provided `password`.
#     - If the password is correct, the window closes and returns 1.
#     - If the password is incorrect:
#         - Shakes the window if no custom `error_message` is provided.
#         - Displays an error popup with the custom `error_message` if it is provided.
#     - Centers the window on the screen using the `center_window` function.
#     - Supports optional parameters for customizing the appearance and behavior of the password window.
#     """
#     return_val = 0
#     from tkinter import ttk
#     window = tk.Toplevel(parent) if parent else tk.Tk()  # 支持作为子窗口
#     window.wm_attributes('-topmost', topmost)
#     window.geometry('300x150')
#     window.title(title)
#     tk.Label(window, text=text).place(x=10, y=2)
#     entry = ttk.Entry(window, show=mask, width=40)
#     entry.place(x=10, y=50)
#     def ok():
#         nonlocal entry, password, return_val, window, error_message
#         if entry.get() == password:
#             window.destroy()
#             return_val = 1
#             return return_val
#         if not error_message:
#             shake_window(window)
#         else:
#             from tkinter import messagebox
#             messagebox.showerror(title="Password Error", message=error_message)
#     def on_cancel():
#         nonlocal return_val
#         return_val = -1  # Clearly marked as "User Cancel"
#         window.destroy()
#
#     ttk.Button(window, text="Cancel", command=on_cancel).place(x=105, y=120)
#     ttk.Button(window, text="OK", command=ok).place(x=205, y=120)
#     center_window(window)
#     if not parent:  # 如果是独立窗口
#         window.wait_window()  # 非阻塞等待
#     else:           # 如果是子窗口
#         window.transient(parent)
#         window.grab_set()
#         parent.wait_window(window)
#
#     return return_val


def password_window(
    password: str,
    title: str = "Password",
    prompt: str = "Please enter your password",
    *,
    mask: str | None = None,
    error_message: str | None = None,
    topmost: bool = False,
    parent: tk.Tk | None = None,
) -> RetMode:
    """
    Create a password input window using Tkinter.

    This function generates a window prompting the user to input a password.
    It validates the entered password and performs actions based on the correctness of the input.

    Args:
        password: The correct password string that the user needs to input.
        title: The title of the password window (default is "Password").
        prompt: The prompt text displayed in the window (default is "Please input your Password").
        mask: mask: Must be keyword parameters, Optional character to mask the password input [e.g., '*' or None(for
        no masking, default)].
        error_message: Optional custom error message when the password is incorrect.
                          If not provided, the window will shake to indicate an error.
        topmost: Boolean indicating whether the window should stay on top of others (default is False).
        parent: Parent Tkinter window for modal behavior. If None, creates standalone window.

    Returns:
        Returns RetMode.SUCCESS if the correct password is entered, RetMode.USER_CANCEL if canceled via button,
        or RetMode.WINDOW_CLOSE if closed via window controls.

    Functionality:
    - Displays a Tkinter window with a label, an entry field for password input, and two buttons ("OK" and "Cancel").
    - Validates the entered password against the provided `password`.
    - If the password is correct, the window closes and returns RetMode.SUCCESS.
    - If the password is incorrect:
        - Shakes the window if no custom `error_message` is provided.
        - Displays an error popup with the custom `error_message` if it is provided.
    - Centers the window on the screen using the `center_window` function.
    - Supports optional parameters for customizing the appearance and behavior of the password window.
    """
    # Create window hierarchy
    is_root = parent is None
    window = tk.Toplevel(parent) if parent else tk.Tk()
    if is_root:
        window.title(title)

    # Configure window properties
    window.wm_attributes("-topmost", int(topmost))
    window.geometry("300x150")
    window.resizable(False, False)

    # Status container (using list for mutable closure)
    result = [RetMode.WINDOW_CLOSE]  # Default: closed without verification

    # Password verification handler
    def verify_password() -> None:
        """Validate entered password against reference"""
        if entry.get() == password:
            result[0] = RetMode.SUCCESS
            window.destroy()
        elif error_message:
            messagebox.showerror("Verification Error", error_message, parent=window, master=window)
            entry.select_range(0, tk.END)
        else:
            # Calculate shake parameters dynamically
            shake_window(window, amplitude=min(10, window.winfo_width() // 30))
            entry.select_range(0, tk.END)

    # Cancel operation handler
    def cancel_operation() -> None:
        """Handle explicit cancellation"""
        result[0] = RetMode.USER_CANCEL
        window.destroy()

    # Configure UI components
    ttk.Label(window, text=prompt).pack(pady=(10, 0))
    entry = ttk.Entry(window, show=mask, width=25)
    entry.pack(pady=10, padx=20, fill=tk.X)
    entry.focus_set()

    button_frame = ttk.Frame(window)
    button_frame.pack(pady=10, fill=tk.X, padx=20)

    ttk.Button(button_frame, text="Cancel", command=cancel_operation).pack(side=tk.LEFT)
    ttk.Button(button_frame, text="OK", command=verify_password).pack(side=tk.RIGHT)

    # Configure window close protocol
    window.protocol("WM_DELETE_WINDOW", window.destroy)

    # Bind Enter key to submit
    window.bind("<Return>", lambda e: verify_password())

    # Position window and start event loop
    center_window(window)
    window.transient(parent)
    window.grab_set()
    window.wait_window()

    return result[0]


def setting_password_window(
    title: str = "Password",
    prompt: str = "Please input your Password",
    prompt_again: str = "Please input tour Password again",
    *,
    mask: None | str = None,
    error_message: None | str = None,
    topmost=False,
    check_fun: callable = lambda _: True,
) -> None | str:
    """
    Window to set password.
    Args:
        title: Main window title
        prompt: The prompt text for entering password for the first time
        prompt_again: The prompt text for entering password for the second time
        mask: Must be keyword parameters, Optional character to mask the password input [e.g., '*' or None(for no masking, default)].
        error_message: Optional custom error message when the password is incorrect.
                       If not provided, the window will shake to indicate an error.
        topmost: Boolean indicating whether the window should stay on top of others (default is False).
        check_fun: Functions that check whether they comply with password specifications are the default constant true function

    Returns:
        A string, if the user closes the window (press Cancel or close key, it will return None)
    """
    return_val = None
    widgets_width = []

    window = tk.Tk()
    window.wm_attributes("-topmost", topmost)
    window.title(title)
    tk.Label(window, text=prompt).place(x=10, y=2)
    entry1 = ttk.Entry(window, show=mask, width=40)
    entry1.place(x=10, y=30)
    widgets_width.append(entry1.winfo_reqwidth())
    tk.Label(window, text=prompt_again).place(x=10, y=60)
    entry2 = ttk.Entry(window, show=mask, width=40)
    entry2.place(x=10, y=90)
    widgets_width.append(entry2.winfo_reqwidth())

    def ok():
        nonlocal entry1, entry2, return_val, window, error_message
        if not entry1.get() == entry2.get() or not check_fun(entry1.get()):
            if not error_message:
                shake_window(window)
            else:
                messagebox.showerror(title=" Password Error", message=error_message, parent=window, master=window)
            return
        return_val = entry1.get()
        window.destroy()

    tmp = ttk.Button(window, text="Cancel", command=lambda: window.destroy())
    tmp.place(x=105, y=120)
    widgets_width.append(tmp.winfo_reqwidth())
    tmp = ttk.Button(window, text="OK", command=ok)
    tmp.place(x=205, y=120)
    widgets_width.append(tmp.winfo_reqwidth())
    window_width = max(widgets_width)
    window.geometry(f"{window_width + 20}x150")
    center_window(window)
    window.wait_window()
    return return_val


def window_sleep(windows: List[tk.Wm] | tk.Wm, wait_time: Seconds):
    """
    Keep windows updated while the program sleeps

    Args:
        windows: Windows that need to be kept updated
        wait_time: Time to sleep(Seconds)
    """
    start_time = time.time()
    if isinstance(windows, tk.Wm):
        windows = [windows]
    while time.time() - start_time < wait_time:
        for window in windows:
            window.update()
        time.sleep(0.01)


class Rect:
    """
    A Rect class for tkinter

    You can construct a Rect object in the following ways:
    - `Rect(x, y, width, height)`: Creates a rectangle with its top-left corner at (x, y), a width of `width`, and a height of `height`.
    - `Rect((x, y), (width, height))`: Creates a rectangle with its top-left corner at (x, y), a width of `width`, and a height of `height`.
    - `Rect(rect_object)`: Creates a rectangle with the same position and dimensions as the given `rect` object.
    - `Rect(tk.Widget)`: Generates a Rect object for the specified Widget.


    Attributes:
        x, y(left, top): The x, y position of top and left side
        w, h(width, height): The width/height of the rect
        right: The x position of the right side
        bottom: The y position of the bottom side
        centerx, centery : The x/y position of the rect center
        center = (centerx, centery)
        size = (w, h)
        topleft = (left, top)
        topright = (right, top)
        bottomright = (right, bottom)
        bottomleft = (left, bottom)
        midleft = (left, centery)
        midright = (right, centery)
        midtop = (centerx, top)
        midbottom = (centerx, bottom)

    Examples:
        >>> r = Rect(10, 20, 30, 40)
        >>> r.x, r.y, r.w, r.h
        (10, 20, 20, 20)
        >>> r.left, r.top, r.right, r.bottom
        (10, 20, 30, 40)
        >>> r.width = 30
        >>> r.height = 30
        >>> r.size
        (30, 30)
        >>> r.topleft = (5, 10)
        >>> r.bottomright
        (35, 40)
        >>> r.center = (20, 30)
        >>> r.topleft
        (5, 15)
        >>> r2 = r.copy()
        >>> r2.move(10, 10) #doctest: +ELLIPSIS
        <Rect(10, 10, 40, 40) at ...>
        >>> r2.move_ip(15, 25)
        >>> r2.topleft
        (15, 25)
    """

    def __init__(self, *args):
        if len(args) == 1 and isinstance(args[0], Rect):
            rect = args[0]
            self.x, self.y, self.w, self.h = rect.x, rect.y, rect.w, rect.h
        elif len(args) == 4:
            self.x, self.y, self.w, self.h = args
        elif len(args) == 2 and isinstance(args[0], Iterable) and isinstance(args[1], Iterable):
            self.x, self.y = args[0]
            self.w, self.h = args[1]
        elif len(args) == 1 and isinstance(args[0], tk.Widget):
            widget = args[0]
            self.x, self.y = widget.winfo_x(), widget.winfo_y()
            self.w, self.h = widget.winfo_reqwidth(), widget.winfo_reqheight()
        else:
            raise TypeError("Invalid arguments for Rect")

    @property
    def width(self):
        return self.w

    @width.setter
    def width(self, value):
        self.w = value

    @property
    def height(self):
        return self.h

    @height.setter
    def height(self, value):
        self.h = value

    @property
    def size(self):
        return self.w, self.h

    @size.setter
    def size(self, value):
        self.w, self.h = value[0], value[1]

    @property
    def left(self):
        return self.x

    @left.setter
    def left(self, value):
        self.x = value

    @property
    def top(self):
        return self.y

    @top.setter
    def top(self, value):
        self.y = value

    @property
    def right(self):
        return self.x + self.w

    @right.setter
    def right(self, value):
        self.x = value - self.w

    @property
    def bottom(self):
        return self.y + self.h

    @bottom.setter
    def bottom(self, value):
        self.y = value - self.h

    @property
    def centerx(self):
        return self.x + self.w // 2

    @centerx.setter
    def centerx(self, value):
        self.x = value - self.w // 2

    @property
    def centery(self):
        return self.y + self.h // 2

    @centery.setter
    def centery(self, value):
        self.y = value - self.h // 2

    @property
    def center(self):
        return self.centerx, self.centery

    @center.setter
    def center(self, value):
        cx, cy = value
        self.centerx = cx
        self.centery = cy

    @property
    def topleft(self):
        return self.left, self.top

    @topleft.setter
    def topleft(self, value):
        self.left, self.top = value[0], value[1]

    @property
    def topright(self):
        return self.right, self.top

    @topright.setter
    def topright(self, value):
        self.right, self.top = value[0], value[1]

    @property
    def bottomleft(self):
        return self.left, self.bottom

    @bottomleft.setter
    def bottomleft(self, value):
        self.left, self.bottom = value[0], value[1]

    @property
    def bottomright(self):
        return self.right, self.bottom

    @bottomright.setter
    def bottomright(self, value):
        self.right, self.bottom = value[0], value[1]

    @property
    def midleft(self):
        return self.left, self.centery

    @midleft.setter
    def midleft(self, value):
        self.left, self.centery = value[0], value[1]

    @property
    def midright(self):
        return self.right, self.centery

    @midright.setter
    def midright(self, value):
        self.right, self.centery = value[0], value[1]

    @property
    def midtop(self):
        return self.centerx, self.top

    @midtop.setter
    def midtop(self, value):
        self.centerx, self.top = value[0], value[1]

    @property
    def midbottom(self):
        return self.centerx, self.bottom

    @midbottom.setter
    def midbottom(self, value):
        self.centerx, self.bottom = value[0], value[1]

    def move(self, x: int, y: int) -> "Rect":
        """Move the rect and return the rect
        >>> r = Rect(10, 20, 30, 40)
        >>> r2 = r.move(5, 5)
        >>> r2.topleft
        (5, 5)
        >>> r2.bottomright
        (25, 25)
        """
        return Rect(x, y, x + self.w, y + self.h)

    def move_ip(self, x: int, y: int) -> None:
        """Move the rect in situ
        >>> r = Rect(10, 20, 30, 40)
        >>> r.move_ip(5, 5)
        >>> r.topleft
        (5, 5)
        """
        self.x, self.y = x, y

    def copy(self) -> "Rect":
        """Copy the self Rect
        >>> r = Rect(10, 20, 30, 40)
        >>> r2 = r.copy()
        >>> r2.topleft == r.topleft
        True
        >>> r2.bottomright == r.bottomright
        True
        """
        return Rect(self.x, self.y, self.x + self.w, self.y + self.h)

    def pack_widget(self, widget: tk.Widget) -> None:
        """
        Put the widget in the corresponding position on the Rect
        :param widget: The tk widget to be placed
        """
        widget.place(x=self.x, y=self.y)

    def __repr__(self):
        return f"<Rect({self.x}, {self.y}, {self.x + self.w}, {self.y + self.h}) at {hex(id(self))}>"

    def __eq__(self, other):
        if not isinstance(other, Rect):
            return False
        return self.x == other.x and self.y == other.y and self.w == other.w and self.h == other.h

    def __hash__(self):
        return hash((self.x, self.y, self.w, self.h))

    def __add__(self, other):
        if not isinstance(other, Rect):
            return NotImplemented
        return Rect(self.x + other.x, self.y + other.y, self.x + self.w + other.w, self.y + self.h + other.h)

    def __sub__(self, other):
        if not isinstance(other, Rect):
            return NotImplemented
        return Rect(self.x - other.x, self.y - other.y, self.x + self.w - other.w, self.y + self.h - other.h)

    def __mul__(self, scalar):
        return Rect(self.x * scalar, self.y * scalar, (self.x + self.w) * scalar, (self.y + self.h) * scalar)

    def __truediv__(self, scalar):
        return Rect(self.x / scalar, self.y / scalar, (self.x + self.w) / scalar, (self.y + self.h) / scalar)

    def __iadd__(self, other):
        if not isinstance(other, Rect):
            return NotImplemented
        self.x += other.x
        self.y += other.y
        self.w += other.w
        self.h += other.h
        return self

    def __isub__(self, other):
        if not isinstance(other, Rect):
            return NotImplemented
        self.x -= other.x
        self.y -= other.y
        self.w -= other.w
        self.h -= other.h
        return self

    def __imul__(self, scalar):
        self.x *= scalar
        self.y *= scalar
        self.w *= scalar
        self.h *= scalar
        return self

    def __itruediv__(self, scalar):
        self.x /= scalar
        self.y /= scalar
        self.w /= scalar
        self.h /= scalar
        return self


def pix_to_fontsize(pix: int, font: tuple = ("KaiTi", 12)) -> tuple:
    """
    Convert pixels to font size

    Args:
        pix: The number of pixes to be converted
        font: The font to be used for conversion

    Returns:
        A tuple of two integers representing the font size

    Note: This function creates a temporary Tk window

    Examples:
        >>> pix_to_fontsize(100)
        (54, 54)
    """
    root = tk.Tk()
    label = tk.Label(root, height=1, width=1, font=font)
    label.pack()
    root.update()
    width, height = label.winfo_reqwidth(), label.winfo_reqheight()
    root.destroy()
    return int(pix * (12 / height)), int(pix * (12 / height))


def fontsize_to_pix(num: int, font: tuple = ("KaiTi", 12)) -> tuple:
    """
    Convert font size to pixels

    Args:
        num: The number of font size to be converted
        font: The font to be used for conversion

    Returns:
        A tuple of two integers representing the pixels

    Note: This function creates a temporary Tk window
    Examples:
        >>> fontsize_to_pix(12)
        (14, 22)
    """
    root = tk.Tk()
    label = tk.Label(root, height=1, width=1, font=font)
    label.pack()
    root.update()
    width, height = label.winfo_reqwidth(), label.winfo_reqheight()
    root.destroy()
    return width * num // 12, height * num // 12


def show_message(title: str, message: str, box_type: MessageboxMode = MessageboxMode.INFO) -> str:
    """
    Show a tkinter messagebox

    Args:
        title: The title of the messagebox
        message: The message to be displayed
        box_type: The type of messagebox to be displayed

    Returns:
        The result of the messagebox
    """
    if box_type == MessageboxMode.INFO:
        return messagebox.showinfo(title, message)
    elif box_type == MessageboxMode.WARNING:
        return messagebox.showwarning(title, message)
    elif box_type == MessageboxMode.ERROR:
        return messagebox.showerror(title, message)
    elif box_type == MessageboxMode.QUESTION:
        return messagebox.askquestion(title, message)
    elif box_type == MessageboxMode.YESNO:
        return messagebox.askyesno(title, message)
    elif box_type == MessageboxMode.YESNOCANCEL:
        return messagebox.askyesnocancel(title, message)
    elif box_type == MessageboxMode.RETRYCANCEL:
        return messagebox.askretrycancel(title, message)
    else:
        raise ValueError(f"Invalid box_type: {box_type}")


def custom_messagebox(
    title: Optional[str] = None,
    message: Optional[str] = None,
    icon: Optional[str] = None,
    _type: Optional = None,
    **options,
) -> str:
    """
    Custom message box (advanced usage)

    Args:
        title: The title of the messagebox
        message: The message to be displayed
        icon: The icon to be displayed
        _type: The type of messagebox to be displayed
        **options: Additional options for the messagebox

    Returns:
        The result of the messagebox
    """
    return messagebox._show(title, message, icon, _type, **options)


if __name__ == "__main__":
    import doctest

    print("tkhelper Doctest:")
    doctest.testmod()
    print("\n\n\n")
    input_string = "Please input you want to test Mod:\n\t1.window_sleep();\n\t2.shake_window();\n\t3.center_window();\n\t4.password_window();\n\t5.setting_password_window();\n> "
    mode = str(input(input_string))
    root = tk.Tk()
    root.geometry("300x300")
    try:
        print("=" * 20)
        print("tkhelperGUI Test Mod:")
        print("=" * 20)
        if "1" in mode:  # window_sleep
            print("tkhelper.window_sleep")
            print("\tSleep One Window")
            t = time.time()
            window_sleep([root], 5)
            print(f"\t\tTime Cost: {time.time() - t}s")
            print("\tSleep Two Window")
            toplevel = tk.Toplevel(root)
            t = time.time()
            window_sleep([root, toplevel], 5)
            print(f"\tTime Cost: {time.time() - t}s")
            toplevel.destroy()
            del toplevel
            print("-" * 20)
        if "2" in mode:  # shake_window
            print("tkhelper.shake_window()")
            print("\tDefault Mode:")
            shake_window(root)
            time.sleep(1)
            print("\tTest Direction(horizontal):")
            shake_window(root, dire="horizontal")
            time.sleep(1)
            print("\tTest Jitter Time(5s):")
            t = time.time()
            shake_window(root, jitter_time=5)
            print(f"\t\tTime Cost: {time.time() - t}s")
            time.sleep(1)
            print("\tTest Jitter Count(80s):")
            shake_window(root, jitter_count=80)
            time.sleep(1)
            print("\tTest Amplitude(10px)")
            shake_window(root, amplitude=10)
            time.sleep(1)
            print("shake_window Test Done.")
            print("-" * 20)
        if "3" in mode:  # center_window
            print("tkhelper.center_window:")
            print("\tReset the form position (10, 10):")
            root.geometry("+10+10")
            print("\tCetner all:")
            center_window(root, dire="All")
            print("\tReset the form position (10, 10):")
            root.geometry("+10+10")
            print("\tCenter Vertical:")
            center_window(root, dire="vertical")
            print("\tReset the form position (10, 10):")
            root.geometry("+10+10")
            print("\tCenter Horizontal:")
            center_window(root, dire="horizontal")
            print("center_window() Test Done.")
            print("-" * 20)
        if "4" in mode:  # password_window
            password = "541881452527415157"
            print("tkhelper.password_window():")
            print("\tTest no mask, no error_message and no topmost")
            ret = password_window(password, "Password Window", "Please input your password", topmost=False)
            print(f"\t\tPassword Window Return: {ret}")
            print("\tTest has mask, has error_message and topmost")
            ret = password_window(
                password,
                "Password Window",
                "Please input your password",
                mask="*",
                error_message="Your Password Wrong! Please try again",
                topmost=True,
            )
            print(f"\t\tPassword Window Return: {ret}")
            print("password_window() Test Done.")
            print("-" * 20)
        if "5" in mode:  # setting_password_window
            print("tkhelper.setting_password_window():")
            print("\tNo Mask, No topmost, No ErrorMessage, Can only contain numbers:")
            user_password = setting_password_window(
                "Setting Password",
                "Please input Password",
                "Please input your Password Again",
                check_fun=lambda ps: ps.isdigit(),
            )
            print(f"\t\tSetting Password Window Return: {user_password}")
            print("\tHas Mask, Has topmost, Has ErrorMessage, Can only contain numbers:")
            user_password = setting_password_window(
                "Setting Password",
                "Please input Password",
                "Please input your Password Again",
                check_fun=lambda ps: ps.isdigit(),
                mask="*",
                topmost=True,
                error_message="Wrong! Your password Can only contain NUMBERS!",
            )
            print(f"\t\tSetting Password Window Return: {user_password}")
            print("setting_password_window() Test Done.")
            print("-" * 20)
        print("=" * 20)
    except Exception as e:
        raise
    else:
        print("." * len(mode))
        print("Test Success!")
    finally:
        root.destroy()
