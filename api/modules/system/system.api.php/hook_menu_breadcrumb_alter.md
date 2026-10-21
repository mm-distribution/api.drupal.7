# hook_menu_breadcrumb_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 1519–1530 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L1519-L1530)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_menu_breadcrumb_alter(&$active_trail, $item)
```

## Documentation

```text
Alter links in the active trail before it is rendered as the breadcrumb.

This hook is invoked by menu_get_active_breadcrumb() and allows alteration
of the breadcrumb links for the current page, which may be preferred instead
of setting a custom breadcrumb via drupal_set_breadcrumb().

Implementations should take into account that menu_get_active_breadcrumb()
subsequently performs the following adjustments to the active trail *after*
this hook has been invoked:
- The last link in $active_trail is removed, if its 'href' is identical to
  the 'href' of $item. This happens, because the breadcrumb normally does
  not contain a link to the current page.
- The (second to) last link in $active_trail is removed, if the current $item
  is a MENU_DEFAULT_LOCAL_TASK. This happens in order to do not show a link
  to the current page, when being on the path for the default local task;
  e.g. when being on the path node/%/view, the breadcrumb should not contain
  a link to node/%.

Each link in the active trail must contain:
- title: The localized title of the link.
- href: The system path to link to.
- localized_options: An array of options to pass to url().

@param $active_trail
  An array containing breadcrumb links for the current page.
@param $item
  The menu router item of the current page.

@see drupal_set_breadcrumb()
@see menu_get_active_breadcrumb()
@see menu_get_active_trail()
@see menu_set_active_trail()
```

## Code

```php
function hook_menu_breadcrumb_alter(&$active_trail, $item) {
  // Always display a link to the current page by duplicating the last link in
  // the active trail. This means that menu_get_active_breadcrumb() will remove
  // the last link (for the current page), but since it is added once more here,
  // it will appear.
  if (!drupal_is_front_page()) {
    $end = end($active_trail);
    if ($item['href'] == $end['href']) {
      $active_trail[] = $end;
    }
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_menu_breadcrumb_alter()".

_None found._

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
