# UpdateTestContribCase::getInfo()

- **Type:** Method
- **File:** [`modules/update/update.test`](../_file.md), lines 284–290 · [local source](../../../../../source/modules/update/update.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.test#L284-L290)
- **Class:** [UpdateTestContribCase](../UpdateTestContribCase.md)
- **Module/theme:** update

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
      'name' => 'Update contrib functionality',
      'description' => 'Tests how the Update Manager module handles contributed modules and themes in a series of functional tests using mock XML data.',
      'group' => 'Update',
    );
  }
```

---
_Drupal 7.103 · [modules/update/update.test](https://github.com/drupal/drupal/blob/7.103/modules/update/update.test) · Licensed GPL-2.0-or-later (see LICENSE)._
