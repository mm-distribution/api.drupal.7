# FormsRedirectTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/simpletest/tests/form.test`](../_file.md), lines 1822–1828 · [local source](../../../../../../source/modules/simpletest/tests/form.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test#L1822-L1828)
- **Class:** [FormsRedirectTestCase](../FormsRedirectTestCase.md)
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
      'name' => 'Form redirecting',
      'description' => 'Tests functionality of drupal_redirect_form().',
      'group' => 'Form API',
    );
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/form.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test) · Licensed GPL-2.0-or-later (see LICENSE)._
