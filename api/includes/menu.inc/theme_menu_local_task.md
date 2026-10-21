# theme_menu_local_task()

- **Type:** Function
- **File:** [`includes/menu.inc`](_file.md), lines 1672–1690 · [local source](../../../source/includes/menu.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc#L1672-L1690)
- **Topics:** [menu](../../topics/menu.md), [themeable](../../topics/themeable.md)

## Signature

```php
function theme_menu_local_task($variables)
```

## Documentation

```text
Returns HTML for a single local task link.

@param $variables
  An associative array containing:
  - element: A render element containing:
    - #link: A menu link array with 'title', 'href', and 'localized_options'
      keys.
    - #active: A boolean indicating whether the local task is active.

@ingroup themeable
```

## Code

```php
function theme_menu_local_task($variables) {
  $link = $variables['element']['#link'];
  $link_text = $link['title'];

  if (!empty($variables['element']['#active'])) {
    // Add text to indicate active tab for non-visual users.
    $active = '<span class="element-invisible">' . t('(active tab)') . '</span>';

    // If the link does not contain HTML already, check_plain() it now.
    // After we set 'html'=TRUE the link will not be sanitized by l().
    if (empty($link['localized_options']['html'])) {
      $link['title'] = check_plain($link['title']);
    }
    $link['localized_options']['html'] = TRUE;
    $link_text = t('!local-task-title!active', array('!local-task-title' => $link['title'], '!active' => $active));
  }

  return '<li' . (!empty($variables['element']['#active']) ? ' class="active"' : '') . '>' . l($link_text, $link['href'], $link['localized_options']) . "</li>\n";
}
```

---
_Drupal 7.103 · [includes/menu.inc](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
