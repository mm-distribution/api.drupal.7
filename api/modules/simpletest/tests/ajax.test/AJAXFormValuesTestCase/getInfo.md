# AJAXFormValuesTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/simpletest/tests/ajax.test`](../_file.md), lines 388–394 · [local source](../../../../../../source/modules/simpletest/tests/ajax.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/ajax.test#L388-L394)
- **Class:** [AJAXFormValuesTestCase](../AJAXFormValuesTestCase.md)
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
      'name' => 'AJAX command form values',
      'description' => 'Tests that form values are properly delivered to AJAX callbacks.',
      'group' => 'AJAX',
    );
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/ajax.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/ajax.test) · Licensed GPL-2.0-or-later (see LICENSE)._
