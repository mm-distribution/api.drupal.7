# PHPFilterTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/php/php.test`](../_file.md), lines 54–60 · [local source](../../../../../source/modules/php/php.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/php/php.test#L54-L60)
- **Class:** [PHPFilterTestCase](../PHPFilterTestCase.md)
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
      'name' => 'PHP filter functionality',
      'description' => 'Make sure that PHP filter properly evaluates PHP code when enabled.',
      'group' => 'PHP',
    );
  }
```

---
_Drupal 7.103 · [modules/php/php.test](https://github.com/drupal/drupal/blob/7.103/modules/php/php.test) · Licensed GPL-2.0-or-later (see LICENSE)._
