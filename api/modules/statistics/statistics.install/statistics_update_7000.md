# statistics_update_7000()

- **Type:** Function
- **File:** [`modules/statistics/statistics.install`](_file.md), lines 147–155 · [local source](../../../../source/modules/statistics/statistics.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.install#L147-L155)
- **Module/theme:** statistics
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function statistics_update_7000()
```

## Documentation

```text
Update the {accesslog}.sid column to match the length of {sessions}.sid
```

## Code

```php
function statistics_update_7000() {
  db_change_field('accesslog', 'sid', 'sid', array(
    'type' => 'varchar',
    'length' => 128,
    'not null' => TRUE,
    'default' => '',
    'description' => 'Browser session ID of user that visited page.',
  ));
}
```

---
_Drupal 7.103 · [modules/statistics/statistics.install](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.install) · Licensed GPL-2.0-or-later (see LICENSE)._
