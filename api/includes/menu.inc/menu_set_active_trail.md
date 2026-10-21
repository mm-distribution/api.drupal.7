# menu_set_active_trail()

- **Type:** Function
- **File:** [`includes/menu.inc`](_file.md), lines 2391–2461 · [local source](../../../source/includes/menu.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc#L2391-L2461)
- **Topics:** [menu](../../topics/menu.md)

## Signature

```php
function menu_set_active_trail($new_trail = NULL)
```

## Documentation

```text
Sets the active trail (path to the menu tree root) of the current page.

Any trail set by this function will only be used for functionality that calls
menu_get_active_trail(). Drupal core only uses trails set here for
breadcrumbs and the page title and not for menu trees or page content.
Additionally, breadcrumbs set by drupal_set_breadcrumb() will override any
trail set here.

To affect the trail used by menu trees, use menu_tree_set_path(). To affect
the page content, use menu_set_active_item() instead.

@param $new_trail
  Menu trail to set; the value is saved in a static variable and can be
  retrieved by menu_get_active_trail(). The format of this array should be
  the same as the return value of menu_get_active_trail().

@return
  The active trail. See menu_get_active_trail() for details.
```

## Code

```php
function menu_set_active_trail($new_trail = NULL) {
  $trail = &drupal_static(__FUNCTION__);

  if (isset($new_trail)) {
    $trail = $new_trail;
  }
  elseif (!isset($trail)) {
    $trail = array();
    $trail[] = array(
      'title' => t('Home'),
      'href' => '<front>',
      'link_path' => '',
      'localized_options' => array(),
      'type' => 0,
    );

    // Try to retrieve a menu link corresponding to the current path. If more
    // than one exists, the link from the most preferred menu is returned.
    $preferred_link = menu_link_get_preferred();
    $current_item = menu_get_item();

    // There is a link for the current path.
    if ($preferred_link) {
      // Pass TRUE for $only_active_trail to make menu_tree_page_data() build
      // a stripped down menu tree containing the active trail only, in case
      // the given menu has not been built in this request yet.
      $tree = menu_tree_page_data($preferred_link['menu_name'], NULL, TRUE);
      $curr = current($tree);
      next($tree);
    }
    // There is no link for the current path.
    else {
      $preferred_link = $current_item;
      $curr = FALSE;
    }

    while ($curr) {
      $link = $curr['link'];
      if ($link['in_active_trail']) {
        // Add the link to the trail, unless it links to its parent.
        if (!($link['type'] & MENU_LINKS_TO_PARENT)) {
          // The menu tree for the active trail may contain additional links
          // that have not been translated yet, since they contain dynamic
          // argument placeholders (%). Such links are not contained in regular
          // menu trees, and have only been loaded for the additional
          // translation that happens here, so as to be able to display them in
          // the breadcrumb for the current page.
          // @see _menu_tree_check_access()
          // @see _menu_link_translate()
          if (strpos($link['href'], '%') !== FALSE) {
            _menu_link_translate($link, TRUE);
          }
          if ($link['access']) {
            $trail[] = $link;
          }
        }
        $tree = $curr['below'] ? $curr['below'] : array();
      }
      $curr = current($tree);
      next($tree);
    }
    // Make sure the current page is in the trail to build the page title, by
    // appending either the preferred link or the menu router item for the
    // current page. Exclude it if we are on the front page.
    $last = end($trail);
    if ($preferred_link && $last['href'] != $preferred_link['href'] && !drupal_is_front_page()) {
      $trail[] = $preferred_link;
    }
  }
  return $trail;
}
```

---
_Drupal 7.103 · [includes/menu.inc](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
