# ProfileBlockTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/profile/profile.test`](../_file.md), lines 388–394 · [local source](../../../../../source/modules/profile/profile.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.test#L388-L394)
- **Class:** [ProfileBlockTestCase](../ProfileBlockTestCase.md)
- **Module/theme:** profile

## Signature

```php
public static function getInfo()
```

## Documentation

_No docblock in source._

## Code

```php
  public static function getInfo() {
    return array(
      'name' => 'Block availability',
      'description' => 'Check if the Author Information block is available.',
      'group' => 'Profile',
    );
  }
```

---
_Drupal 7.103 · [modules/profile/profile.test](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.test) · Licensed GPL-2.0-or-later (see LICENSE)._
