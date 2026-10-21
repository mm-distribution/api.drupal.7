# DrupalHTMLIdentifierTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 1010–1016 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L1010-L1016)
- **Class:** [DrupalHTMLIdentifierTestCase](../DrupalHTMLIdentifierTestCase.md)
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
      'name' => 'HTML identifiers',
      'description' => 'Test the functions drupal_html_class(), drupal_html_id() and drupal_clean_css_identifier() for expected behavior',
      'group' => 'System',
    );
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
