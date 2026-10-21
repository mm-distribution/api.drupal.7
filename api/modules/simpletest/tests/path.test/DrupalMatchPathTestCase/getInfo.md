# DrupalMatchPathTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/simpletest/tests/path.test`](../_file.md), lines 16–22 · [local source](../../../../../../source/modules/simpletest/tests/path.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/path.test#L16-L22)
- **Class:** [DrupalMatchPathTestCase](../DrupalMatchPathTestCase.md)
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
      'name' => 'Drupal match path',
      'description' => 'Tests the drupal_match_path() function to make sure it works properly.',
      'group' => 'Path API',
    );
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/path.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/path.test) · Licensed GPL-2.0-or-later (see LICENSE)._
