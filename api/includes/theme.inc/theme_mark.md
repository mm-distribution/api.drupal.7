# theme_mark()

- **Type:** Function
- **File:** [`includes/theme.inc`](_file.md), lines 2186–2197 · [local source](../../../source/includes/theme.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc#L2186-L2197)
- **Topics:** [themeable](../../topics/themeable.md)

## Signature

```php
function theme_mark($variables)
```

## Documentation

```text
Returns HTML for a marker for new or updated content.

@param $variables
  An associative array containing:
  - type: Number representing the marker type to display. See MARK_NEW,
    MARK_UPDATED, MARK_READ.
```

## Code

```php
function theme_mark($variables) {
  $type = $variables['type'];
  global $user;
  if ($user->uid) {
    if ($type == MARK_NEW) {
      return ' <span class="marker">' . t('new') . '</span>';
    }
    elseif ($type == MARK_UPDATED) {
      return ' <span class="marker">' . t('updated') . '</span>';
    }
  }
}
```

---
_Drupal 7.103 · [includes/theme.inc](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
