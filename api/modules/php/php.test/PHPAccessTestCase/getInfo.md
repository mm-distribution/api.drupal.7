# PHPAccessTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/php/php.test`](../_file.md), lines 95–101 · [local source](../../../../../source/modules/php/php.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/php/php.test#L95-L101)
- **Class:** [PHPAccessTestCase](../PHPAccessTestCase.md)
- **Module/theme:** php

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
      'name' => 'PHP filter access check',
      'description' => 'Make sure that users who don\'t have access to the PHP filter can\'t see it.',
      'group' => 'PHP',
    );
  }
```

---
_Drupal 7.103 · [modules/php/php.test](https://github.com/drupal/drupal/blob/7.103/modules/php/php.test) · Licensed GPL-2.0-or-later (see LICENSE)._
