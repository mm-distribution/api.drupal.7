# DateTimeFunctionalTest::getInfo()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 1324–1330 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L1324-L1330)
- **Class:** [DateTimeFunctionalTest](../DateTimeFunctionalTest.md)
- **Module/theme:** system

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
      'name' => 'Date and time',
      'description' => 'Configure date and time settings. Test date formatting and time zone handling, including daylight saving time.',
      'group' => 'System',
    );
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
