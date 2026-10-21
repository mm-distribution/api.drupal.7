# ActionsConfigurationTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/simpletest/tests/actions.test`](../_file.md), lines 4–10 · [local source](../../../../../../source/modules/simpletest/tests/actions.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/actions.test#L4-L10)
- **Class:** [ActionsConfigurationTestCase](../ActionsConfigurationTestCase.md)
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
      'name' => 'Actions configuration',
      'description' => 'Tests complex actions configuration by adding, editing, and deleting a complex action.',
      'group' => 'Actions',
    );
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/actions.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/actions.test) · Licensed GPL-2.0-or-later (see LICENSE)._
