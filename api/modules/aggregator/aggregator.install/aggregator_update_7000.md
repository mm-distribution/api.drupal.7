# aggregator_update_7000()

- **Type:** Function
- **File:** [`modules/aggregator/aggregator.install`](_file.md), lines 284–286 · [local source](../../../../source/modules/aggregator/aggregator.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.install#L284-L286)
- **Module/theme:** aggregator
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function aggregator_update_7000()
```

## Documentation

```text
Add hash column to aggregator_feed table.
```

## Code

```php
function aggregator_update_7000() {
  db_add_field('aggregator_feed', 'hash', array('type' => 'varchar', 'length' => 64, 'not null' => TRUE, 'default' => ''));
}
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.install](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.install) · Licensed GPL-2.0-or-later (see LICENSE)._
