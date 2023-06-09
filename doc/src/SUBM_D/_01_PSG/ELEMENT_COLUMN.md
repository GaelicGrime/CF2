

  - AddRow = add_row\(
    - self, 
    - *args\)
  - Layout = layout\(
    - self, 
    - rows\)
  - Update = update\(
    - self, 
    - visible=None\)
  - \_\_init\_\_\(
    - self, 
    - layout, 
    - background_color=None, 
    - size=\(None, None\), 
    - s=\(None, None\), 
    - pad=None, 
    - p=None, 
    - scrollable=False, 
    - vertical_scroll_only=False, 
    - right_click_menu=None, 
    - key=None, 
    - k=None, 
    - visible=True, 
    - justification=None, 
    - element_justification=None, 
    - vertical_alignment=None, 
    - grab=None, 
    - expand_x=None, 
    - expand_y=None, 
    - metadata=None\)
      - :param layout:                Layout that will be shown in the Column container
      - :type layout:                 List\[List\[Element\]\]
      - :param background_color:      color of background of entire Column
      - :type background_color:       \(str\)
      - :param size:                  \(width, height\) size in pixels \(doesn't work quite right, sometimes only 1 dimension is set by tkinter. Use a Sizer Element to help set sizes
      - :type size:                   \(int | None, int | None\)
      - :param s:                     Same as size parameter.  It's an alias. If EITHER of them are set, then the one that's set will be used. If BOTH are set, size will be used
      - :type s:                      \(int | None, int | None\)
      - :param pad:                   Amount of padding to put around element in pixels \(left/right, top/bottom\) or \(\(left, right\), \(top, bottom\)\) or an int. If an int, then it's converted into a tuple \(int, int\)
      - :type pad:                    \(int, int\) or \(\(int, int\),\(int,int\)\) or \(int,\(int,int\)\) or  \(\(int, int\),int\) | int
      - :param p:                     Same as pad parameter.  It's an alias. If EITHER of them are set, then the one that's set will be used. If BOTH are set, pad will be used
      - :type p:                      \(int, int\) or \(\(int, int\),\(int,int\)\) or \(int,\(int,int\)\) or  \(\(int, int\),int\) | int
      - :param scrollable:            if True then scrollbars will be added to the column
      - :type scrollable:             \(bool\)
      - :param vertical_scroll_only:  if Truen then no horizontal scrollbar will be shown
      - :type vertical_scroll_only:   \(bool\)
      - :param right_click_menu:      A list of lists of Menu items to show when this element is right clicked. See user docs for exact format.
      - :type right_click_menu:       List\[List\[ List\[str\] | str \]\]
      - :param key:                   Value that uniquely identifies this element from all other elements. Used when Finding an element or in return values. Must be unique to the window
      - :type key:                    str | int | tuple | object
      - :param k:                     Same as the Key. You can use either k or key. Which ever is set will be used.
      - :type k:                      str | int | tuple | object
      - :param visible:               set visibility state of the element
      - :type visible:                \(bool\)
      - :param justification:         set justification for the Column itself. Note entire row containing the Column will be affected
      - :type justification:          \(str\)
      - :param element_justification: All elements inside the Column will have this justification 'left', 'right', 'center' are valid values
      - :type element_justification:  \(str\)
      - :param vertical_alignment:    Place the column at the 'top', 'center', 'bottom' of the row \(can also use t,c,r\). Defaults to no setting \(tkinter decides\)
      - :type vertical_alignment:     \(str\)
      - :param grab:                  If True can grab this element and move the window around. Default is False
      - :type grab:                   \(bool\)
      - :param expand_x:              If True the column will automatically expand in the X direction to fill available space
      - :type expand_x:               \(bool\)
      - :param expand_y:              If True the column will automatically expand in the Y direction to fill available space
      - :type expand_y:               \(bool\)
      - :param metadata:              User metadata that can be set to ANYTHING
      - :type metadata:               \(Any\)
  - add_row\(
    - self, 
    - *args\)
      - Not recommended user call.  Used to add rows of Elements to the Column Element.
        - :param *args: The list of elements for this row
        - :type *args:  List\[Element\]
  - contents_changed\(
    - self\)
      - When a scrollable column has part of its layout changed by making elements visible or invisible or the layout is extended for the Column, then this method needs to be called so that the new scroll area is computed to match the new contents.
  - layout\(
    - self, 
    - rows\)
      - Can use like the Window.Layout method, but it's better to use the layout parameter when creating
        - :param rows: The rows of Elements
        - :type rows:  List\[List\[Element\]\]
        - :return:     Used for chaining
        - :rtype:      \(Column\)
  - update\(
    - self, 
    - visible=None\)
      - Changes some of the settings for the Column Element. Must call `Window.Read` or `Window.Finalize` prior changes will not be visible in your window until you call window.read or window.refresh.
      - If you change visibility, your element may MOVE. If you want it to remain stationary, use the "layout helper" function "pin" to ensure your element is "pinned" to that location in your layout so that it returns there when made visible.
      - :param visible: control visibility of element
      - :type visible:  \(bool\)
