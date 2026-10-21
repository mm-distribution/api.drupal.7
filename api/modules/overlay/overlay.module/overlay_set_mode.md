# overlay_set_mode()

- **Type:** Function
- **File:** [`modules/overlay/overlay.module`](_file.md), lines 639–666 · [local source](../../../../source/modules/overlay/overlay.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.module#L639-L666)
- **Module/theme:** overlay
- **Topics:** overlay_api

## Signature

```php
function overlay_set_mode($mode = NULL)
```

## Documentation

```text
Sets the overlay mode and adds proper JavaScript and styles to the page.

Note that since setting the overlay mode triggers a variety of behaviors
(including hooks being invoked), it can only be done once per page request.
Therefore, the first call to this function which passes along a value of the
$mode parameter controls the overlay mode that will be used.

@param $mode
  To set the mode, pass in one of the following values:
  - 'parent': This is used in the context of a parent window (a regular
    browser window). If set, JavaScript is added so that administrative
    links in the parent window will open in an overlay.
  - 'child': This is used in the context of the child overlay window (the
    page actually appearing within the overlay iframe). If set, JavaScript
    and CSS are added so that Drupal behaves nicely from within the overlay.
  - 'none': This is used to avoid adding any overlay-related code to the
    page at all. Modules can set this to explicitly prevent the overlay from
    being used. For example, since the overlay module itself sets the mode
    to 'parent' or 'child' in overlay_init() when certain conditions are
    met, other modules which want to override that behavior can do so by
    setting the mode to 'none' earlier in the page request - e.g., in their
    own hook_init() implementations, if they have a lower weight.
  This parameter is optional, and if omitted, the current mode will be
  returned with no action taken.

@return
  The current mode, if any has been set, or NULL if no mode has been set.

@ingroup overlay_api
@see overlay_init()
```

## Code

```php
function overlay_set_mode($mode = NULL) {
  global $base_path;
  $overlay_mode = &drupal_static(__FUNCTION__);

  // Make sure external resources are not included more than once. Also return
  // the current mode, if no mode was specified.
  if (isset($overlay_mode) || !isset($mode)) {
    return $overlay_mode;
  }
  $overlay_mode = $mode;

  switch ($overlay_mode) {
    case 'parent':
      drupal_add_library('overlay', 'parent');

      // Allow modules to act upon overlay events.
      module_invoke_all('overlay_parent_initialize');
      break;

    case 'child':
      drupal_add_library('overlay', 'child');

      // Allow modules to act upon overlay events.
      module_invoke_all('overlay_child_initialize');
      break;
  }
  return $overlay_mode;
}
```

---
_Drupal 7.103 · [modules/overlay/overlay.module](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.module) · Licensed GPL-2.0-or-later (see LICENSE)._
