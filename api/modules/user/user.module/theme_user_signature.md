# theme_user_signature()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 3602–3614 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L3602-L3614)
- **Module/theme:** user
- **Topics:** [themeable](../../../topics/themeable.md)

## Signature

```php
function theme_user_signature($variables)
```

## Documentation

```text
Returns HTML for a user signature.

@param $variables
  An associative array containing:
  - signature: The user's signature.

@ingroup themeable
```

## Code

```php
function theme_user_signature($variables) {
  $signature = $variables['signature'];
  $output = '';

  if ($signature) {
    $output .= '<div class="clear">';
    $output .= '<div>—</div>';
    $output .= $signature;
    $output .= '</div>';
  }

  return $output;
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
