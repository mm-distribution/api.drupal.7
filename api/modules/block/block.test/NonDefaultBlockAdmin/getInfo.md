# NonDefaultBlockAdmin::getInfo()

- **Type:** Method
- **File:** [`modules/block/block.test`](../_file.md), lines 384–390 · [local source](../../../../../source/modules/block/block.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.test#L384-L390)
- **Class:** [NonDefaultBlockAdmin](../NonDefaultBlockAdmin.md)
- **Module/theme:** block

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
      'name' => 'Non default theme admin',
      'description' => 'Check the administer page for non default theme.',
      'group' => 'Block',
    );
  }
```

---
_Drupal 7.103 · [modules/block/block.test](https://github.com/drupal/drupal/blob/7.103/modules/block/block.test) · Licensed GPL-2.0-or-later (see LICENSE)._
