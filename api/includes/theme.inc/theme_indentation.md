# theme_indentation()

- **Type:** Function
- **File:** [`includes/theme.inc`](_file.md), lines 2410–2416 · [local source](../../../source/includes/theme.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc#L2410-L2416)
- **Topics:** [themeable](../../topics/themeable.md)

## Signature

```php
function theme_indentation($variables)
```

## Documentation

```text
Returns HTML for an indentation div; used for drag and drop tables.

@param $variables
  An associative array containing:
  - size: Optional. The number of indentations to create.
```

## Code

```php
function theme_indentation($variables) {
  $output = '';
  for ($n = 0; $n < $variables['size']; $n++) {
    $output .= '<div class="indentation">&nbsp;</div>';
  }
  return $output;
}
```

---
_Drupal 7.103 · [includes/theme.inc](https://github.com/drupal/drupal/blob/7.103/includes/theme.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
