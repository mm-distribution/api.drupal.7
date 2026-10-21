# _menu_item_localize()

- **Type:** Function
- **File:** [`includes/menu.inc`](_file.md), lines 679–732 · [local source](../../../source/includes/menu.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc#L679-L732)
- **Topics:** [menu](../../topics/menu.md)

## Signature

```php
function _menu_item_localize(&$item, $map, $link_translate = FALSE)
```

## Documentation

```text
Localizes the router item title using t() or another callback.

Translate the title and description to allow storage of English title
strings in the database, yet display of them in the language required
by the current user.

@param $item
  A menu router item or a menu link item.
@param $map
  The path as an array with objects already replaced. E.g., for path
  node/123 $map would be array('node', $node) where $node is the node
  object for node 123.
@param $link_translate
  TRUE if we are translating a menu link item; FALSE if we are
  translating a menu router item.

@return
  No return value.
  $item['title'] is localized according to $item['title_callback'].
  If an item's callback is check_plain(), $item['options']['html'] becomes
  TRUE.
  $item['description'] is translated using t().
  When doing link translation and the $item['options']['attributes']['title']
  (link title attribute) matches the description, it is translated as well.
```

## Code

```php
function _menu_item_localize(&$item, $map, $link_translate = FALSE) {
  $callback = $item['title_callback'];
  $item['localized_options'] = $item['options'];
  // All 'class' attributes are assumed to be an array during rendering, but
  // links stored in the database may use an old string value.
  // @todo In order to remove this code we need to implement a database update
  //   including unserializing all existing link options and running this code
  //   on them, as well as adding validation to menu_link_save().
  if (isset($item['options']['attributes']['class']) && is_string($item['options']['attributes']['class'])) {
    $item['localized_options']['attributes']['class'] = explode(' ', $item['options']['attributes']['class']);
  }
  // If we are translating the title of a menu link, and its title is the same
  // as the corresponding router item, then we can use the title information
  // from the router. If it's customized, then we need to use the link title
  // itself; can't localize.
  // If we are translating a router item (tabs, page, breadcrumb), then we
  // can always use the information from the router item.
  if (!$link_translate || ($item['title'] == $item['link_title'])) {
    // t() is a special case. Since it is used very close to all the time,
    // we handle it directly instead of using indirect, slower methods.
    if ($callback == 't') {
      if (empty($item['title_arguments'])) {
        $item['title'] = t($item['title']);
      }
      else {
        $item['title'] = t($item['title'], menu_unserialize($item['title_arguments'], $map));
      }
    }
    elseif ($callback && function_exists($callback)) {
      if (empty($item['title_arguments'])) {
        $item['title'] = $callback($item['title']);
      }
      else {
        $item['title'] = call_user_func_array($callback, menu_unserialize($item['title_arguments'], $map));
      }
      // Avoid calling check_plain again on l() function.
      if ($callback == 'check_plain') {
        $item['localized_options']['html'] = TRUE;
      }
    }
  }
  elseif ($link_translate) {
    $item['title'] = $item['link_title'];
  }

  // Translate description, see the motivation above.
  if (!empty($item['description'])) {
    $original_description = $item['description'];
    $item['description'] = t($item['description']);
    if ($link_translate && isset($item['options']['attributes']['title']) && $item['options']['attributes']['title'] == $original_description) {
      $item['localized_options']['attributes']['title'] = $item['description'];
    }
  }
}
```

---
_Drupal 7.103 · [includes/menu.inc](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
