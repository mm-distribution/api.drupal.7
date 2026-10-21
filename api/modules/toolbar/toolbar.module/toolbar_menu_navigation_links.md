# toolbar_menu_navigation_links()

- **Type:** Function
- **File:** [`modules/toolbar/toolbar.module`](_file.md), lines 315–343 · [local source](../../../../source/modules/toolbar/toolbar.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/toolbar/toolbar.module#L315-L343)
- **Module/theme:** toolbar

## Signature

```php
function toolbar_menu_navigation_links($tree)
```

## Documentation

```text
Generates a links array from a menu tree array.

Based on menu_navigation_links(). Adds path based IDs and icon placeholders
to the links.

@return
  An array of links as defined above.
```

## Code

```php
function toolbar_menu_navigation_links($tree) {
  $links = array();
  foreach ($tree as $item) {
    if (!$item['link']['hidden'] && $item['link']['access']) {
      // Make sure we have a path specific ID in place, so we can attach icons
      // and behaviors to the items.
      $id = str_replace(array('/', '<', '>'), array('-', '', ''), $item['link']['href']);

      $link = $item['link']['localized_options'];
      $link['href'] = $item['link']['href'];
      // Add icon placeholder.
      $link['title'] = '<span class="icon"></span>' . check_plain($item['link']['title']);
      // Add admin link ID.
      $link['attributes'] = array('id' => 'toolbar-link-' . $id);
      if (!empty($item['link']['description'])) {
        $link['title'] .= ' <span class="element-invisible">(' . $item['link']['description'] . ')</span>';
        $link['attributes']['title'] = $item['link']['description'];
      }
      $link['html'] = TRUE;

      $class = ' path-' . $id;
      if (toolbar_in_active_trail($item['link']['href'])) {
        $class .= ' active-trail';
      }
      $links['menu-' . $item['link']['mlid'] . $class] = $link;
    }
  }
  return $links;
}
```

---
_Drupal 7.103 · [modules/toolbar/toolbar.module](https://github.com/drupal/drupal/blob/7.103/modules/toolbar/toolbar.module) · Licensed GPL-2.0-or-later (see LICENSE)._
