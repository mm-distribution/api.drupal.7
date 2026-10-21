# ConfirmFormTest::getInfo()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 3168–3174 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L3168-L3174)
- **Class:** [ConfirmFormTest](../ConfirmFormTest.md)
- **Module/theme:** system

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
      'name' => 'Confirm form',
      'description' => 'Tests that the confirm form does not use external destinations.',
      'group' => 'System',
    );
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
