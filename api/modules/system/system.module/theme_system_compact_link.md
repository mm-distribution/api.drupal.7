# theme_system_compact_link()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 3478–3489 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L3478-L3489)
- **Module/theme:** system
- **Topics:** [themeable](../../../topics/themeable.md)

## Signature

```php
function theme_system_compact_link()
```

## Documentation

```text
Returns HTML for a link to show or hide inline help descriptions.

@ingroup themeable
```

## Code

```php
function theme_system_compact_link() {
  $output = '<div class="compact-link">';
  if (system_admin_compact_mode()) {
    $output .= l(t('Show descriptions'), 'admin/compact/off', array('attributes' => array('title' => t('Expand layout to include descriptions.')), 'query' => drupal_get_destination()));
  }
  else {
    $output .= l(t('Hide descriptions'), 'admin/compact/on', array('attributes' => array('title' => t('Compress layout by hiding descriptions.')), 'query' => drupal_get_destination()));
  }
  $output .= '</div>';

  return $output;
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
