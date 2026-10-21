# CronRunTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 798–804 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L798-L804)
- **Class:** [CronRunTestCase](../CronRunTestCase.md)
- **Module/theme:** system

## Signature

```php
public static function getInfo()
```

## Documentation

```text
Implement getInfo().
```

## Code

```php
  public static function getInfo() {
    return array(
      'name' => 'Cron run',
      'description' => 'Test cron run.',
      'group' => 'System'
    );
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
