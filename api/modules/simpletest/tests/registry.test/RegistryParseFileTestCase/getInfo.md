# RegistryParseFileTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/simpletest/tests/registry.test`](../_file.md), lines 8–14 · [local source](../../../../../../source/modules/simpletest/tests/registry.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/registry.test#L8-L14)
- **Class:** [RegistryParseFileTestCase](../RegistryParseFileTestCase.md)
- **Module/theme:** batch_test

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
      'name' => 'Registry parse file test',
      'description' => 'Parse a simple file and check that its resources are saved to the database.',
      'group' => 'System'
    );
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/registry.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/registry.test) · Licensed GPL-2.0-or-later (see LICENSE)._
