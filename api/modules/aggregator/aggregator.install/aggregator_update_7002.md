# aggregator_update_7002()

- **Type:** Function
- **File:** [`modules/aggregator/aggregator.install`](_file.md), lines 298–306 · [local source](../../../../source/modules/aggregator/aggregator.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.install#L298-L306)
- **Module/theme:** aggregator
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function aggregator_update_7002()
```

## Documentation

```text
Add queued timestamp.
```

## Code

```php
function aggregator_update_7002() {
  db_add_field('aggregator_feed', 'queued', array(
    'type' => 'int',
    'not null' => TRUE,
    'default' => 0,
    'description' => 'Time when this feed was queued for refresh, 0 if not queued.',
  ));
  db_add_index('aggregator_feed', 'queued', array('queued'));
}
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.install](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.install) · Licensed GPL-2.0-or-later (see LICENSE)._
