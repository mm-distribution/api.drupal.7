# _user_sort()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 3488–3492 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L3488-L3492)
- **Module/theme:** user

## Signature

```php
function _user_sort($a, $b)
```

## Documentation

_No docblock in source._

## Code

```php
function _user_sort($a, $b) {
  $a = (array) $a + array('weight' => 0, 'title' => '');
  $b = (array) $b + array('weight' => 0, 'title' => '');
  return $a['weight'] < $b['weight'] ? -1 : ($a['weight'] > $b['weight'] ? 1 : ($a['title'] < $b['title'] ? -1 : 1));
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
